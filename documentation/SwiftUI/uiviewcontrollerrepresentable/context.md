# UIViewControllerRepresentable.Context

**Framework**: SwiftUI  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
typealias Context = UIViewControllerRepresentableContext<Self>
```

## See Also

### Creating and updating the view controller
- [func makeUIViewController(context: Self.Context) -> Self.UIViewControllerType](./makeuiviewcontroller%28context%29.md)
  Creates the view controller object and configures its initial state.
- [func updateUIViewController(Self.UIViewControllerType, context: Self.Context)](./updateuiviewcontroller%28_,context%29.md)
  Updates the state of the specified view controller with new information from SwiftUI.
- [associatedtype UIViewControllerType : UIViewController](./uiviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable/context)*