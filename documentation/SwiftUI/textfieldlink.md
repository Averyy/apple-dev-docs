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

#### Overview

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

### Linking to other content
- [struct Link](./link.md)
  A control for navigating to a URL.
- [struct ShareLink](./sharelink.md)
  A view that controls a sharing presentation.
- [struct SharePreview](./sharepreview.md)
  A representation of a type to display in a share preview.
- [struct HelpLink](./helplink.md)
  A button with a standard appearance that opens app-specific help documentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldlink)*