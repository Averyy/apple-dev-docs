# NewDocumentButton

**Framework**: SwiftUI  
**Kind**: struct

A button that creates and opens new documents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct NewDocumentButton<Label> where Label : View
```

#### Overview

Use a new document button to give people the option to create documents in your app. In the following example, there are two new document buttons, both support [`Text`](text.md) labels. When the user taps or clicks the first button, the system creates a new document in the directory currently open in the document browser. The second button presents a template picker, where a document can be prepopulated or preconfigured using a template.

```swift
@State private var isTemplatePickerPresented = false
@State private var documentCreationContinuation:
    CheckedContinuation<TextDocument?, any Error>?

var body: some Scene {
    DocumentGroupLaunchScene("My Documents") {
        NewDocumentButton(Text("Start Writing…"))
        NewDocumentButton(Text("Choose a Template"), for: TextDocument.self) {
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

If you don’t provide a custom label, the system provides a button with the default “Create Document” label.

## Topics

### Initializers
- [init(_:contentType:)](newdocumentbutton/init(_:contenttype:).md)
  Creates and opens new documents.
- [init(_:contentType:prepareDocumentURL:)](newdocumentbutton/init(_:contenttype:preparedocumenturl:).md)
  Creates and opens new documents.
- [init(_:for:contentType:prepareDocument:)](newdocumentbutton/init(_:for:contenttype:preparedocument:).md)
  Creates and opens new documents.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct DocumentGroupLaunchScene](documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [struct DocumentLaunchView](documentlaunchview.md)
  A view to present when launching document-related user experience.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton)*