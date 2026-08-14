# Adopting App Intents to support system experiences

**Framework**: App Intents

Create app intents and entities so people can use your app’s content and actions across system experiences.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

This sample contains a main app, a widget extension, and a shared Swift package, and shows you how to make an app’s content and actions discoverable by Apple Intelligence and other system experiences. The sample app uses a shared Swift package to organize its intents, entities, and data model so both the main app and a widget extension can use them.

By adopting the App Intents framework, you let people:

- Find and run the app’s intents in Shortcuts.
- Create custom shortcuts or use the provided “Find Closest” App Shortcut in Shortcuts.
- Place custom shortcuts or the App Shortcut on the Home Screen as a bookmark.
- Search for a landmark, photo, or the “Find Closest” App Shortcut in Spotlight.
- Circle an object onscreen or in the camera to view matching results using visual intelligence.
- Trigger a custom shortcut or the App Shortcut using the Action button.
- Use custom shortcuts or the App Shortcut from Siri Suggestions.
- View information about a landmark in the app, then ask Siri for a content summary.
- Search for landmarks and photos, browse photo albums, and view photos on the map in the app.
- Browse landmark collections or photo albums as a slideshow, favorite items, or upload a photo from the app’s widget.
- Pin, favorite, share, tag, or add items to collections and albums from context menus.

#### Describe Actions As App Intents and Entities

The app contains many actions and makes them available to the system as app intents, so people can create custom shortcuts and invoke them across system experiences. For example, the app offers key actions such as finding the closest landmark or opening a landmark in the app. This app intent opens a landmark in the app:

```swift
public struct OpenLandmarkIntent: OpenIntent {
    public static let title: LocalizedStringResource = "Open Landmark"
    public init() {}

    @Parameter(title: "Landmark", requestValueDialog: "Which landmark?")
    public var target: LandmarkEntity

    public init(target: LandmarkEntity) {
        self.target = target
    }

    /**
     If your app intent conforms to the `OpenIntent` protocol and the intent's only
     functionality is to open the app to a specific scene,
     you don't have to implement your own `perform()` method in your iOS, iPadOS, or Mac app you built with Mac Catalyst.
     */
    #if os(macOS)
    @Dependency var navigator: Navigator

    public func perform() async throws -> some IntentResult {

        await navigator.navigate(to: target)

        return .result()
    }
    #endif
}
```

To use your data as input and output of app intents and make the data available to the system, you use app entities. An app entity exposes only the parts of your stored model object that the system needs. It also adds required information to understand the data or to use it in system experiences. For example, the `LandmarkEntity` of the sample app provides required `typeDisplayRepresentation` and `displayRepresentation` properties but doesn’t include every property of the `Landmark` model object:

```swift
public struct LandmarkEntity: IndexedEntity {
    public static var typeDisplayRepresentation: TypeDisplayRepresentation {
        return TypeDisplayRepresentation(
            name: LocalizedStringResource(
                "Landmark",
                table: "AppIntents",
                comment: "The type name for the landmark entity"
            ),
            numericFormat: "\(placeholder: .int) landmarks"
        )
    }

    public var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(
            title: "\(name)",
            subtitle: "\(continent)",
            image: .init(named: landmark.thumbnailImageName)
        )
    }

    public static let defaultQuery = LandmarkEntityQuery()

    public var id: Int { landmark.id }

    @ComputedProperty(indexingKey: \.displayName)
    public var name: String { landmark.name }

    // ...

}
```

For more information about describing actions as app intents and app entities, refer to [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md) and [`Creating your first app intent`](creating-your-first-app-intent.md).

#### Organize Intents Using a Shared Swift Package

The app organizes its App Intents code in a shared Swift package called `TravelTrackingShared`, with three layered libraries:

- `TravelTrackingCore` contains data models, persistence functionality, sample data, and utilities.
- `TravelTrackingIntents` depends on `TravelTrackingCore` and contains app entities, app intents, and intent helpers.
- `TravelTrackingSnippets` depends on `TravelTrackingIntents` and contains snippet intents and SwiftUI views.

Both the main app and the widget extension import the shared `TravelTrackingShared` package, so the package defines intents and entities once and makes them available everywhere.

