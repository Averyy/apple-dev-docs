# ctm

**Framework**: Core Graphics  
**Kind**: property

Returns the current transformation matrix.

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
var ctm: CGAffineTransform { get }
```

## See Also

- [func rotate(by: CGFloat)](cgcontext/rotate(by:).md)
  Rotates the user coordinate system in a context.
- [func scaleBy(x: CGFloat, y: CGFloat)](cgcontext/scaleby(x:y:).md)
  Changes the scale of the user coordinate system in a context.
- [func translateBy(x: CGFloat, y: CGFloat)](cgcontext/translateby(x:y:).md)
  Changes the origin of the user coordinate system in a context.
- [func concatenate(CGAffineTransform)](cgcontext/concatenate(_:).md)
  Transforms the user coordinate system in a context using a specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/ctm)*