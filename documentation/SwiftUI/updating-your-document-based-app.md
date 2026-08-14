# Updating your document-based app

**Framework**: SwiftUI

Migrate an existing app to adopt URL-based document reading and writing with Swift concurrency.

#### Overview

If you have an existing document-based app, you can adopt the [`Document`](document.md) protocol to take advantage of direct URL access, Swift concurrency integration, and modern observation. The [`Document`](document.md) protocol separates reading and writing into dedicated types, which gives you more control over file I/O and enables partial reads and writes for complex document formats.

In releases before iOS 27, iPadOS 27, macOS 27, and visionOS 27, you create a document type by conforming to either `FileDocument` or `ReferenceFileDocument`. In these and later releases, you can either conform to the `Document` protocol or to the `ReadableDocument` and `WritableDocument` protocols, depending on what your app does. Although `FileDocument` and `ReferenceFileDocument` remain available, they’re no longer supported for new document types.

The following table highlights the differences between these three protocols to help you choose the right migration path:

|  | [`FileDocument`](filedocument.md) | [`ReferenceFileDocument`](referencefiledocument.md) | [`Document`](document.md) |
| --- | --- | --- | --- |
| Type | Value (`struct`) | Reference (`class`) | Reference (`class`) |
| Reading | [`init(configuration:)`](filedocument/init(configuration:).md) | [`init(configuration:)`](referencefiledocument/init(configuration:).md) | [`reader(configuration:)`](readabledocument/reader(configuration:).md) + [`apply(snapshot:previous:)`](readabledocument/apply(snapshot:previous:).md) |
| Writing | [`fileWrapper(configuration:)`](filedocument/filewrapper(configuration:).md) | [`fileWrapper(snapshot:configuration:)`](referencefiledocument/filewrapper(snapshot:configuration:).md) | [`writer(configuration:)`](writabledocument/writer(configuration:).md) + [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md) |
| Reading and writing execution | Synchronous | Synchronous | `async`/`sending` with explicit actor boundaries |
| File access | [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper) only | [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper) only | URL or [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper) |
| Undo | Automatic (value semantics) | Manual ([`UndoManager`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/undomanager)) | Manual ([`UndoManager`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/undomanager)) |
| Observation | N/A (value type) | [`ObservableObject`](https://developer.apple.comhttps://developer.apple.com/documentation/combine/observableobject) | [`@Observable`](https://developer.apple.comhttps://developer.apple.com/documentation/observation/observable) |

#### Update Your App

Depending on which deprecated protocol your app uses, select the appropriate tab and follow the checklist to update your app:

**FileDocument**:

1. **Convert from a structure to an [`@Observable`](https://developer.apple.comhttps://developer.apple.com/documentation/observation/observable) class.** A document type that conforms to [`FileDocument`](filedocument.md) is typically a value type. The [`Document`](document.md) protocol requires a reference type. Replace your structure with a `final class` annotated with [`@Observable`](https://developer.apple.comhttps://developer.apple.com/documentation/observation/observable).
2. **Separate reading logic into a [`DocumentReader`](documentreader.md).** For reading, use [`FileWrapperDocumentReader`](filewrapperdocumentreader.md) and provide a closure that converts a [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper) into a snapshot value.
3. **Implement [`apply(snapshot:previous:)`](readabledocument/apply(snapshot:previous:).md).** Use this method to update your document’s properties when a new snapshot arrives from the reader.
4. **Separate writing logic into a [`DocumentWriter`](documentwriter.md).** For writing, use [`FileWrapperDocumentWriter`](filewrapperdocumentwriter.md) and provide a closure that converts a snapshot into a [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper).
5. **Implement [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md).** Add this method to capture your document’s current state on the main actor. Mark it `async throws` and return a `sending` value.
6. **Add undo registration.** With [`FileDocument`](filedocument.md), SwiftUI manages undo automatically through value semantics and [`Binding`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/binding). With the [`Document`](document.md) protocol, you register undo actions yourself using an [`UndoManager`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/undomanager). The undo manager from the environment in your content view is already connected to the document.
7. **Update your [`DocumentGroup`](documentgroup.md) initializer.** Replace `DocumentGroup(newDocument:)` with the closure-based initializer that receives [`URLDocumentConfiguration`](urldocumentconfiguration.md) and [`DocumentCreationContext`](documentcreationcontext.md).
8. **Update your content view.** Replace `@Binding var document: MyDocument` with a direct reference to your observable class, and use [`@Bindable`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/bindable) for creating bindings.

**ReferenceFileDocument**:

1. **Mark your document [`@Observable`](https://developer.apple.comhttps://developer.apple.com/documentation/observation/observable).** The [`ReferenceFileDocument`](referencefiledocument.md) protocol predates the Observation framework. Add the [`@Observable`](https://developer.apple.comhttps://developer.apple.com/documentation/observation/observable) macro and remove any [`ObservableObject`](https://developer.apple.comhttps://developer.apple.com/documentation/combine/observableobject) conformance and [`@Published`](https://developer.apple.comhttps://developer.apple.com/documentation/combine/published) property wrappers.
2. **Separate reading logic into a [`DocumentReader`](documentreader.md).** For reading, use [`FileWrapperDocumentReader`](filewrapperdocumentreader.md) and provide a closure that converts a [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper) into a snapshot value.
3. **Implement [`apply(snapshot:previous:)`](readabledocument/apply(snapshot:previous:).md).** Use this method to update your document’s properties when a new snapshot arrives from the reader.
4. **Separate writing logic into a [`DocumentWriter`](documentwriter.md).** For writing, use [`FileWrapperDocumentWriter`](filewrapperdocumentwriter.md) and provide a closure that converts a snapshot into a [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper).
5. **Implement [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md).** Update the method to add `async throws` and `sending` to the return type to enable safe transfer across concurrency boundaries.
6. **Update your [`DocumentGroup`](documentgroup.md) initializer.** Replace the type-based initializer with the closure-based one that receives [`URLDocumentConfiguration`](urldocumentconfiguration.md) and [`DocumentCreationContext`](documentcreationcontext.md).
7. **Audit undo registration.** Undo registration is conceptually the same, but verify that your undo actions work correctly after the changes.

If your existing document-based app uses [`FileDocument`](filedocument.md) or [`ReferenceFileDocument`](referencefiledocument.md), the following table shows how concepts map to the [`Document`](document.md) protocol:

**FileDocument**:

| Before | After |
| --- | --- |
| [`FileDocument`](filedocument.md) | [`Document`](document.md) |
| `struct` (value type) | [`@Observable`](https://developer.apple.comhttps://developer.apple.com/documentation/observation/observable) `final class` (reference type) |
| [`init(configuration:)`](filedocument/init(configuration:).md) | Separate [`DocumentReader`](documentreader.md) |
| [`fileWrapper(configuration:)`](filedocument/filewrapper(configuration:).md) | Separate [`DocumentWriter`](documentwriter.md) |
| Implicit snapshot (value semantics) | Explicit [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md) method |
| Automatic undo via [`Binding`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/binding) | Manual undo registration with [`UndoManager`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/undomanager) |
| `DocumentGroup(newDocument:)` | [`DocumentGroup`](documentgroup.md) initializer |

**ReferenceFileDocument**:

| Before | After |
| --- | --- |
| [`ReferenceFileDocument`](referencefiledocument.md) | [`Document`](document.md) |
| [`init(configuration:)`](referencefiledocument/init(configuration:).md) | Separate [`DocumentReader`](documentreader.md) |
| [`fileWrapper(snapshot:configuration:)`](referencefiledocument/filewrapper(snapshot:configuration:).md) | Separate [`DocumentWriter`](documentwriter.md) |
| [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper) only | [`FileWrapper`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/filewrapper) and URL access through [`DocumentReader`](documentreader.md) and [`DocumentWriter`](documentwriter.md) |
| Single `Snapshot` type on [`ReferenceFileDocument`](referencefiledocument.md) | Separate `Snapshot` types on [`DocumentWriter`](documentwriter.md) and [`DocumentReader`](documentreader.md) |

The following example shows a complete text document before and after migrating from [`FileDocument`](filedocument.md):

**Before**:

```swift
struct TextDocument: FileDocument {
    static let readableContentTypes: [UTType] = [.plainText]

    var text: String

    init(configuration: ReadConfiguration) throws {
        guard let data = configuration.file.regularFileContents,
              let string = String(data: data, encoding: .utf8)
        else {
            throw CocoaError(.fileReadCorruptFile)
        }
        text = string
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        let data = Data(text.utf8)
        return FileWrapper(regularFileWithContents: data)
    }
}

struct TextDocumentApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextDocument()) { file in
            TextEditor(text: file.$document.text)
        }
    }
}
```

**After**:

```swift
@Observable
final class TextDocument: Document {
    static let readableContentTypes: [UTType] = [.plainText]

    var text: String

    init(text: String = "") {
        self.text = text
    }

    func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
        FileWrapperDocumentReader(configuration) { fileWrapper in
            guard let data = fileWrapper.regularFileContents else {
                throw CocoaError(.fileReadCorruptFile)
            }
            return String(decoding: data, as: UTF8.self)
        }
    }

    func writer(configuration: sending WriteConfiguration) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot in
            FileWrapper(
                regularFileWithContents: Data(snapshot.utf8)
            )
        }
    }

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending String {
        text
    }

    @MainActor
    func apply(snapshot: sending String, previous: sending String?) async throws {
        text = snapshot
    }
}

struct TextDocumentApp: App {
    var body: some Scene {
        DocumentGroup { document in
            TextDocumentView(document: document)
        } makeDocument: { _, _ in
            TextDocument()
        }
    }
}

struct TextDocumentView: View {
    @Bindable var document: TextDocument
    @Environment(\.undoManager) private var undoManager

    var body: some View {
        TextEditor(text: $document.text)
            .onChange(of: document.text) { oldValue, _ in
                undoManager?.registerUndo(
                    withTarget: document
                ) { document in
                    document.text = oldValue
                }
            }
    }
}
```

The key structural change is the shift from value to reference semantics. With [`FileDocument`](filedocument.md), SwiftUI tracks mutations through the [`Binding`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/binding) to the structure and manages undo automatically. With [`Document`](document.md), you use [`@Observable`](https://developer.apple.comhttps://developer.apple.com/documentation/observation/observable) for change tracking and register undo actions explicitly — but gain async I/O, URL-based file access, and clear separation between state capture and serialization.

The following example shows a complete text document before and after migrating from [`ReferenceFileDocument`](referencefiledocument.md):

**Before**:

```swift
final class OldTextDocument: ReferenceFileDocument {
    typealias Snapshot = String

    static let readableContentTypes = [UTType.utf8PlainText]

    @Published var text: String

    init() {
        text = ""
    }

    required init(configuration: ReadConfiguration) throws {
        if let data = configuration.file.regularFileContents {
            text = String(data: data, encoding: .utf8) ?? ""
        } else {
            text = ""
        }
    }

    func snapshot(contentType: UTType) throws -> String {
        text
    }

    func fileWrapper(
        snapshot: String, configuration: WriteConfiguration
    ) throws -> FileWrapper {
        let data = snapshot.data(using: .utf8) ?? Data()
        return FileWrapper(regularFileWithContents: data)
    }
}
```

**After**:

```swift
@Observable
final class TextDocument: Document {
    static let readableContentTypes = [UTType.utf8PlainText]

    var text: String

    init() {
        text = ""
    }

    func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
        FileWrapperDocumentReader(configuration) { fileWrapper in
            if let data = fileWrapper.regularFileContents,
               let text = String(data: data, encoding: .utf8) {
                return text
            }
            return ""
        }
    }

    @MainActor
    func apply(snapshot: sending String, previous: sending String?) async throws {
        text = snapshot
    }

    func writer(configuration: sending WriteConfiguration) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, previous in
            let data = snapshot.data(using: .utf8) ?? Data()
            return FileWrapper(regularFileWithContents: data)
        }
    }

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending String {
        text
    }
}

struct TextDocumentView: View {
    @Bindable var document: TextDocument
    @Environment(\.undoManager) private var undoManager

    var body: some View {
        TextEditor(text: $document.text)
            .onChange(of: document.text) { oldValue, _ in
                undoManager?.registerUndo(
                    withTarget: document
                ) { document in
                    document.text = oldValue
                }
            }
    }
}
```

The migrated document cleanly separates concerns, supports URL access for advanced use cases, adopts the Observation framework, and integrates Swift concurrency.

## See Also

- [Creating a document-based app](creating-a-document-based-app.md)
  Build apps that people can use to open, edit, and save files using coordinated file access.
- [Handling advanced document scenarios](handling-advanced-document-scenarios.md)
  Extend your document-based app to support custom file formats, on-demand file access, and progress reporting.
- [Building a document-based app with SwiftUI](building-a-document-based-app-with-swiftui.md)
  Create, save, and open documents in a multiplatform app.
- [Building a document-based app using SwiftData](building-a-document-based-app-using-swiftdata.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [struct DocumentGroup](documentgroup.md)
  A scene that enables support for opening, creating, and saving documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/updating-your-document-based-app)*