# submitScope(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.

**Availability**:
- iOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func submitScope(_ isBlocking: Bool = true) -> some View
```

#### Discussion

Use this modifier when you want to avoid specific views from initiating a submission action configured by the `View/onSubmit(of:_:)` modifier. In the example below, the tag field doesn’t trigger the submission of the form:

```None
Form {
    TextField("Username", text: $viewModel.userName)
    SecureField("Password", text: $viewModel.password)

    TextField("Tags", text: $viewModel.tags)
        .submitScope()
}
.onSubmit {
    guard viewModel.validate() else { return }
    viewModel.login()
}
```

## Parameters

- `isBlocking`: A Boolean that indicates whether this scope is   actively blocking submission triggers from reaching higher submission   actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/submitscope(_:))*