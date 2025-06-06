# TextEditor

**Framework**: SwiftUI  
**Kind**: struct

A view that can display and edit long-form text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct TextEditor
```

#### Overview

A text editor view allows you to display and edit multiline, scrollable text in your app’s user interface. By default, the text editor view styles the text using characteristics inherited from the environment, like [`font(_:)`](view/font(_:).md), [`foregroundColor(_:)`](view/foregroundcolor(_:).md), and [`multilineTextAlignment(_:)`](view/multilinetextalignment(_:).md).

You create a text editor by adding a `TextEditor` instance to the body of your view, and initialize it by passing in a [`Binding`](binding.md) to a string variable in your app:

```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
    }
}
```

To style the text, use the standard view modifiers to configure a system font, set a custom font, or change the color of the view’s text.

In this example, the view renders the editor’s text in gray with a custom font:

```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
    }
}
```

If you want to change the spacing or font scaling aspects of the text, you can use modifiers like [`lineLimit(_:)`](view/linelimit(_:).md), [`lineSpacing(_:)`](view/linespacing(_:).md), and [`minimumScaleFactor(_:)`](view/minimumscalefactor(_:).md) to configure how the view displays text depending on the space constraints. For example, here the [`lineSpacing(_:)`](view/linespacing(_:).md) modifier sets the spacing between lines to 5 points:

```swift
struct TextEditingView: View {
    @State private var fullText: String = "This is some editable text..."

    var body: some View {
        TextEditor(text: $fullText)
            .foregroundColor(Color.gray)
            .font(.custom("HelveticaNeue", size: 13))
            .lineSpacing(5)
    }
}
```

## Topics

### Creating a text editor
- [init(text: Binding<String>)](texteditor/init(text:).md)
  Creates a plain text editor.
### Initializers
- [init(text: Binding<String>, selection: Binding<TextSelection?>)](texteditor/init(text:selection:).md)
  Creates a plain text editor that captures the current selection.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct TextField](textfield.md)
  A control that displays an editable text interface.
- [func textFieldStyle<S>(S) -> some View](view/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [struct SecureField](securefield.md)
  A control into which people securely enter private text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/texteditor)*