# isRect(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Indicates whether or not a graphics path represents a rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isRect(_ rect: UnsafeMutablePointer<CGRect>?) -> Bool
```

```c
extern bool CGPathIsRect(CGPathRef path, CGRect *rect);
```

#### Return Value

A Boolean value that indicates whether the specified path represents a rectangle. If the path represents a rectangle, returns [`true`](../../Swift/true.md).

## Parameters

- `rect`: On input, a pointer to an uninitialized rectangle. If the specified path represents a rectangle, on return contains a copy of the rectangle.

## See Also

### Examining a Graphics Path
- [var boundingBox: CGRect](./boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](./boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [var currentPoint: CGPoint](./currentpoint.md)
  Returns the current point in a graphics path.
- [func contains(CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](./contains%28_,using,transform%29.md)
  Returns whether the specified point is interior to the path.
- [var isEmpty: Bool](./isempty.md)
  Indicates whether or not a graphics path is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/isrect(_:))*