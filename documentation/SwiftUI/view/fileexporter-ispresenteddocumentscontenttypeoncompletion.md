# fileExporter(isPresented:documents:contentType:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a system interface for exporting a collection of value type documents to files on disk.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element : FileDocument
```

#### Discussion

In order for the interface to appear, both `isPresented` must be `true` and `documents` must not be empty. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

The `contentType` provided must be included within the document type’s `writableContentTypes`, otherwise the first valid writable content type will be used instead.

## Parameters

- `isPresented`: A binding to whether the interface should be shown.
- `documents`: The collection of in-memory documents to export.
- `contentType`: The content type to use for the exported file.
- `onCompletion`: A callback that will be invoked when the operation has   has succeeded or failed.

## See Also

- [func fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:).md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](view/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface for allowing the user to export a `FileDocument` to a file on disk.
- [func fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](view/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `FileDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](view/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a `Transferable` item to file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](view/fileexporter(ispresented:items:contenttypes:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a collection of items to files on disk.
- [func fileExporterFilenameLabel(_:)](view/fileexporterfilenamelabel(_:).md)
  On macOS, configures the `fileExporter` with a text to use as a label for the file name field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:documents:contenttype:oncompletion:))*