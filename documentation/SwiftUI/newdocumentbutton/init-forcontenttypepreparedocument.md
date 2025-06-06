# init(_:for:contentType:prepareDocument:)

**Framework**: SwiftUI  
**Kind**: init

Creates and opens new documents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init<D>(_ label: Text? = nil, for documentType: D.Type = D.self, contentType: UTType? = nil, prepareDocument: @escaping () async throws -> D? = { nil }) where D : FileDocument
```

#### Discussion

A button that presents a document template picker and creates documents can be implemented like this:

```swift
   struct ChooseDocumentTemplateButton: View {
       @State private var showTemplatePicker = false
       @State private var documentCreationContinuation:
           CheckedContinuation<TextDocument?, any Error>?

       var body: some View {
           NewDocumentButton(for: TextDocument.self) {
               try await withCheckedThrowingContinuation { continuation in
                   documentCreationContinuation = continuation
                   showTemplatePicker = true
               }
           }
           .fullScreenCover(isPresented: $showTemplatePicker) {
               TemplatePicker($documentCreationContinuation)
           }
       }
   }

   struct TemplatePicker: View {
       @Binding var documentCreationContinuation:
           CheckedContinuation<TextDocument?, any Error>?

       ...

       func present(document: TextDocument) {
           documentCreationContinuation.resume(returning: document)
           documentCreationContinuation = nil
       }
   }

   struct TextDocument: FileDocument { ... }
```

## Parameters

- `label`: A label for the button.
- `documentType`: A type of the document to create.
- `contentType`: An optional content type of the document to create.
- `prepareDocument`: A closure is called when a user presses the button.   At this point, you can present a document template picker or another UI that allows   users to choose a theme, configuration, or a template   to create a document from.   Return a prepared document, or throw an error if document creation failed.   Return   to request creation of an empty document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:for:contenttype:preparedocument:))*