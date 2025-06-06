# init(newDocument:editor:)

**Framework**: SwiftUI  
**Kind**: init

Creates a document group for creating and editing file documents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@preconcurrency
nonisolated init(newDocument: @autoclosure @escaping () -> Document, @ViewBuilder editor: @escaping (FileDocumentConfiguration<Document>) -> Content)
```

#### Discussion

Use a [`DocumentGroup`](documentgroup.md) scene to tell SwiftUI what kinds of documents your app can open when you declare your app using the [`App`](app.md) protocol. You initialize a document group scene by passing in the document model and a view capable of displaying the document’s contents. The document types you supply to [`DocumentGroup`](documentgroup.md) must conform to [`FileDocument`](filedocument.md) or [`ReferenceFileDocument`](referencefiledocument.md). SwiftUI uses the model to add document support to your app. In macOS this includes document-based menu support including the ability to open multiple documents. On iOS this includes a document browser that can navigate to the documents stored on the file system and multiwindow support:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextFile()) { file in
            ContentView(document: file.$document)
        }
    }
}
```

The document types you supply to [`DocumentGroup`](documentgroup.md) must conform to [`FileDocument`](filedocument.md) or [`ReferenceFileDocument`](referencefiledocument.md). Your app can support multiple document types by adding additional [`DocumentGroup`](documentgroup.md) scenes.

## Parameters

- `newDocument`: The initial document to use when a user creates   a new document.
- `editor`: The editing UI for the provided document.

## See Also

- [init(viewing:viewer:)](documentgroup/init(viewing:viewer:).md)
  Creates a document group capable of viewing file documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(newdocument:editor:))*