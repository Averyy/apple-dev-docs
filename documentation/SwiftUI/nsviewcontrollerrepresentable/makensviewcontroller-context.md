# makeNSViewController(context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates the view controller object and configures its initial state.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType
```

#### Return Value

Your AppKit view controller configured with the provided information.

#### Discussion

You must implement this method and use it to create your view controller object. Create the view controller using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view controller for the first time. For all subsequent updates, the system calls the [`updateNSViewController(_:context:)`](nsviewcontrollerrepresentable/updatensviewcontroller(_:context:).md) method.

## Parameters

- `context`: A context structure containing information about   the current state of the system.

## See Also

- [func updateNSViewController(Self.NSViewControllerType, context: Self.Context)](nsviewcontrollerrepresentable/updatensviewcontroller(_:context:).md)
  Updates the state of the specified view controller with new information from SwiftUI.
- [NSViewControllerRepresentable.Context](nsviewcontrollerrepresentable/context.md)
- [associatedtype NSViewControllerType : NSViewController](nsviewcontrollerrepresentable/nsviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/makensviewcontroller(context:))*