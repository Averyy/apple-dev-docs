# TextFieldLink

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A control that requests text input from the user when pressed.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
struct TextFieldLink<Label> where Label : View
```

## Overview

A `TextFieldLink` should be used to request text input from the user through a button interface.

## Topics

### Creating a text field link
- [init(_:prompt:onSubmit:)](./textfieldlink/init%28_,prompt,onsubmit%29.md)
  Creates a TextFieldLink which when pressed will request text input from the user.
- [init(prompt: Text?, label: () -> Label, onSubmit: (String) -> Void)](./textfieldlink/init%28prompt,label,onsubmit%29.md)
  Creates a TextFieldLink which when pressed will request text input from the user.

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
- [struct TextEditor](./texteditor.md)
  A view that can display and edit long-form text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldlink)*