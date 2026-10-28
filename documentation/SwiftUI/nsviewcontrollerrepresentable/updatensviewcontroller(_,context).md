# updateNSViewController(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates the state of the specified view controller with new information from SwiftUI.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func updateNSViewController(_ nsViewController: Self.NSViewControllerType, context: Self.Context)
```

## Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding AppKit view controller. Use this method to update the configuration of your view controller to match the new state information provided in the `context` parameter.

## Parameters

- `nsViewController`: Your custom view controller object.
- `context`: A context structure containing information about the current state of the system.

## See Also

### Creating and updating the view controller
- [func makeNSViewController(context: Self.Context) -> Self.NSViewControllerType](./makensviewcontroller%28context%29.md)
  Creates the view controller object and configures its initial state.
- [NSViewControllerRepresentable.Context](./context.md)
- [associatedtype NSViewControllerType : NSViewController](./nsviewcontrollertype.md)
  The type of view controller to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/updatensviewcontroller(_:context:))*