# draw(_:at:)

**Framework**: Core Graphics  
**Kind**: method

Draws the contents of a layer object at the specified point.

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
func draw(_ layer: CGLayer, at point: CGPoint)
```

#### Discussion

Calling this method is equivalent to calling the [`draw(_:in:)`](cgcontext/draw(_:in:).md) method with a rectangle whose origin is the specified point and whose size matches that of the specified layer.

## Parameters

- `layer`: The layer whose contents you want to draw.
- `point`: The location, in current user space coordinates, to use as the origin for the drawing.

## See Also

- [func draw(CGLayer, in: CGRect)](cgcontext/draw(_:in:).md)
  Draws the contents of a layer object into the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/draw(_:at:))*