# submitLabel(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the submit label for this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
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

- [struct SubmitLabel](submitlabel.md)
  A semantic label describing the label of submission within a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/submitlabel(_:))*