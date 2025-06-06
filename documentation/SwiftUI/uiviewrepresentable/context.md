# UIViewRepresentable.Context

**Framework**: SwiftUI  
**Kind**: typealias

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
typealias Context = UIViewRepresentableContext<Self>
```

## See Also

- [func makeUIView(context: Self.Context) -> Self.UIViewType](uiviewrepresentable/makeuiview(context:).md)
  Creates the view object and configures its initial state.
- [func updateUIView(Self.UIViewType, context: Self.Context)](uiviewrepresentable/updateuiview(_:context:).md)
  Updates the state of the specified view with new information from SwiftUI.
- [associatedtype UIViewType : UIView](uiviewrepresentable/uiviewtype.md)
  The type of view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentable/context)*