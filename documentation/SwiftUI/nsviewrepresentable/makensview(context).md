# makeNSView(context:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates the view object and configures its initial state.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func makeNSView(context: Self.Context) -> Self.NSViewType
```

## Return Value

Your AppKit view configured with the provided information.

## Discussion

You must implement this method and use it to create your view object. Configure the view using your app’s current data and contents of the `context` parameter. The system calls this method only once, when it creates your view for the first time. For all subsequent updates, the system calls the [`updateNSView(_:context:)`](./updatensview%28_,context%29.md) method.

## Parameters

- `context`: A context structure containing information about the current state of the system.

## See Also

### Creating and updating the view
- [func updateNSView(Self.NSViewType, context: Self.Context)](./updatensview%28_,context%29.md)
  Updates the state of the specified view with new information from SwiftUI.
- [NSViewRepresentable.Context](./context.md)
- [associatedtype NSViewType : NSView](./nsviewtype.md)
  The type of view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/makensview(context:))*