# DocumentGroup

**Framework**: SwiftUI  
**Kind**: struct

A scene that enables support for opening, creating, and saving documents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
struct DocumentGroup<Document, Content> where Content : View
```

## Mentions

- [Building and customizing the menu bar with SwiftUI](building-and-customizing-the-menu-bar-with-swiftui.md)

#### Overview

Use a `DocumentGroup` scene to tell SwiftUI what kinds of documents your app can open when you declare your app using the [`App`](app.md) protocol.

Initialize a document group scene by passing in the document model and a view capable of displaying the document type. The document types you supply to `DocumentGroup` must conform to [`FileDocument`](filedocument.md) or [`ReferenceFileDocument`](referencefiledocument.md). SwiftUI uses the model to add document support to your app. In macOS this includes document-based menu support, including the ability to open multiple documents. On iOS this includes a document browser that can navigate to the documents stored on the file system and multiwindow support:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextFile()) { configuration in
            ContentView(document: configuration.$document)
        }
    }
}
```

Any time the configuration changes, SwiftUI updates the contents with that new configuration, similar to other parameterized builders.

##### Viewing Documents

If your app only needs to display but not modify a specific document type, you can use the file viewer document group scene. You supply the file type of the document, and a view that displays the document type that you provide:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(viewing: MyImageFormatDocument.self) {
            MyImageFormatViewer(image: $0.document)
        }
    }
}
```

##### Supporting Multiple Document Types

Your app can support multiple document types by adding additional document group scenes:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextFile()) { group in
            ContentView(document: group.$document)
        }
        DocumentGroup(viewing: MyImageFormatDocument.self) { group in
            MyImageFormatViewer(image: group.document)
        }
    }
}
```

##### Opening Documents

When a person opens a file — for example, by double-clicking it in macOS Finder or tapping it in the iOS Files app — the system looks through the list of registered Uniform Type Identifiers (or *content types*) to find one that corresponds to the file extension.

The operating system learns about new content types from information property list files of installed apps. Your app’s information property list can include several keys depending on your needs:

- The *Document Types* key (`CFBundleDocumentTypes`) lists the content type identifiers your app can open. Every document-based app must include this key.
- The *Exported Type Identifiers* key (`UTExportedTypeDeclarations`) declares a custom content type that your app defines. Include a file extension so the system knows which files correspond to that type.
- The *Imported Type Identifiers* key (`UTImportedTypeDeclarations`) registers a content type that another app defines. If the person doesn’t have that app installed, your declaration is what the system uses to identify the type and its associated files. If they do have it installed, the app’s exported declaration takes precedence instead. For example, if your app works with `xcresult` bundles, declare `com.apple.xcode.resultbundle` as an imported type. If someone doesn’t have Xcode installed, your declaration tells the system that `.xcresult` files belong to this type. Once they install Xcode, its exported declaration takes over. You don’t need to declare content types the operating system defines, like `UTType.utf8PlainText`.

You can configure these property list keys in the Info pane of your app target in Xcode. Document types that correspond to regular files on disk must conform to `UTType/data`; packages must conform to `UTType/package`.

For more information on how the `UTType` system works, including its hierarchical structure and when to export versus import a type, refer to [`A Reintroduction to Uniform Type Identifiers`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/10696/).

When multiple apps can open the same file type, the system also considers the *Handler Rank* you set in the Document Types key, which indicates whether your app is the default handler or an alternative.

For example, to declare a custom plain-text format, extend `UTType` with your app’s reverse-DNS identifier and declare its conformance and associated file extension in your app’s information property list:

```swift
extension UTType {
    static let customTextFormat = UTType(
        exportedAs: "com.myApp.customTextFormat")
}

struct MyDocument: FileDocument {
    static let readableContentTypes = [UTType.customTextFormat]
    // ...
}
```

