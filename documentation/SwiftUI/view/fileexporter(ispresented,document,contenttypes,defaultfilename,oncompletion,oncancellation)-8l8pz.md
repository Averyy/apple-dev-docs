# fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a system dialog for allowing the user to export a `ReferenceFileDocument` to a file on disk.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.2
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)`](./fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion,oncancellation%29.md) instead.

## Declaration

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType] = [], defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where D : ReferenceFileDocument
```

**Other overloads**:

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType] = [], defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where D : FileDocument
```

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

To further configure the dialog’s appearance and behavior, use these view modifiers: [`fileDialogDefaultDirectory(_:)`](./filedialogdefaultdirectory%28_%29.md), [`fileDialogConfirmationLabel(_:)`](./filedialogconfirmationlabel%28_%29.md), [`fileDialogMessage(_:)`](./filedialogmessage%28_%29.md), [`fileDialogBrowserOptions(_:)`](./filedialogbrowseroptions%28_%29.md), [`fileExporterFilenameLabel(_:)`](./fileexporterfilenamelabel%28_%29.md), and [`fileDialogCustomizationID(_:)`](./filedialogcustomizationid%28_%29.md).

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `document`: The in-memory document to export.
- `contentTypes`: The list of supported content types which can be exported. If not provided, `ReferenceFileDocument.writableContentTypes` are used.
- `defaultFilename`: If provided, the default name to use for the exported file, which will the user will have an opportunity to edit prior to the export.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed.
- `onCancellation`: A callback that will be invoked if the user cancels the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-8l8pz)*