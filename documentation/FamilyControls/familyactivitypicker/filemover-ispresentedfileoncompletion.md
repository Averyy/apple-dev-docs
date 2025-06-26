# fileMover(isPresented:file:onCompletion:)

**Framework**: FamilyControls  
**Kind**: method

Presents a system interface for allowing the user to move an existing file to a new location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View
```

#### Discussion

> **Note**: This interface provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the interface to appear, both `isPresented` must be `true` and `file` must not be `nil`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

## Parameters

- `isPresented`: A binding to whether the interface should be shown.
- `file`: The   of the file to be moved.
- `onCompletion`: A callback that will be invoked when the operation has   has succeeded or failed. To access the received URLs, call  .   When the access is no longer required, call  .
- `result`: A   indicating whether the operation succeeded or   failed.

## See Also

- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-3cork.md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-3mnp5.md)
  Presents a system interface for exporting a document that’s stored in a reference type, like a class, to a file on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:documents:contenttype:oncompletion:)-2szoo.md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:documents:contenttype:oncompletion:)-9hq0d.md)
  Presents a system interface for exporting a collection of reference type documents to files on disk.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/filemover(ispresented:file:oncompletion:))*