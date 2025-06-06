# init(prompt:label:onSubmit:)

**Framework**: SwiftUI  
**Kind**: init

Creates a TextFieldLink which when pressed will request text input from the user.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(prompt: Text? = nil, @ViewBuilder label: () -> Label, onSubmit: @escaping (String) -> Void)
```

## Parameters

- `prompt`: Text which describes the reason for requesting text input.
- `label`: A view that describes the action of requesting text input.
- `onSubmit`: An action to perform when text input has been accepted and dismissed

## See Also

- [init(_:prompt:onSubmit:)](textfieldlink/init(_:prompt:onsubmit:).md)
  Creates a TextFieldLink which when pressed will request text input from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldlink/init(prompt:label:onsubmit:))*