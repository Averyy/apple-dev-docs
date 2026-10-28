# fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType] = [], onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: (() -> Void)? = nil) -> some View where C : Collection, C.Element : WritableDocument, C.Element.Writer.Destination == URL
```

**Other overloads**:

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType] = [], onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where C : Collection, C.Element : FileDocument
```

```swift
nonisolated
func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType] = [], onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where C : Collection, C.Element : ReferenceFileDocument
```

## Discussion

In order for the dialog to appear, `documents` must be non-empty. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

```swift
@MainActor
final class TextDocument: WritableDocument {
    static let writableContentTypes: [UTType] = [.utf8PlainText]

    var text: String = ""

    nonisolated func writer(
        configuration: sending WriteConfiguration
    ) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(regularFileWithContents: Data(snapshot.utf8))
        }
    }

    func snapshot(contentType: UTType) async throws -> String {
        text
    }
}

struct ExportView: View {
    @Binding var documents: [TextDocument]
    @State private var isExporting = false

    var body: some View {
        Button("Export…") { isExporting = true }
            .fileExporter(
                isPresented: $isExporting,
                documents: documents
            ) { _ in }
    }
}
```

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `documents`: The in-memory documents to export.
- `contentTypes`: The content types to export to. If not provided, `WritableDocument.writableContentTypes` are used.
- `onCompletion`: A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed.
- `onCancellation`: A callback that will be invoked if the user cancels the operation.

## See Also

### Exporting to file
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType?, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: (() -> Void)?) -> some View](./fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](./fileexporter%28ispresented,item,contenttypes,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](./fileexporter%28ispresented,items,contenttypes,oncompletion,oncancellation%29.md)
  Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.
- [func fileExporterFilenameLabel(_:)](./fileexporterfilenamelabel%28_%29.md)
  On macOS, configures the `fileExporter` with a label for the file name field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:))*