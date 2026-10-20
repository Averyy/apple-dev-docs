# init(edges:absoluteOffset:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an anchor with the specified edges to attach to, offset by the provided absolute value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(edges: NSDirectionalRectEdge, absoluteOffset: CGPoint)
```

```objc
+ (instancetype) layoutAnchorWithEdges:(NSDirectionalRectEdge) edges absoluteOffset:(CGPoint) absoluteOffset;
```

## See Also

### Creating an anchor
- [convenience init(edges: NSDirectionalRectEdge)](./init%28edges%29.md)
  Creates an anchor with the specified edges to attach to.
- [convenience init(edges: NSDirectionalRectEdge, fractionalOffset: CGPoint)](./init%28edges,fractionaloffset%29.md)
  Creates an anchor with the specified edges to attach to, offset by the provided fractional value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutanchor/init(edges:absoluteoffset:))*