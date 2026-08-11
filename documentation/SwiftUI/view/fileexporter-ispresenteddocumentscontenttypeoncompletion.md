# fileExporter(isPresented:documents:contentType:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a system dialog for exporting a collection of value type documents to files on disk.

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

To further configure the dialog’s appearance and behavior, use these view modifiers: [`fileDialogDefaultDirectory(_:)`](view/filedialogdefaultdirectory(_:).md), [`fileDialogConfirmationLabel(_:)`](view/filedialogconfirmationlabel(_:).md), [`fileDialogMessage(_:)`](view/filedialogmessage(_:).md), [`fileDialogBrowserOptions(_:)`](view/filedialogbrowseroptions(_:).md), [`fileExporterFilenameLabel(_:)`](view/fileexporterfilenamelabel(_:).md), and [`fileDialogCustomizationID(_:)`](view/filedialogcustomizationid(_:).md).

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `documents`: The collection of in-memory documents to export.
- `contentType`: The content type to use for the exported file.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed. - **result**: A `Result` indicating whether the operation succeeded or failed.

## See Also

- [struct Alert](alert.md)
  A representation of an alert presentation.
- [struct ActionSheet](actionsheet.md)
  A representation of an action sheet presentation.
- [func fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:).md)
  Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](view/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:documents:contenttype:oncompletion:))*