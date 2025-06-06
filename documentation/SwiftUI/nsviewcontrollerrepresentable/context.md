# NSViewControllerRepresentable.Context

**Framework**: SwiftUI  
**Kind**: typealias

**Availability**:
- macOS 10.15+

## Declaration

```swift
typealias Context = NSViewControllerRepresentableContext<Self>
```

## See Also

- [func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType](nsviewcontrollerrepresentable/makensviewcontroller(context:).md)
  Creates the view controller object and configures its initial state.
- [func updateNSViewController(Self.NSViewControllerType, context: Self.Context)](nsviewcontrollerrepresentable/updatensviewcontroller(_:context:).md)
  Updates the state of the specified view controller with new information from SwiftUI.
- [associatedtype NSViewControllerType : NSViewController](nsviewcontrollerrepresentable/nsviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/context)*