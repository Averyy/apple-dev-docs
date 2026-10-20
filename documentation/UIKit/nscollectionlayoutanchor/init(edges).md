# init(edges:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an anchor with the specified edges to attach to.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(edges: NSDirectionalRectEdge)
```

```objc
+ (instancetype) layoutAnchorWithEdges:(NSDirectionalRectEdge) edges;
```

## See Also

### Creating an anchor
- [convenience init(edges: NSDirectionalRectEdge, absoluteOffset: CGPoint)](./init%28edges,absoluteoffset%29.md)
  Creates an anchor with the specified edges to attach to, offset by the provided absolute value.
- [convenience init(edges: NSDirectionalRectEdge, fractionalOffset: CGPoint)](./init%28edges,fractionaloffset%29.md)
  Creates an anchor with the specified edges to attach to, offset by the provided fractional value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutanchor/init(edges:))*