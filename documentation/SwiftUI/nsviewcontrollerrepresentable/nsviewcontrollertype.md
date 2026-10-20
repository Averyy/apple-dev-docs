# NSViewControllerType

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of view controller to present.

**Availability**:
- macOS 10.15+

## Declaration

```swift
associatedtype NSViewControllerType : NSViewController
```

## See Also

### Creating and updating the view controller
- [func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType](./makensviewcontroller%28context%29.md)
  Creates the view controller object and configures its initial state.
- [func updateNSViewController(Self.NSViewControllerType, context: Self.Context)](./updatensviewcontroller%28_,context%29.md)
  Updates the state of the specified view controller with new information from SwiftUI.
- [NSViewControllerRepresentable.Context](./context.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/nsviewcontrollertype)*