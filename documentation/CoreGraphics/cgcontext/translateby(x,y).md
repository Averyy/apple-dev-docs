# translateBy(x:y:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Changes the origin of the user coordinate system in a context.

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
func translateBy(x tx: CGFloat, y ty: CGFloat)
```

```c
extern void CGContextTranslateCTM(CGContextRef c, CGFloat tx, CGFloat ty);
```

## Parameters

- `tx`: The amount to displace the x-axis of the coordinate space, in units of the user space, of the specified context.
- `ty`: The amount to displace the y-axis of the coordinate space, in units of the user space, of the specified context.

## See Also

### Working with the Current Transformation Matrix
- [var ctm: CGAffineTransform](./ctm.md)
  Returns the current transformation matrix.
- [func rotate(by: CGFloat)](./rotate%28by%29.md)
  Rotates the user coordinate system in a context.
- [func scaleBy(x: CGFloat, y: CGFloat)](./scaleby%28x,y%29.md)
  Changes the scale of the user coordinate system in a context.
- [func concatenate(CGAffineTransform)](./concatenate%28_%29.md)
  Transforms the user coordinate system in a context using a specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/translateby(x:y:))*