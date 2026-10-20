# init(edges:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates an anchor with the specified edges to attach to.

**Availability**:
- macOS 10.15+

## Declaration

```swift
convenience init(edges: NSDirectionalRectEdge)
```

```objc
+ (instancetype) layoutAnchorWithEdges:(NSDirectionalRectEdge) edges;
```

## See Also

### Creating an anchor
- [convenience init(edges: NSDirectionalRectEdge, absoluteOffset: NSPoint)](./init%28edges,absoluteoffset%29.md)
  Creates an anchor with the specified edges to attach to, offset by the provided absolute value.
- [convenience init(edges: NSDirectionalRectEdge, fractionalOffset: NSPoint)](./init%28edges,fractionaloffset%29.md)
  Creates an anchor with the specified edges to attach to, offset by the provided fractional value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutanchor/init(edges:))*