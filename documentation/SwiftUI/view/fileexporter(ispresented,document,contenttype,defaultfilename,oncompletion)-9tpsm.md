# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a system dialog for exporting a document that’s stored in a reference type, like a class, to a file on disk.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)`](./fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion,oncancellation%29.md) instead.

## Declaration

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View where D : ReferenceFileDocument
```

**Other overloads**:

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View where D : FileDocument
```

## Discussion

In order for the dialog to appear, both `isPresented` must be `true` and `document` must not be `nil`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

The `contentType` provided must be included within the document type’s `writableContentTypes`, otherwise the first valid writable content type will be used instead.

To further configure the dialog’s appearance and behavior, use these view modifiers: [`fileDialogDefaultDirectory(_:)`](./filedialogdefaultdirectory%28_%29.md), [`fileDialogConfirmationLabel(_:)`](./filedialogconfirmationlabel%28_%29.md), [`fileDialogMessage(_:)`](./filedialogmessage%28_%29.md), [`fileDialogBrowserOptions(_:)`](./filedialogbrowseroptions%28_%29.md), [`fileExporterFilenameLabel(_:)`](./fileexporterfilenamelabel%28_%29.md), and [`fileDialogCustomizationID(_:)`](./filedialogcustomizationid%28_%29.md).

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `document`: The in-memory document to export.
- `contentType`: The content type to use for the exported file.
- `defaultFilename`: If provided, the default name to use for the exported file, which the user will have an opportunity to edit prior to the export.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed.

  - **result**: A `Result` indicating whether the operation succeeded or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-9tpsm)*