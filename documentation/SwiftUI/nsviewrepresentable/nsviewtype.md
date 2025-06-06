# NSViewType

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type of view to present.

**Availability**:
- macOS 10.15+

## Declaration

```swift
associatedtype NSViewType : NSView
```

## See Also

- [func makeNSView(context: Self.Context) -> Self.NSViewType](nsviewrepresentable/makensview(context:).md)
  Creates the view object and configures its initial state.
- [func updateNSView(Self.NSViewType, context: Self.Context)](nsviewrepresentable/updatensview(_:context:).md)
  Updates the state of the specified view with new information from SwiftUI.
- [NSViewRepresentable.Context](nsviewrepresentable/context.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/nsviewtype)*