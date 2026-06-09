# Making actions and content discoverable by Apple Intelligence

**Framework**: App Intents

Equip the system so that Siri can work with your app by adding specific schemas from relevant domains.

#### Overview

A big part of people’s personal context is the apps they use every day. To help Apple Intelligence work with your app, the system needs to understand what your app can do and what content it manages. A *schema* is a special app intent, entity, or enumeration that the framework defines for a specific purpose.

![An illustration that shows app schema domains next to the Apple Intelligence icon.](https://docs-assets.developer.apple.com/published/5f3dbd07e292e965af51721a6bfc60b7/making-actions-and-content-available-to-apple-intelligence%402x.png)

Each schema’s properties give Apple Intelligence the information it needs to work with your app. When you adopt schemas, you make your app’s actions and content available to the app toolbox, which Apple Intelligence draws on to service requests. You can add schemas to your app by conforming its existing types to a schema, or by creating new types with framework macros.

A *domain* is a collection of schemas for a specific category of functionality. For example, the [`Calendar`](app-schema-domain-calendar.md) domain has schemas for creating, updating, and deleting events. The [`Messages`](app-schema-domain-messages.md) domain has schemas for sending, drafting, editing, and unsending messages. See [`App schema domains`](app-schema-domains.md) for a list of the domain pages, each of which catalogs the schemas that belong to that domain.

When you build and run your app with schemas in place, a person can take action with your app, such as by communicating with Siri. For example, a person with a plant-journaling app might say, “Open the close-up of my basil plant from this morning.” Apple Intelligence identifies the correct app, the entities that represent the basil plant, and invokes the right *intent* that carries out the request. This works because that intent conforms to the `.photos.openAsset` schema, which tells the system exactly what that action does and what content it operates on.

> **Note**: Schemas define structural inputs for Apple Intelligence, which means Siri can interpret the various phrases that different people naturally say in everyday conversations.

See [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md) for more information about the fundamentals of app intents, entities, and enumerations.

#### Choose One or More Domains for Your App

Look through the available domains in [`App schema domains`](app-schema-domains.md) and identify which categories match your app’s functionality. Each domain page lists its schemas and example phrases that show how people invoke them through Siri.

An app can adopt schemas from multiple domains. For example, a houseplant-journaling app can adopt schemas from the [`Notes`](app-schema-domain-notes.md) domain, which has schemas that create new notes and update existing notes. It can also adopt schemas from the [`Photos`](app-schema-domain-photos.md) domain, which has a wide variety of intents, including those for opening, editing, and deleting photo assets.

Only apply schemas for actions and content that genuinely match the domain’s intended purpose. The following domains require that your app supports every schema in the group:

- [`Mail`](app-schema-domain-mail.md)
- [`Clock`](app-schema-domain-clock.md)
- [`Messages`](app-schema-domain-messages.md)

In other words, if you decide to support one schema in those domains, you need to adopt them all.

> **Note**: Xcode notifies you at build time when you need to support additional schemas in a group.

#### Support a Schema By Creating a New Type

To generate a starting implementation for a schema, type the domain name followed by an underscore in Xcode. Then select the schema from the suggestions list. For example, to get the framework’s code snippet for the [`openAsset`](appschema/photosintent/openasset.md), which is an intent schema in the photos domain, type: “photos_” and select: `photos_openAsset`. An intent schema represents a specific action that your app can do, in this case opening or presenting a photo.

```swift
photos_openAsset
```

The snippet expands into a template struct with the schema macro and the schema requirements, which can be properties, stub methods, or both:

```swift
@AppIntent(schema: .photos.openAsset)
struct OpenMediaAssetIntent: OpenIntent {
    var target: <#PhotoEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

Connect the template code to your app by replacing the placeholders, and optionally rename the type to better fit your project. The example renames the open asset intent to `OpenPlantPhotoIntent` and replaces the placeholders:

- The `target` property’s type is `PlantPhotoEntity`, another type within the app.
- The body of the `perform()` method now has code that calls into the rest of the app.

```swift
@AppIntent(schema: .photos.openAsset)
struct OpenPlantPhotoIntent: OpenIntent {
    var target: PlantPhotoEntity

    func perform() async -> some IntentResult {
        // Present the photo for this plant on the display
        // by calling into the app's main code.
        // ...

        return .result()
    }
}
```

In this example, the `OpenPlantPhotoIntent` is the intent and the system invokes its action by calling the `perform()` method. The properties on an intent struct serve as implicit parameters for the method. The system configures these properties before calling `perform()`, which has no explicit parameters itself.

Apple Intelligence only uses the properties that each schema defines. You can add extra properties if they’re optional, which only the Shortcuts app recognizes.

The `target` property references `PlantPhotoEntity`, which conforms to a schema through the [`AppEntity(schema:)`](appentity(schema:).md) macro. Creating an entity schema follows the same pattern as an intent schema. Type the domain prefix and select the entity schema from the suggestions, expand the snippet into a template, and fill in the placeholders with your app’s types and logic.

The following entity supports the `.photos.asset` schema:

```swift
@AppEntity(schema: .photos.asset)
struct PlantPhotoEntity {

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(
            title: "\(photo.name)",
            subtitle: "\(photo.creationDate.formatted(date: .abbreviated, time: .omitted))"
        )
    }

    static let defaultQuery = PlantPhotoEntityQuery()

    var id: Int { photo.id }

    var creationDate: Date? { photo.creationDate }
    var location: PlaceDescriptor? { nil }
    var assetType: PhotoAssetType? { .photo }
    var isFavorite: Bool { photo.isFavorite }
    var isHidden: Bool { photo.isHidden }
    var hasSuggestedEdits: Bool { false }
    var aperture: Double? { nil }
    var exposure: Double? { nil }
    var saturation: Double? { nil }
    var warmth: Double? { nil }
    var filter: PhotoFilterEffectType? { nil }
    var isPortraitModeEnabled: Bool? { nil }

    var photo: PlantPhoto

    init(photo: PlantPhoto) {
        self.photo = photo
    }
}
```

Set schema properties to `nil` when your app doesn’t support them, such as `location` or `aperture` in this example.

The entity above references `PhotoAssetType` for its `assetType` property. Enumeration schemas define a fixed set of values that a property can hold. Unlike intent and entity schemas, which represent actions and content, an enum schema represents the valid options for a specific property. The following enumeration conforms to the `.photos.assetType` schema:

```swift
@AppEnum(schema: .photos.assetType)
enum PhotoAssetType: String, Sendable {
    case photo
    case video

