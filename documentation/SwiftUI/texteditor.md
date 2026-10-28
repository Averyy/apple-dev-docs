# TextEditor

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A view that can display and edit long-form text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
struct TextEditor
```

## Overview

A text editor view allows you to display and edit multiline, scrollable text in your app’s user interface. By default, the text editor view styles the text using characteristics inherited from the environment, like [`font(_:)`](./view/font%28_%29.md), [`foregroundColor(_:)`](./view/foregroundcolor%28_%29.md), and [`multilineTextAlignment(_:)`](./view/multilinetextalignment%28_%29.md). The text editor view supports attributed text formatting when initialized with [`init(text:selection:)`](./texteditor/init%28text,selection%29-11r0a.md).

You create a text editor by adding a `TextEditor` instance to the body of your view, and initialize it by passing in a [`Binding`](./binding.md) to a string variable in your app:

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

If you want to change the spacing or font scaling aspects of the text, you can use modifiers like [`lineSpacing(_:)`](./view/linespacing%28_%29.md) and [`minimumScaleFactor(_:)`](./view/minimumscalefactor%28_%29.md) to configure how the view displays text depending on the space constraints. For example, here the [`lineSpacing(_:)`](./view/linespacing%28_%29.md) modifier sets the spacing between lines to 5 points:

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

### Text formatting

When initialized with [`init(text:selection:)`](./texteditor/init%28text,selection%29-11r0a.md), `TextEditor` supports editing and formatting styled text.

By default, `TextEditor` shows system text formatting controls in the context menu and in the keyboard toolbar on iOS. Use [`textInputFormattingControlVisibility(_:for:)`](./view/textinputformattingcontrolvisibility%28_,for%29.md) to configure visibility of system text formatting controls.

For more information on formatting attributed text with `TextEditor`, see [`init(text:selection:)`](./texteditor/init%28text,selection%29-11r0a.md).

## Topics

### Creating a text editor
- [init(text: Binding<String>)](./texteditor/init%28text%29.md)
  Creates a plain text editor.
### Initializers
- [init(text:selection:)](./texteditor/init%28text,selection%29.md)
  Creates a styled text editor.

## Relationships

### Conforms To
- [View](./view.md)

## See Also

### Getting text input
- [Building rich SwiftUI text experiences](./building-rich-swiftui-text-experiences.md)
  Build an editor for formatted text using SwiftUI text editor views and attributed strings.
- [struct TextField](./textfield.md)
  A control that displays an editable text interface.
- [func textFieldStyle<S>(S) -> some View](./view/textfieldstyle%28_%29.md)
  Sets the style for text fields within this view.
- [struct SecureField](./securefield.md)
  A control into which people securely enter private text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/texteditor)*