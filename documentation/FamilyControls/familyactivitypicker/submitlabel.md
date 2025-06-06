# submitLabel(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the submit label for this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func submitLabel(_ submitLabel: SubmitLabel) -> some View
```

#### Discussion

```swift
Form {
    TextField("Username", $viewModel.username)
        .submitLabel(.continue)
    SecureField("Password", $viewModel.password)
        .submitLabel(.done)
}
```

## Parameters

- `submitLabel`: One of the cases specified in  .

## See Also

- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](familyactivitypicker/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](familyactivitypicker/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/submitlabel(_:))*