    static var caseDisplayRepresentations: [Self: DisplayRepresentation] {
        [
            .photo: "Photo",
            .video: "Video"
        ]
    }
}
```

#### Add Schema Conformance to an Existing Type

If your app already has a type that matches a schema’s purpose, add the appropriate framework macro on the line above the existing type’s declaration:

- [`AppIntent(schema:)`](appintent(schema:).md) for intents
- [`AppEntity(schema:)`](appentity(schema:).md) for entities
- [`AppEnum(schema:)`](appenum(schema:).md) for enumerations

The macro generates protocol conformance and validates that your type satisfies the schema’s requirements. If your type is missing a required property, Xcode generates an error at build time with a Fix-It that adds it for you. The macro produces the same conformance regardless of whether the type is new or existing.

> 💡 **Tip**: Increase the number of ways people can interact with your app through Apple Intelligence by adopting optional schemas that fit the app’s capabilities.

#### Migrate Existing Intents to Schemas

If your app exposes intents through the Shortcuts app, some of those intents may overlap with available schemas. When the existing intent’s properties already satisfy the schema’s requirements, add the macro directly. For example, if your app has an `OpenPhotoIntent` with a `target` property typed to a photo entity, that’s exactly what `.photos.openAsset` requires. Adding `@AppIntent(schema: .photos.openAsset)` above the declaration is the only change you need to make.

When adding a schema to an intent that has incompatible properties that might break existing shortcuts, create a new intent alongside the existing one. Removing or changing the older intent breaks any shortcuts that use it. As a temporary workaround, configure the new intent so that it’s only available to Apple Intelligence by setting [`isAssistantOnly`](assistantschemaintent/isassistantonly.md) to `true`:

```swift
@AppIntent(schema: .photos.createAssets)
struct CreateAssetsIntent: AppIntent {

    // ...

    static let isAssistantOnly: Bool = true

    // ...

    @MainActor
    func perform() async throws -> some ReturnsValue<[PlantPhotoEntity]> {
        // ...
    }
}
```

When you set an intent’s `isAssistantOnly` property to `true`, it effectively hides the intent from the Shortcuts app. This avoids presenting both intents as a duplicate pair. During this period, the old intent continues to serve existing shortcuts, and the new intent handles requests people make through Siri. To complete the transition, remove `isAssistantOnly` so the new intent appears in Shortcuts, then retire the old intent. For more information about giving people time to update their shortcuts, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

#### Help the System Discover Your Content

Schemas define your app’s capabilities and content at build time, but the system needs to find specific instances at runtime when someone makes a request.

Submit your entities to the Spotlight semantic index so the system indexes your app’s content and matches it to requests. For more information about indexing, see [`Donations and discovery`](donations-and-discovery.md).

Annotate your views with entity data so Apple Intelligence can connect what’s visible on screen to a verbal conversation with a person. You can also make your entities transferable so other apps can use them directly. For more information about view annotations and transferable entities, see [`Providing contextual cues to Apple Intelligence and Siri`](providing-contextual-cues-to-apple-intelligence-and-siri.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-by-apple-intelligence)*