# updateNSView(_:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Updates the state of the specified view with new information from SwiftUI.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func updateNSView(_ nsView: Self.NSViewType, context: Self.Context)
```

#### Discussion

When the state of your app changes, SwiftUI updates the portions of your interface affected by those changes. SwiftUI calls this method for any changes affecting the corresponding AppKit view. Use this method to update the configuration of your view to match the new state information provided in the `context` parameter.

## Parameters

- `nsView`: Your custom view object.
- `context`: A context structure containing information about the current   state of the system.

## See Also

- [func makeNSView(context: Self.Context) -> Self.NSViewType](nsviewrepresentable/makensview(context:).md)
  Creates the view object and configures its initial state.
- [NSViewRepresentable.Context](nsviewrepresentable/context.md)
- [associatedtype NSViewType : NSView](nsviewrepresentable/nsviewtype.md)
  The type of view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/updatensview(_:context:))*