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

Use a new document button to give people the option to create documents in your app. In the following example, there are two new document buttons, both support [`Text`](text.md) labels. When the user taps or clicks the first button, the system creates a new document in the directory currently open in the document browser. The second button creates a new document from a template.

```swift
@State private var isTemplatePickerPresented = false
@State private var documentCreationContinuation:
    CheckedContinuation<TextDocument?, any Error>?

var body: some Scene {
    DocumentGroupLaunchScene("My Documents") {
        NewDocumentButton("Start Writing…")
        NewDocumentButton("Choose a Template", for: MyDocument.self) {
            try await withCheckedThrowingContinuation { continuation in
                documentCreationContinuation = continuation
                isTemplatePickerPresented = true
            }
        }
        .fullScreenCover(isPresented: $isTemplatePickerPresented) {
            TemplatePicker(continuation: $documentCreationContinuation)
        }
    }
}
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