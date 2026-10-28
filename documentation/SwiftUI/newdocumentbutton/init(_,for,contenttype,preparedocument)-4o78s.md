# init(_:for:contentType:prepareDocument:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates and opens new documents.

**Availability**:
- iOS 18.0+ - Deprecated in 27.2
- iPadOS 18.0+ - Deprecated in 27.2
- Mac Catalyst 18.0+ - Deprecated in 27.2
- macOS 15.0+ - Deprecated in 27.2
- visionOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Conform your document type to ReadableDocument instead.

## Declaration

```swift
nonisolated
init<D>(_ title: some StringProtocol, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<D>(_ title: LocalizedStringResource, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

```swift
@export(implementation)
nonisolated init<D>(_ title: LocalizedStringResource, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : ReferenceFileDocument
```

```swift
nonisolated
init<D>(_ label: Text? = nil, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

```swift
nonisolated
init<D>(_ label: Text? = nil, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : ReferenceFileDocument
```

```swift
nonisolated
init<D>(_ title: LocalizedStringKey, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

```swift
nonisolated
init<D>(_ title: LocalizedStringKey, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : ReferenceFileDocument
```

```swift
nonisolated
init<D>(_ title: some StringProtocol, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : ReferenceFileDocument
```

## Discussion

This initializer allows presenting a template picker, where a document can be prepopulated or preconfigured using a template.

```swift
@State private var isTemplatePickerPresented = false
@State private var documentCreationContinuation:
    CheckedContinuation<TextDocument?, any Error>?

var body: some Scene {
    DocumentGroupLaunchScene("My Documents") {
        NewDocumentButton("Start Writing…")
        NewDocumentButton("Choose a Template", for: TextDocument.self) {
            try await withCheckedThrowingContinuation { continuation in
                documentCreationContinuation = continuation
                isTemplatePickerPresented = true
            }
        }
        .fullScreenCover(isPresented: $isTemplatePickerPresented) {
            TemplatePicker(
                continuation: $documentCreationContinuation
            )
        }
    }

    DocumentGroup(newDocument: TextDocument()) { configuration in
        MyDocumentView(document: configuration.$document))
    }
}

struct TemplatePicker: View {
    @Binding var continuation:
        CheckedContinuation<TextDocument?, any Error>?
    @Environment(\.dismiss) var dismiss

    var body: some View {
        VStack {
            Text("Choose a template")
                .font(.title)
            Button("Meeting minutes") {
                let document = makeMeetingMinutes()
                documentCreationContinuation?.resume(returning: document)
                dismiss()
            }
            Button("Letter") {
                let document = makeLetter()
                documentCreationContinuation?.resume(returning: document)
                dismiss()
            }
            Button("Cancel") {
                documentCreationContinuation?.resume(throwing: CancellationError())
                dismiss()
            }
        }
    }

    private func makeMeetingMinutes() -> TextDocument { ... }
    private func makeLetter() -> TextDocument { ... }
}

struct TextDocument: FileDocument { ... }
```

## Parameters

- `title`: A title for the button title.
- `documentType`: A type of the document to create.
- `contentType`: An optional content type of the document to create.
- `prepareDocument`: A closure is called when a user presses the button. At this point, you can present a document template picker or another UI that allows users to choose a theme, configuration, or a template to create a document from. Return a prepared document, or throw an error if document creation failed. Return `nil` to request creation of an empty document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:for:contenttype:preparedocument:)-4o78s)*