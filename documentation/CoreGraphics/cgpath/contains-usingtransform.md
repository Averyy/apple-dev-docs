# contains(_:using:transform:)

**Framework**: Core Graphics  
**Kind**: method

Returns whether the specified point is interior to the path.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func contains(_ point: CGPoint, using rule: CGPathFillRule = .winding, transform: CGAffineTransform = .identity) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the point is interior to the path; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

A point is contained in a path if it would be inside the painted region when the path is filled.

## Parameters

- `point`: The point to check.
- `rule`: The rule for determining which areas to treat as the interior of the path. Defaults to the   rule if not specified.
- `transform`: An affine transform to apply to the point before checking for containment in the path. Defaults to the   transform if not specified.

## See Also

- [enum CGPathFillRule](cgpathfillrule.md)
  Rules for determining which regions are interior to a path, used by the [`fillPath(using:)`](cgcontext/fillpath(using:).md) and [`clip(using:)`](cgcontext/clip(using:).md) methods.
- [var boundingBox: CGRect](cgpath/boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](cgpath/boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [var currentPoint: CGPoint](cgpath/currentpoint.md)
  Returns the current point in a graphics path.
- [var isEmpty: Bool](cgpath/isempty.md)
  Indicates whether or not a graphics path is empty.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](cgpath/isrect(_:).md)
  Indicates whether or not a graphics path represents a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/contains(_:using:transform:))*