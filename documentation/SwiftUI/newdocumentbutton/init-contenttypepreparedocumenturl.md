# init(_:contentType:prepareDocumentURL:)

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
init(_ label: Text? = nil, contentType: UTType, prepareDocumentURL: @escaping () async throws -> URL? = { nil })
```

#### Discussion

A button that presents a document template picker and creates documents can be implemented like this:

```swift
   struct ChooseDocumentTemplateButton: View {
       @State private var showTemplatePicker = false
       @State private var documentCreationContinuation:
           CheckedContinuation<URL?, any Error>?

       var body: some View {
           NewDocumentButton(contentType: .text) {
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
           CheckedContinuation<URL?, any Error>?

       ...

       func present(document: URL) {
           documentCreationContinuation.resume(returning: document)
           documentCreationContinuation = nil
       }
   }
```

## Parameters

- `label`: A label for the button.
- `contentType`: A content type of the document to create.
- `prepareDocumentURL`: A closure that is called when a user presses the button.   At this point, you can present a document template picker or another UI that allows   users to choose a theme, configuration, or a template   to create a document from.   Return a prepared document, or throw an error if document creation failed.   Return   to request creation of an empty document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(_:contenttype:preparedocumenturl:))*