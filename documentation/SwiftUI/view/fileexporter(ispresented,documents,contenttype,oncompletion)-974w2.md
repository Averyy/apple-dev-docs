# fileExporter(isPresented:documents:contentType:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a system dialog for exporting a collection of reference type documents to files on disk.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)`](./fileexporter%28ispresented,documents,contenttypes,oncompletion,oncancellation%29.md) instead.

## Declaration

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element : ReferenceFileDocument
```

**Other overloads**:

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element : FileDocument
```

## Discussion

In order for the dialog to appear, both `isPresented` must be `true` and `documents` must not be empty. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

The `contentType` provided must be included within the document type’s `writableContentTypes`, otherwise the first valid writable content type will be used instead.

To further configure the dialog’s appearance and behavior, use these view modifiers: [`fileDialogDefaultDirectory(_:)`](./filedialogdefaultdirectory%28_%29.md), [`fileDialogConfirmationLabel(_:)`](./filedialogconfirmationlabel%28_%29.md), [`fileDialogMessage(_:)`](./filedialogmessage%28_%29.md), [`fileDialogBrowserOptions(_:)`](./filedialogbrowseroptions%28_%29.md), [`fileExporterFilenameLabel(_:)`](./fileexporterfilenamelabel%28_%29.md), and [`fileDialogCustomizationID(_:)`](./filedialogcustomizationid%28_%29.md).

This overload works the same way as the batch [`FileDocument`](../filedocument.md) overload, but accepts a collection of [`ReferenceFileDocument`](../referencefiledocument.md) values instead.

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `documents`: The collection of in-memory documents to export.
- `contentType`: The content type to use for the exported file.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed.

  - **result**: A `Result` indicating whether the operation succeeded or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:documents:contenttype:oncompletion:)-974w2)*