# init(viewing:viewer:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a document group capable of viewing file documents.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Conform your type to ReadableDocument instead.

## Declaration

```swift
nonisolated
init(viewing documentType: Document.Type, @ContentBuilder viewer: @escaping (FileDocumentConfiguration<Document>) -> Content)
```

Available when `Document` conforms to `FileDocument` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(viewing documentType: Document.Type, @ContentBuilder viewer: @escaping (ReferenceFileDocumentConfiguration<Document>) -> Content)
```

## Discussion

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

With the `viewing:` initializer, SwiftUI considers your app as a viewer for given content types (readable content types declared on the document type). No File > New menu item is added on macOS, no New Document button appears in the iOS document browser, and the [`isEditable`](../filedocumentconfiguration/iseditable.md) property is `false`, preventing accidental writes. Use the [`init(newDocument:editor:)`](./init%28newdocument,editor%29.md) initializer instead if your app needs to create or edit documents.

You tell the system about the app’s role with respect to the document type by setting the [`CFBundleTypeRole`](../../BundleResources/information-property-list/cfbundledocumenttypes/cfbundletyperole.md) `Info.plist` key with a value of `Viewer`.

## Parameters

- `documentType`: The type of document your app can view.
- `viewer`: The viewing UI for the provided document.

## See Also

### Creating a document group
- [init(allowCreating: Bool, editor: (Document) -> Content, makeDocument: (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)](./init%28allowcreating,editor,makedocument%29.md)
  Creates a document group capable of creating, viewing, and editing documents.
- [init(viewer: (Document) -> Content, makeReadableDocument: (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)](./init%28viewer,makereadabledocument%29.md)
  Creates a document group capable of opening and viewing read-only documents.
- [init(newDocument:editor:)](./init%28newdocument,editor%29.md)
  Creates a document group for creating and editing file documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:viewer:))*