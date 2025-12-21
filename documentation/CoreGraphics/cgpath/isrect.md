# isRect(_:)

**Framework**: Core Graphics  
**Kind**: method

Indicates whether or not a graphics path represents a rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isRect(_ rect: UnsafeMutablePointer<CGRect>?) -> Bool
```

#### Return Value

A Boolean value that indicates whether the specified path represents a rectangle. If the path represents a rectangle, returns [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `rect`: On input, a pointer to an uninitialized rectangle. If the specified path represents a rectangle, on return contains a copy of the rectangle.

## See Also

- [var boundingBox: CGRect](cgpath/boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](cgpath/boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [var currentPoint: CGPoint](cgpath/currentpoint.md)
  Returns the current point in a graphics path.
- [func contains(CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](cgpath/contains(_:using:transform:).md)
  Returns whether the specified point is interior to the path.
- [var isEmpty: Bool](cgpath/isempty.md)
  Indicates whether or not a graphics path is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/isrect(_:))*