# newDocument

**Framework**: SwiftUI  
**Kind**: property

An action in the environment that presents a new document.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var newDocument: NewDocumentAction { get }
```

#### Discussion

Use the `newDocument` environment value to get the instance of the [`NewDocumentAction`](newdocumentaction.md) structure for a given [`Environment`](environment.md). Then call the instance to present a new document. You call the instance directly because it defines a [`callAsFunction(_:)`](newdocumentaction/callasfunction(_:).md) method that Swift calls when you call the instance.

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

## See Also

- [struct NewDocumentAction](newdocumentaction.md)
  An action that presents a new document.
- [var openDocument: OpenDocumentAction](environmentvalues/opendocument.md)
  An action in the environment that presents an existing document.
- [struct OpenDocumentAction](opendocumentaction.md)
  An action that presents an existing document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/newdocument)*