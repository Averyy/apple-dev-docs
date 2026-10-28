# fileExporter(isPresented:documents:contentType:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a system dialog for exporting a collection of value type documents to files on disk.

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
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element : FileDocument
```

**Other overloads**:

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element : ReferenceFileDocument
```

## Discussion

In order for the dialog to appear, both `isPresented` must be `true` and `documents` must not be empty. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

The `contentType` provided must be included within the document type’s `writableContentTypes`, otherwise the first valid writable content type will be used instead.

For example, a button that exports a collection of text documents might look like this:

```swift
struct ExportAllButton: View {
    @State private var isExporterPresented = false
    var documents: [TextFile]

    var body: some View {
        Button("Export All") {
            isExporterPresented = true
        }
        .fileExporter(
            isPresented: $isExporterPresented,
            documents: documents,
            contentType: .utf8PlainText
        ) { result in
            switch result {
            case .success(let urls):
                urls.forEach { print("Saved to \($0)") }
            case .failure(let error):
                print(error)
            }
        }
    }
}
```

To further configure the dialog’s appearance and behavior, use these view modifiers: [`fileDialogDefaultDirectory(_:)`](./filedialogdefaultdirectory%28_%29.md), [`fileDialogConfirmationLabel(_:)`](./filedialogconfirmationlabel%28_%29.md), [`fileDialogMessage(_:)`](./filedialogmessage%28_%29.md), [`fileDialogBrowserOptions(_:)`](./filedialogbrowseroptions%28_%29.md), [`fileExporterFilenameLabel(_:)`](./fileexporterfilenamelabel%28_%29.md), and [`fileDialogCustomizationID(_:)`](./filedialogcustomizationid%28_%29.md).

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `documents`: The collection of in-memory documents to export.
- `contentType`: The content type to use for the exported file.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed.

  - **result**: A `Result` indicating whether the operation succeeded or failed.

## See Also

### Deprecated
- [struct Alert](../alert.md)
  A representation of an alert presentation.
- [struct ActionSheet](../actionsheet.md)
  A representation of an action sheet presentation.
- [func fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](./fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion%29.md)
  Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](./fileexporter%28ispresented,document,contenttypes,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:documents:contenttype:oncompletion:))*