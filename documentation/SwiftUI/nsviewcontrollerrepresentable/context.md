# NSViewControllerRepresentable.Context

**Framework**: SwiftUI  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS 10.15+

## Declaration

```swift
typealias Context = NSViewControllerRepresentableContext<Self>
```

## See Also

### Creating and updating the view controller
- [func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType](./makensviewcontroller%28context%29.md)
  Creates the view controller object and configures its initial state.
- [func updateNSViewController(Self.NSViewControllerType, context: Self.Context)](./updatensviewcontroller%28_,context%29.md)
  Updates the state of the specified view controller with new information from SwiftUI.
- [associatedtype NSViewControllerType : NSViewController](./nsviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/context)*