SwiftUI then checks each `DocumentGroup` in your scene body from top to bottom and uses the first one whose document’s `readableContentTypes` static array property includes a `UTType` the file conforms to. Content types form a hierarchy — for example, HTML is a kind of plain text, so a document group that declares `UTType/plainText` also matches HTML files.

If multiple document groups can match the same file, SwiftUI uses the first one declared. Declare more specific types before broader ones to match each file to the correct document group:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        // Checked first; matches only this custom format.
        DocumentGroup(newDocument: MyDocument()) { configuration in
            MyDocumentView(document: configuration.$document)
        }
        // Checked second; matches any remaining plain-text files.
        DocumentGroup(newDocument: TextFile()) { configuration in
            ContentView(document: configuration.$document)
        }
    }
}
```

##### Document Life Cycle

Once SwiftUI selects the matching `DocumentGroup`, it loads the file’s contents into the document type and presents the view with the loaded document.

For a value-type document, like a `struct`, SwiftUI tracks edits through the document binding. For a reference-type document, like a `class`, it tracks changes you register with `EnvironmentValues.undoManager`. SwiftUI writes the document back to disk when needed — for example, in response to a Save command.

##### Accessing the Documents Url

If your app needs to know the document’s URL, you can read it from the `editor` closure’s `configuration` parameter, along with the binding to the document. When you create a new document, the configuration’s `fileURL` property is `nil`. Every time it changes, it is passed over to the `DocumentGroup` builder in the updated `configuration`. This ensures that the view you define in the closure always knows the URL of the document it hosts.

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextFile()) { configuration in
            ContentView(
                document: configuration.$document,
                fileURL: configuration.fileURL
            )
        }
    }
}
```

The URL can be used, for example, to present the file path of the file name in the user interface. Don’t access the document’s contents or metadata using the URL because that can conflict with the management of the file that SwiftUI performs. Instead, use the methods that [`FileDocument`](filedocument.md) and [`ReferenceFileDocument`](referencefiledocument.md) provide to perform read and write operations.

## Topics

### Creating a document group
- [init(allowCreating:editor:makeDocument:)](documentgroup/init(allowcreating:editor:makedocument:).md)
  Creates a document group capable of creating, viewing, and editing documents.
- [init(newDocument:editor:)](documentgroup/init(newdocument:editor:).md)
  Creates a document group for creating and editing file documents.
- [init(viewing:viewer:)](documentgroup/init(viewing:viewer:).md)
  Creates a document group capable of viewing file documents.
- [init(viewer: (Document) -> Content, makeReadableDocument: (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)](documentgroup/init(viewer:makereadabledocument:).md)
  Creates a document group capable of opening and viewing read-only documents.
### Editing a document backed by a persistent store
- [init(editing:contentType:editor:prepareDocument:)](documentgroup/init(editing:contenttype:editor:preparedocument:).md)
  Instantiates a document group for creating and editing documents that store a specific model type.
- [init(editing: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: () -> Content, prepareDocument: (ModelContext) -> Void)](documentgroup/init(editing:migrationplan:editor:preparedocument:).md)
  Instantiates a document group for creating and editing documents described by the last `Schema` in the migration plan.
### Viewing a document backed by a persistent store
- [init(viewing:contentType:viewer:)](documentgroup/init(viewing:contenttype:viewer:).md)
  Instantiates a document group for viewing documents that store a specific model type.
- [init(viewing: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: () -> Content)](documentgroup/init(viewing:migrationplan:viewer:).md)
  Instantiates a document group for viewing documents described by the last `Schema` in the migration plan.

## Relationships

### Conforms To
- [Scene](scene.md)

## See Also

- [Building a document-based app with SwiftUI](building-a-document-based-app-with-swiftui.md)
  Create, save, and open documents in a multiplatform app.
- [Building a document-based app using SwiftData](building-a-document-based-app-using-swiftdata.md)
  Code along with the WWDC presenter to transform an app with SwiftData.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup)*