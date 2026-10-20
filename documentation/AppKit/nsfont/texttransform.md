# textTransform

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current transformation matrix of the font.

**Availability**:
- macOS

## Declaration

```swift
var textTransform: AffineTransform { get }
```

```objc
@property (copy, readonly) NSAffineTransform * textTransform;
```

## See Also

### Related Documentation
- [func set()](./set%28%29.md)
  Sets this font as the font for the current graphics context.
### Getting the Font Matrices
- [var matrix: UnsafePointer<CGFloat>](./matrix.md)
  The transformation matrix associated with the font.
- [class var identityMatrix: UnsafePointer<CGFloat>](./identitymatrix.md)
  The identify matrix for the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/texttransform)*