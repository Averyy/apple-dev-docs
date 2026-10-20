# translateBy(x:y:)

**Framework**: Core Graphics  
**Kind**: method

Changes the origin of the user coordinate system in a context.

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
func translateBy(x tx: CGFloat, y ty: CGFloat)
```

## Parameters

- `tx`: The amount to displace the x-axis of the coordinate space, in units of the user space, of the specified context.
- `ty`: The amount to displace the y-axis of the coordinate space, in units of the user space, of the specified context.

## See Also

- [var ctm: CGAffineTransform](cgcontext/ctm.md)
  Returns the current transformation matrix.
- [func rotate(by: CGFloat)](cgcontext/rotate(by:).md)
  Rotates the user coordinate system in a context.
- [func scaleBy(x: CGFloat, y: CGFloat)](cgcontext/scaleby(x:y:).md)
  Changes the scale of the user coordinate system in a context.
- [func concatenate(CGAffineTransform)](cgcontext/concatenate(_:).md)
  Transforms the user coordinate system in a context using a specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/translateby(x:y:))*