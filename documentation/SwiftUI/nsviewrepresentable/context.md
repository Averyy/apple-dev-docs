# NSViewRepresentable.Context

**Framework**: SwiftUI  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS 10.15+

## Declaration

```swift
typealias Context = NSViewRepresentableContext<Self>
```

## See Also

### Creating and updating the view
- [func makeNSView(context: Self.Context) -> Self.NSViewType](./makensview%28context%29.md)
  Creates the view object and configures its initial state.
- [func updateNSView(Self.NSViewType, context: Self.Context)](./updatensview%28_,context%29.md)
  Updates the state of the specified view with new information from SwiftUI.
- [associatedtype NSViewType : NSView](./nsviewtype.md)
  The type of view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/context)*