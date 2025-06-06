# submitLabel(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the submit label for this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func submitLabel(_ submitLabel: SubmitLabel) -> some View
```

#### Discussion

```None
Form {
    TextField("Username", $viewModel.username)
        .submitLabel(.continue)
    SecureField("Password", $viewModel.password)
        .submitLabel(.done)
}
```

## Parameters

- `submitLabel`: One of the cases specified in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/submitlabel(_:))*