# rotate(by:)

**Framework**: Core Graphics  
**Kind**: method

Rotates the user coordinate system in a context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func rotate(by angle: CGFloat)
```

#### Discussion

The direction that the context is rotated may appear to be altered by the state of the current transformation matrix prior to executing this function. For example, on iOS, a [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) applies a transformation to the graphics context that inverts the Y-axis (by multiplying it by `-1`). Rotating the user coordinate system on coordinate system that was previously flipped results in a rotation in the opposite direction (that is, positive values appear to rotate the coordinate system in the clockwise direction).

## Parameters

- `angle`: The angle, in radians, by which to rotate the coordinate space of the specified context. Positive values rotate counterclockwise and negative values rotate clockwise.)

## See Also

- [var ctm: CGAffineTransform](cgcontext/ctm.md)
  Returns the current transformation matrix.
- [func scaleBy(x: CGFloat, y: CGFloat)](cgcontext/scaleby(x:y:).md)
  Changes the scale of the user coordinate system in a context.
- [func translateBy(x: CGFloat, y: CGFloat)](cgcontext/translateby(x:y:).md)
  Changes the origin of the user coordinate system in a context.
- [func concatenate(CGAffineTransform)](cgcontext/concatenate(_:).md)
  Transforms the user coordinate system in a context using a specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/rotate(by:))*