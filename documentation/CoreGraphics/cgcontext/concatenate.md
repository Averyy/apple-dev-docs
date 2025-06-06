# concatenate(_:)

**Framework**: Core Graphics  
**Kind**: method

Transforms the user coordinate system in a context using a specified matrix.

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
func concatenate(_ transform: CGAffineTransform)
```

#### Discussion

When you call this function, it concatenates (that is, it combines) two matrices, by multiplying them together. The order in which matrices are concatenated is important, as the operations are not commutative. The resulting CTM in the context is:   `CTMnew = transform * CTMcontext.`

## Parameters

- `transform`: The transformation matrix to apply to the specified context’s current transformation matrix.

## See Also

- [var ctm: CGAffineTransform](cgcontext/ctm.md)
  Returns the current transformation matrix.
- [func rotate(by: CGFloat)](cgcontext/rotate(by:).md)
  Rotates the user coordinate system in a context.
- [func scaleBy(x: CGFloat, y: CGFloat)](cgcontext/scaleby(x:y:).md)
  Changes the scale of the user coordinate system in a context.
- [func translateBy(x: CGFloat, y: CGFloat)](cgcontext/translateby(x:y:).md)
  Changes the origin of the user coordinate system in a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/concatenate(_:))*