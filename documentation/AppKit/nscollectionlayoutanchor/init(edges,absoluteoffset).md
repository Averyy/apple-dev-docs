# init(edges:absoluteOffset:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates an anchor with the specified edges to attach to, offset by the provided absolute value.

**Availability**:
- macOS 10.15+

## Declaration

```swift
convenience init(edges: NSDirectionalRectEdge, absoluteOffset: NSPoint)
```

```objc
+ (instancetype) layoutAnchorWithEdges:(NSDirectionalRectEdge) edges absoluteOffset:(NSPoint) absoluteOffset;
```

## See Also

### Creating an anchor
- [convenience init(edges: NSDirectionalRectEdge)](./init%28edges%29.md)
  Creates an anchor with the specified edges to attach to.
- [convenience init(edges: NSDirectionalRectEdge, fractionalOffset: NSPoint)](./init%28edges,fractionaloffset%29.md)
  Creates an anchor with the specified edges to attach to, offset by the provided fractional value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutanchor/init(edges:absoluteoffset:))*