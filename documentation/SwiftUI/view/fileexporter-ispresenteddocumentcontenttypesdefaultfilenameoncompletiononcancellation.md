# fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

**Framework**: SwiftUI  
**Kind**: method

Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType] = [], defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where D : FileDocument
```

#### Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

For example, a button that exports a document and handles cancellation might look like this:

```swift
struct ExportButton: View {
    @State private var isExporterPresented = false
    var document: TextFile?

    var body: some View {
        Button("Export") {
            isExporterPresented = true
        }
        .fileExporter(
            isPresented: $isExporterPresented,
            document: document,
            contentTypes: [.utf8PlainText],
            defaultFilename: "Exported Document"
        ) { result in
            switch result {
            case .success(let url):
                print("Saved to \(url)")
            case .failure(let error):
                print(error)
            }
        } onCancellation: {
            print("Export cancelled")
        }
    }
}
```

To further configure the dialog’s appearance and behavior, use these view modifiers: [`fileDialogDefaultDirectory(_:)`](view/filedialogdefaultdirectory(_:).md), [`fileDialogConfirmationLabel(_:)`](view/filedialogconfirmationlabel(_:).md), [`fileDialogMessage(_:)`](view/filedialogmessage(_:).md), [`fileDialogBrowserOptions(_:)`](view/filedialogbrowseroptions(_:).md), [`fileExporterFilenameLabel(_:)`](view/fileexporterfilenamelabel(_:).md), and [`fileDialogCustomizationID(_:)`](view/filedialogcustomizationid(_:).md).

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `document`: The in-memory document to export.
- `contentTypes`: The list of supported content types which can be exported. If not provided, `FileDocument.writableContentTypes` are used.
- `defaultFilename`: If provided, the default name to use for the exported file, which the user will have an opportunity to edit prior to the export.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed.
- `onCancellation`: A callback that will be invoked if the user cancels the operation.

## See Also

- [struct Alert](alert.md)
  A representation of an alert presentation.
- [struct ActionSheet](actionsheet.md)
  A representation of an action sheet presentation.
- [func fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:).md)
  Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter(isPresented:documents:contentType:onCompletion:)](view/fileexporter(ispresented:documents:contenttype:oncompletion:).md)
  Presents a system dialog for exporting a collection of value type documents to files on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:))*