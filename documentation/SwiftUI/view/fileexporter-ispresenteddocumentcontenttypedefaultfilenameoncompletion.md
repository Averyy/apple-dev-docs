# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View where D : FileDocument
```

#### Discussion

In order for the dialog to appear, both `isPresented` must be `true` and `document` must not be `nil`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

The `contentType` provided must be included within the document type’s `writableContentTypes`, otherwise the first valid writable content type will be used instead.

For example, a button that exports a text document might look like this:

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
            contentType: .utf8PlainText,
            defaultFilename: "Exported Document"
        ) { result in
            switch result {
            case .success(let url):
                print("Saved to \(url)")
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
- `document`: The in-memory document to export.
- `contentType`: The content type to use for the exported file.
- `defaultFilename`: If provided, the default name to use for the exported file, which the user will have an opportunity to edit prior to the export.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed. - **result**: A `Result` indicating whether the operation succeeded or failed.

## See Also

- [func fileExporter(isPresented:documents:contentType:onCompletion:)](view/fileexporter(ispresented:documents:contenttype:oncompletion:).md)
  Presents a system dialog for exporting a collection of value type documents to files on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType?, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: (() -> Void)?) -> some View](view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk.
- [func fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](view/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk.
- [func fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](view/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `FileDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](view/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](view/fileexporter(ispresented:items:contenttypes:oncompletion:oncancellation:).md)
  Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.
- [func fileExporterFilenameLabel(_:)](view/fileexporterfilenamelabel(_:).md)
  On macOS, configures the `fileExporter` with a label for the file name field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:))*