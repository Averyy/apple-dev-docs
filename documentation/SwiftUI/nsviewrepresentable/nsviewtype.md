# NSViewType

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of view to present.

**Availability**:
- macOS 10.15+

## Declaration

```swift
associatedtype NSViewType : NSView
```

## See Also

### Creating and updating the view
- [func makeNSView(context: Self.Context) -> Self.NSViewType](./makensview%28context%29.md)
  Creates the view object and configures its initial state.
- [func updateNSView(Self.NSViewType, context: Self.Context)](./updatensview%28_,context%29.md)
  Updates the state of the specified view with new information from SwiftUI.
- [NSViewRepresentable.Context](./context.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/nsviewtype)*