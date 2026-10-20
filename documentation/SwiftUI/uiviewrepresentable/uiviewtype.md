# UIViewType

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of view to present.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
associatedtype UIViewType : UIView
```

## See Also

### Creating and updating the view
- [func makeUIView(context: Self.Context) -> Self.UIViewType](./makeuiview%28context%29.md)
  Creates the view object and configures its initial state.
- [func updateUIView(Self.UIViewType, context: Self.Context)](./updateuiview%28_,context%29.md)
  Updates the state of the specified view with new information from SwiftUI.
- [UIViewRepresentable.Context](./context.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentable/uiviewtype)*