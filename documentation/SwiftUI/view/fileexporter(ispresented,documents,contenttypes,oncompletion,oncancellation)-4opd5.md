# fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a system dialog for allowing the user to export a collection of documents that conform to `ReferenceFileDocument` to files on disk.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.2
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Conform your document type to WritableDocument or Transferable protocol instead.

## Declaration

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType] = [], onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where C : Collection, C.Element : ReferenceFileDocument
```

**Other overloads**:

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType] = [], onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: (() -> Void)? = nil) -> some View where C : Collection, C.Element : WritableDocument, C.Element.Writer.Destination == URL
```

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType] = [], onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where C : Collection, C.Element : FileDocument
```

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

To further configure the dialog’s appearance and behavior, use these view modifiers: [`fileDialogDefaultDirectory(_:)`](./filedialogdefaultdirectory%28_%29.md), [`fileDialogConfirmationLabel(_:)`](./filedialogconfirmationlabel%28_%29.md), [`fileDialogMessage(_:)`](./filedialogmessage%28_%29.md), [`fileDialogBrowserOptions(_:)`](./filedialogbrowseroptions%28_%29.md), [`fileExporterFilenameLabel(_:)`](./fileexporterfilenamelabel%28_%29.md), and [`fileDialogCustomizationID(_:)`](./filedialogcustomizationid%28_%29.md).

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `documents`: The in-memory documents to export.
- `contentTypes`: The list of supported content types which can be exported. If not provided, `ReferenceFileDocument.writableContentTypes` are used.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed.
- `onCancellation`: A callback that will be invoked if the user cancels the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-4opd5)*