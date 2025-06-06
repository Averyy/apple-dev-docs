# NSViewRepresentable.Context

**Framework**: SwiftUI  
**Kind**: typealias

**Availability**:
- macOS 10.15+

## Declaration

```swift
typealias Context = NSViewRepresentableContext<Self>
```

## See Also

- [func makeNSView(context: Self.Context) -> Self.NSViewType](nsviewrepresentable/makensview(context:).md)
  Creates the view object and configures its initial state.
- [func updateNSView(Self.NSViewType, context: Self.Context)](nsviewrepresentable/updatensview(_:context:).md)
  Updates the state of the specified view with new information from SwiftUI.
- [associatedtype NSViewType : NSView](nsviewrepresentable/nsviewtype.md)
  The type of view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/context)*