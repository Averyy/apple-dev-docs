# scaleBy(x:y:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Changes the scale of the user coordinate system in a context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func scaleBy(x sx: CGFloat, y sy: CGFloat)
```

```c
extern void CGContextScaleCTM(CGContextRef c, CGFloat sx, CGFloat sy);
```

## Parameters

- `sx`: The factor by which to scale the x-axis of the coordinate space of the specified context.
- `sy`: The factor by which to scale the y-axis of the coordinate space of the specified context.

## See Also

### Working with the Current Transformation Matrix
- [var ctm: CGAffineTransform](./ctm.md)
  Returns the current transformation matrix.
- [func rotate(by: CGFloat)](./rotate%28by%29.md)
  Rotates the user coordinate system in a context.
- [func translateBy(x: CGFloat, y: CGFloat)](./translateby%28x,y%29.md)
  Changes the origin of the user coordinate system in a context.
- [func concatenate(CGAffineTransform)](./concatenate%28_%29.md)
  Transforms the user coordinate system in a context using a specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/scaleby(x:y:))*