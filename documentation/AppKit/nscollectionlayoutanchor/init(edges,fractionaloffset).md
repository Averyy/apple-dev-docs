# init(edges:fractionalOffset:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates an anchor with the specified edges to attach to, offset by the provided fractional value.

**Availability**:
- macOS 10.15+

## Declaration

```swift
convenience init(edges: NSDirectionalRectEdge, fractionalOffset: NSPoint)
```

```objc
+ (instancetype) layoutAnchorWithEdges:(NSDirectionalRectEdge) edges fractionalOffset:(NSPoint) fractionalOffset;
```

## See Also

### Creating an anchor
- [convenience init(edges: NSDirectionalRectEdge)](./init%28edges%29.md)
  Creates an anchor with the specified edges to attach to.
- [convenience init(edges: NSDirectionalRectEdge, absoluteOffset: NSPoint)](./init%28edges,absoluteoffset%29.md)
  Creates an anchor with the specified edges to attach to, offset by the provided absolute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutanchor/init(edges:fractionaloffset:))*