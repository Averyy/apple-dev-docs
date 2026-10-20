# init(prompt:label:onSubmit:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a TextFieldLink which when pressed will request text input from the user.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(prompt: Text? = nil, @ContentBuilder label: () -> Label, onSubmit: @escaping (String) -> Void)
```

Available when `Label` conforms to `View`.

## Parameters

- `prompt`: Text which describes the reason for requesting text input.
- `label`: A view that describes the action of requesting text input.
- `onSubmit`: An action to perform when text input has been accepted and dismissed

## See Also

### Creating a text field link
- [init(_:prompt:onSubmit:)](./init%28_,prompt,onsubmit%29.md)
  Creates a TextFieldLink which when pressed will request text input from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldlink/init(prompt:label:onsubmit:))*