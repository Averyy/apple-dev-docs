# fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

**Framework**: FamilyControls  
**Kind**: method

Presents a system interface for allowing the user to export a `FileDocument` to a file on disk.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType] = [], defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where D : FileDocument
```

#### Discussion

In order for the interface to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

## Parameters

- `isPresented`: A binding to whether the interface should be shown.
- `document`: The in-memory document to export.
- `contentTypes`: The list of supported content types which can   be exported. If not provided,    are used.
- `defaultFilename`: If provided, the default name to use   for the exported file, which will the user will have   an opportunity to edit prior to the export.
- `onCompletion`: A callback that will be invoked when the operation has   succeeded or failed. The   indicates whether   the operation succeeded or failed.
- `onCancellation`: A callback that will be invoked   if the user cancels the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-6otwm)*