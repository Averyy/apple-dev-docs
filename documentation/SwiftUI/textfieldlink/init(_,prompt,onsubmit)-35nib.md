# init(_:prompt:onSubmit:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a TextFieldLink which when pressed will request text input from the user.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, prompt: Text? = nil, onSubmit: @escaping (String) -> Void) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, prompt: Text? = nil, onSubmit: @escaping (String) -> Void)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, prompt: Text? = nil, onSubmit: @escaping (String) -> Void)
```

## Parameters

- `prompt`: Text which describes the reason for requesting text input.
- `onSubmit`: An action to perform when text input has been accepted and dismissed


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textfieldlink/init(_:prompt:onsubmit:)-35nib)*