# NewDocumentAction

**Framework**: SwiftUI  
**Kind**: struct

An action that presents a new document.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency struct NewDocumentAction
```

#### Overview

Use the [`newDocument`](environmentvalues/newdocument.md) environment value to get the instance of this structure for a given [`Environment`](environment.md). Then call the instance to present a new document. You call the instance directly because it defines a [`callAsFunction(_:)`](newdocumentaction/callasfunction(_:).md) method that Swift calls when you call the instance.

For example, you can define a button that creates a new document from the selected text:

```swift
struct NewDocumentFromSelection: View {
    @FocusedBinding(\.selectedText) private var selectedText: String?
    @Environment(\.newDocument) private var newDocument

    var body: some View {
        Button("New Document With Selection") {
            newDocument(TextDocument(text: selectedText))
        }
        .disabled(selectedText?.isEmpty != false)
    }
}
```

The above example assumes that you define a `TextDocument` that conforms to the [`FileDocument`](filedocument.md) or [`ReferenceFileDocument`](referencefiledocument.md) protocol, and a [`DocumentGroup`](documentgroup.md) that handles the associated file type.

## Topics

### Calling the action
- [func callAsFunction(_:)](newdocumentaction/callasfunction(_:).md)
  Presents a new document window.
- [func callAsFunction(contentType: UTType)](newdocumentaction/callasfunction(contenttype:).md)
  Presents a new document window.
- [func callAsFunction(contentType: UTType, prepareDocument: (ModelContext) -> Void)](newdocumentaction/callasfunction(contenttype:preparedocument:).md)
  Presents a new document window with preset contents.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var newDocument: NewDocumentAction](environmentvalues/newdocument.md)
  An action in the environment that presents a new document.
- [var openDocument: OpenDocumentAction](environmentvalues/opendocument.md)
  An action in the environment that presents an existing document.
- [struct OpenDocumentAction](opendocumentaction.md)
  An action that presents an existing document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentaction)*