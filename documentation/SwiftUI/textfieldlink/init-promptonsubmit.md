# init(_:prompt:onSubmit:)

**Framework**: SwiftUI  
**Kind**: init

Creates a TextFieldLink which when pressed will request text input from the user.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, prompt: Text? = nil, onSubmit: @escaping (String) -> Void)
```

## Parameters

- `titleKey`: A key for the TextFieldLink’s localized title, that describes the purpose of   requesting text input.
- `prompt`: Text which describes the reason for requesting text input.
- `onSubmit`: An action to perform when text input has been accepted and dismissed

## See Also

- [init(prompt: Text?, label: () -> Label, onSubmit: (String) -> Void)](textfieldlink/init(prompt:label:onsubmit:).md)
  Creates a TextFieldLink which when pressed will request text input from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldlink/init(_:prompt:onsubmit:))*