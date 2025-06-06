# updateNSViewController(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Updates the state of the specified view controller with new information from SwiftUI.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func updateNSViewController(_ nsViewController: Self.NSViewControllerType, context: Self.Context)
```

#### Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding AppKit view controller. Use this method to update the configuration of your view controller to match the new state information provided in the `context` parameter.

## Parameters

- `nsViewController`: Your custom view controller object.
- `context`: A context structure containing information about the current   state of the system.

## See Also

- [func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType](nsviewcontrollerrepresentable/makensviewcontroller(context:).md)
  Creates the view controller object and configures its initial state.
- [NSViewControllerRepresentable.Context](nsviewcontrollerrepresentable/context.md)
- [associatedtype NSViewControllerType : NSViewController](nsviewcontrollerrepresentable/nsviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/updatensviewcontroller(_:context:))*