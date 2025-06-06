# NSViewControllerType

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type of view controller to present.

**Availability**:
- macOS 10.15+

## Declaration

```swift
associatedtype NSViewControllerType : NSViewController
```

## See Also

- [func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType](nsviewcontrollerrepresentable/makensviewcontroller(context:).md)
  Creates the view controller object and configures its initial state.
- [func updateNSViewController(Self.NSViewControllerType, context: Self.Context)](nsviewcontrollerrepresentable/updatensviewcontroller(_:context:).md)
  Updates the state of the specified view controller with new information from SwiftUI.
- [NSViewControllerRepresentable.Context](nsviewcontrollerrepresentable/context.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/nsviewcontrollertype)*