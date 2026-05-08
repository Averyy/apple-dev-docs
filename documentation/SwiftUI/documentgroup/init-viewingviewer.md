# init(viewing:viewer:)

**Framework**: SwiftUI  
**Kind**: init

Creates a document group capable of viewing file documents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(viewing documentType: Document.Type, @ViewBuilder viewer: @escaping (FileDocumentConfiguration<Document>) -> Content)
```

#### Discussion

Use this method to create a document group that can view files of a specific type. The example below creates a new document viewer for `MyImageFormatDocument` and displays them with `MyImageFormatViewer`:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup(viewing: MyImageFormatDocument.self) { file in
            MyImageFormatViewer(image: file.document)
        }
    }
}
```

You tell the system about the app’s role with respect to the document type by setting the [`CFBundleTypeRole`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes/CFBundleTypeRole) `Info.plist` key with a value of `Viewer`.

## Parameters

- `documentType`: The type of document your app can view.
- `viewer`: The viewing UI for the provided document.

## See Also

- [init(newDocument:editor:)](documentgroup/init(newdocument:editor:).md)
  Creates a document group for creating and editing file documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:viewer:))*