#### Make Your App Entities Transferable

To enable Apple Intelligence to provide the app’s content to other intents, `LandmarkEntity` implements the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol and provides plain-text, image, PDF, and `ValueRepresentation` representations that Siri understands. While the [`FileRepresentation`](https://developer.apple.com/documentation/coretransferable/filerepresentation) and [`DataRepresentation`](https://developer.apple.com/documentation/coretransferable/datarepresentation) types work great for known formats like PDFs or images, [`IntentValueRepresentation`](intentvaluerepresentation.md) handles structured types, such as `PlaceDescriptor` for locations, that don’t have an associated file format:

```swift
extension LandmarkEntity: Transferable {
    public static var transferRepresentation: some TransferRepresentation {

        FileRepresentation(exportedContentType: .pdf) { @MainActor landmark in
            let url = URL.documentsDirectory.appending(path: "\(landmark.name).pdf")

            let renderer = ImageRenderer(content: VStack {
                Image(landmark.landmark.backgroundImageName)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                Text(landmark.name)
                Text("Continent: \(landmark.continent)")
                Text(landmark.description)
            }.frame(width: 600))

            renderer.render { size, renderer in
                var box = CGRect(x: 0, y: 0, width: size.width, height: size.height)

                guard let pdf = CGContext(url as CFURL, mediaBox: &box, nil) else {
                    return
                }
                pdf.beginPDFPage(nil)
                renderer(pdf)
                pdf.endPDFPage()
                pdf.closePDF()
            }

            return .init(url)
        }

        DataRepresentation(exportedContentType: .image) {
            try $0.imageRepresentationData
        }

        DataRepresentation(exportedContentType: .plainText) {
            Data("""
            Landmark: \($0.name)
            Description: \($0.description)
            """.utf8)
        }

        ValueRepresentation(exporting: \.placeDescriptor)
    }
}
```

The `placeDescriptor` computed property creates a `PlaceDescriptor` from the GeoToolbox framework that contains the landmark’s coordinates and name:

```swift
public var placeDescriptor: PlaceDescriptor {
    PlaceDescriptor(
        representations: [.coordinate(landmark.locationCoordinate)],
        commonName: landmark.name
    )
}
```

When a shortcut passes this entity to Maps, Maps receives a `PlaceDescriptor` it can navigate to, not just an image or PDF.

#### Provide Onscreen Context

When the landmark becomes visible onscreen, the app uses the `.appEntityIdentifier` view modifier to make the entity discoverable by Apple Intelligence and Siri:

```swift
ScrollView(.vertical) {
    // ... landmark content
}
.appEntityIdentifier(EntityIdentifier(for: LandmarkEntity.self, identifier: landmark.id))
```

The `.appEntityIdentifier` modifier also works on gallery views, enabling contextual references such as “the second one” or “the deer photo”:

```swift
GalleryHorizontalListView(
    items: landmarkList,
    entityIdentifier: { EntityIdentifier(for: LandmarkEntity.self, identifier: $0.id) }
)
```

For more information about making onscreen content available to Siri and Apple Intelligence, refer to [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

#### Process Entities Efficiently Using an Entity Collection

When an intent receives entities as parameters, the system resolves each one by calling the entity query and populating all properties. For intents that only need entity identifiers, for example, tagging or deleting, this resolution is unnecessary overhead.

[`EntityCollection`](entitycollection.md) stores an array of entity identifiers instead of fully resolved entities. The system passes the identifiers directly to the intent’s `perform()` method without loading the full entity contents:

```swift
public struct TagPhotosIntent: AppIntent {
    public static let title: LocalizedStringResource = "Tag Travel Photos"
    public init() {}
    public static let description: IntentDescription = "Tag selected travel photos with a label."

    @Parameter(title: "Photos", requestValueDialog: "Which photo?")
    var photos: EntityCollection<PhotoEntity>

    @Parameter(title: "Tag", default: "favorite")
    var tag: String

    @Dependency var modelData: ModelData

    public static var parameterSummary: some ParameterSummary {
        Summary("Tag \(\.$photos) with \(\.$tag)")
    }

    public func perform() async throws -> some IntentResult & ProvidesDialog {
        let start = ContinuousClock.now
        await tagPhotos(with: tag)
        let elapsed = start.duration(to: .now)
        let millis = elapsed.components.seconds * 1000 + elapsed.components.attoseconds / 1_000_000_000_000_000
        return .result(dialog: "Tagged \(photos.count) photos with '\(tag)' in \(millis)ms.")
    }

    // Use identifiers for bulk operations, which avoids resolving each `PhotoEntity`.
    private func tagPhotos(with tag: String) async {
        await modelData.tagPhotos(ids: photos.identifiers, tag: tag)
    }
}
```

#### Use Entities Across Devices

When Siri continues a conversation across devices, the system carries entity references alongside the conversation. If an entity uses locally generated IDs, the same entity can have a different ID on each device, and Siri can’t find it.

[`SyncableEntity`](syncableentity.md) declares to the system that an entity’s ID is stable across devices, so Siri can find it. The sample app’s `PhotoEntity` conforms to the `SyncableEntity` protocol:

```swift
@AppEntity(schema: .photos.asset)
struct PhotoEntity: IndexedEntity, SyncableEntity {
    // ...
    var id: Int  // Stable across devices.
    // ...
}
```

For entities that use different local and stable IDs, `SyncableEntityIdentifier` pairs them into a single ID:

```swift
struct PhotoEntity: AppEntity, SyncableEntity {
    var id: SyncableEntityIdentifier<String, String>

    init(localID: String, stableID: String) {
        self.id = SyncableEntityIdentifier(local: localID, stable: stableID)
    }
}
```

If a request stays on a device, the system uses the local ID. Across devices, the system uses the stable ID.

#### Adopt App Schemas

The app’s `PhotoEntity` adopts the `photos.asset` app schema, giving the system an understanding of what the photos represent. Siri, Shortcuts, and Spotlight can then work with the app’s photos:

```swift
@AppEntity(schema: .photos.asset)
public struct PhotoEntity: IndexedEntity, SyncableEntity {
    // ...
}
```

For additional information about adopting app schemas, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md).

#### Configure Widgets with Union Value Parameters

The app includes a widget that displays a slideshow from either a landmark collection or a photo album. The `@UnionValue` macro lets a single parameter accept one of several types:

```swift
@UnionValue
enum TravelGalleryContent {
    case landmarkCollection(LandmarkCollectionEntity)
    case photoAlbum(PhotoAlbumEntity)

    static var typeDisplayRepresentation: TypeDisplayRepresentation { "Travel Gallery" }
    static let caseDisplayRepresentations: [Cases: DisplayRepresentation] = [
        .landmarkCollection: "Landmark Collection",
        .photoAlbum: "Photo Album"
    ]

    /// Stable identifier that scopes widget state (gallery index) per
    /// configured content, so two widgets showing different albums or
    /// collections track their position independently.
    var contentKey: String {
        switch self {
        case .landmarkCollection(let collection): "landmarkCollection-\(collection.id)"
        case .photoAlbum(let album): "photoAlbum-\(album.id)"
        }
    }
}
```

The widget configuration intent uses this union value as a parameter for a switch statement to provide a parameter summary:

```swift
struct TravelGalleryWidgetIntent: WidgetConfigurationIntent {
    static let title: LocalizedStringResource = "Travel Gallery"
    static let description: IntentDescription = "Choose a landmark collection or photo album to display as a slideshow."

    @Parameter var content: TravelGalleryContent?

    static var parameterSummary: some ParameterSummary {
        Switch(\.$content) {
            Case(.landmarkCollection) {
                Summary("Show landmarks from \(\.$content)")
            }
            Case(.photoAlbum) {
                Summary("Cycle through \(\.$content) photos")
            }
            DefaultCase {
                Summary("Show \(\.$content)")
            }
        }
    }
}
```

`@UnionValue` parameters work in every system experience your intent supports, including the Shortcuts app.

#### Run Long Running Intents

By default, intents have only a short time to finish their work. For tasks that take longer, for example, uploading a large photo in chunks, [`LongRunningIntent`](longrunningintent.md) extends execution well beyond the usual limit. The framework manages the background task lifecycle, and the system shows progress updates automatically as a Live Activity:

```swift
public struct UploadPhotoIntent: LongRunningIntent, CancellableIntent {
    public static let title: LocalizedStringResource = "Upload Photo"
    public static let description: IntentDescription = "Upload the current photo with progress tracking."
    
    @Parameter(requestValueDialog: "Which photo?")
    public var photo: IntentFile
    
    var name: String { photo.filename }
    
    public init() {}
    
    public init(photo: IntentFile) {
        self.photo = photo
    }
    
    public func perform() async throws -> some IntentResult & ProvidesDialog {
        let result = try await performBackgroundTask { @Sendable in
            let chunks = calculateChunks()
            progress.totalUnitCount = Int64(chunks)
            progress.localizedDescription = "\(name)"
            progress.localizedAdditionalDescription = "Preparing upload…"
            
            for chunk in 1...chunks {
                try await uploadChunk(chunk)
                progress.completedUnitCount = Int64(chunk)
                progress.localizedAdditionalDescription = "Uploaded \(Int((Double(chunk) / Double(chunks)) * 100))%"
            }
            return "Uploaded \(name) successfully!"
        } onCancel: { reason in
            cleanup(for: reason)
        }
        return .result(dialog: "\(result)")
    }
    
    // ...
}
```

[`CancellableIntent`](cancellableintent.md) gives the intent a chance to clean up any data when it is canceled, whether the person taps cancel, the system needs to reclaim resources, or the intent times out. The intent’s `onCancel` handler receives the cancellation reason.

#### Support Undo

The app’s `UpdateFavoriteIntent` conforms to [`UndoableIntent`](undoableintent.md), which lets the system offer an undo option after the intent runs. The `undo()` method reverses the intent’s action using the same parameters:

```swift
public struct UpdateFavoriteIntent: AppIntent, UndoableIntent {
    // ...

    @MainActor
    public func perform() async throws -> some IntentResult {
        switch item {
        case .landmark(let landmark):
            modelData.updateFavorite(isFavorite, landmark: landmark)
        case .photo(let photo):
            modelData.updateFavorite(isFavorite, photoID: photo.id)
        }
        WidgetCenter.shared.reloadTimelines(ofKind: "TravelGalleryWidget")
        return .result()
    }

    @MainActor
    public func undo() async throws {
        switch item {
        case .landmark(let landmark):
            modelData.updateFavorite(!isFavorite, landmark: landmark)
        case .photo(let photo):
            modelData.updateFavorite(!isFavorite, photoID: photo.id)
        }
        WidgetCenter.shared.reloadTimelines(ofKind: "TravelGalleryWidget")
    }
}
```

#### Control Where Intents Run

When intents live in a shared package that both the app and its extensions link to, the system decides which process runs each intent. [`IntentExecutionTargets`](intentexecutiontargets.md) lets you control this explicitly.

For example, the app’s widget has read-only access to the data model. When someone taps the favorite button on the widget, the write operation needs to run in the main app:

```swift
struct UpdateFavoriteIntent: AppIntent {
    // ...

    static var allowedExecutionTargets: ExecutionTargets { .main }

    // ...
}
```

`ExecutionTargets` is available on both [`AppIntent`](appintent.md) and [`EntityQuery`](entityquery.md), so you can target the main app (`.main`), an App Intents extension (`.appIntentsExtension`), a widget extension (`.widgetKitExtension`), or any combination.

#### Offer Interactive Snippets

The app’s “Find Closest” App Shortcut runs an app intent that finds the nearest landmark without opening the app and lets people find tickets to visit it. Instead of taking them to the app, the intent presents an interactive snippet that appears as an overlay at the top of the screen. To display the interactive snippet, the app’s `ClosestLandmarkIntent` returns a [`SnippetIntent`](snippetintent.md) that presents the interactive snippet in its `perform()` method:

```swift
public struct ClosestLandmarkIntent: AppIntent {
    public static let title: LocalizedStringResource = "Find Closest Landmark"
    public init() {}

    @Dependency var modelData: ModelData

    public func perform() async throws -> some ReturnsValue<LandmarkEntity> & ShowsSnippetIntent & ProvidesDialog {
        let landmark = await self.findClosestLandmark()

        return .result(
            value: landmark,
            dialog: IntentDialog(
                full: "The closest landmark is \(landmark.name).",
                supporting: "\(landmark.name) is located in \(landmark.continent)."
            ),
            snippetIntent: LandmarkSnippetIntent(landmark: landmark)
        )
    }
}
```

For more information about displaying interactive snippets, refer to [`Displaying static and interactive snippets`](displaying-static-and-interactive-snippets.md).

#### Add Entities to the Spotlight Index

The app describes its data as app entities so the system can use that data when running app intents. The app also donates the entities to the semantic search index so people can find them in Spotlight. The following example shows how the app’s `LandmarkEntity` conforms to [`IndexedEntity`](indexedentity.md) and uses Swift macros to add the indexing keys that Spotlight needs.

```swift
struct LandmarkEntity: IndexedEntity {
    // ...

    // Maps the description variable to the Spotlight indexing key `contentDescription`.
    @ComputedProperty(indexingKey: \.contentDescription)
    public var description: String { landmark.description }

    // Custom Spotlight attribute key for the continent. The key name is a compile-time-known
    // identifier; the precondition fails fast with a useful message if it ever becomes invalid.
    private static let continentIndexingKey: CSCustomAttributeKey = {
        guard let key = CSCustomAttributeKey(
            keyName: "com_AppIntentsTravelTracking_LandmarkEntity_continent"
        ) else {
            preconditionFailure("Invalid CSCustomAttributeKey name; must satisfy reserved-name rules.")
        }
        return key
    }()

    // Maps the continent variable to a custom Spotlight indexing key.
    @ComputedProperty(customIndexingKey: continentIndexingKey)
    public var continent: String { landmark.continent }

    // ...
}
```

In a utility function, the app donates the landmark entities to the Spotlight index:

```swift
public static func donateLandmarks(modelData: ModelData) async throws {
    let landmarkEntities = await modelData.landmarkEntities
    try await CSSearchableIndex.default().indexAppEntities(landmarkEntities)
}
```

For more information, refer to [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

#### Integrate Search Results with Visual Intelligence

With visual intelligence, people circle items onscreen or in the visual intelligence camera to search for matching results across apps that support visual intelligence. To support visual intelligence search, the sample app implements an [`IntentValueQuery`](intentvaluequery.md) to find matching landmarks:

```swift
@UnionValue
enum VisualSearchResult {
    case landmark(LandmarkEntity)
    case collection(LandmarkCollectionEntity)
}

struct LandmarkIntentValueQuery: IntentValueQuery {

    @Dependency var modelData: ModelData
    init() {}

    func values(for input: SemanticContentDescriptor) async throws -> [VisualSearchResult] {

        guard let pixelBuffer: CVReadOnlyPixelBuffer = input.pixelBuffer else {
            return []
        }

        let landmarks = try await modelData.search(matching: pixelBuffer)

        return landmarks
    }
}
```

For more information about integrating your app with visual intelligence, refer to [`Visual Intelligence`](https://developer.apple.com/documentation/visualintelligence).

## See Also

- [Apple Intelligence and Siri AI](apple-intelligence-and-siri-ai.md)
  Integrate your app with Apple Intelligence and bring it to Siri AI.
- [Spotlight integration](spotlight.md)
  Add your entities to your app’s Spotlight index, and automate the indexing of your content.
- [App Shortcuts](app-shortcuts.md)
  Improve the experience of using your app intents and entities in system experiences like Siri, Spotlight, and the Shortcuts app.
- [Widgets, Live Activities, and Controls](widgets-live-activities-and-controls.md)
  Implement interactive widgets, controls, watch complications, and Live Activities using app intents.
- [Hardware interactions](hardware-interactions.md)
  Run your App Shortcuts from the Action button on iPhone or Apple Watch, or launch your own conversational app from the side button on iPhone.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.
- [Visual intelligence](visual-intelligence.md)
  Match images to your app’s content and report the results to the Visual Intelligence framework using an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences)*