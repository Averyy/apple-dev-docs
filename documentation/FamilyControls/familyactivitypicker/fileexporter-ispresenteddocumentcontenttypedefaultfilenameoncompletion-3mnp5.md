# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

**Framework**: FamilyControls  
**Kind**: method

Presents a system interface for exporting a document that’s stored in a reference type, like a class, to a file on disk.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View where D : ReferenceFileDocument
```

#### Discussion

In order for the interface to appear, both `isPresented` must be `true` and `document` must not be `nil`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

The `contentType` provided must be included within the document type’s `writableContentTypes`, otherwise the first valid writable content type will be used instead.

## Parameters

- `isPresented`: A binding to whether the interface should be shown.
- `document`: The in-memory document to export.
- `contentType`: The content type to use for the exported file.
- `defaultFilename`: If provided, the default name to use for the   exported file, which will the user will have an opportunity to edit   prior to the export.
- `onCompletion`: A callback that will be invoked when the operation has   has succeeded or failed.
- `result`: A   indicating whether the operation succeeded or   failed.

## See Also

- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-3cork.md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:documents:contenttype:oncompletion:)-2szoo.md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:documents:contenttype:oncompletion:)-9hq0d.md)
  Presents a system interface for exporting a collection of reference type documents to files on disk.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-3mnp5)*