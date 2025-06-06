# matrix

**Framework**: AppKit  
**Kind**: property

The transformation matrix associated with the font.

**Availability**:
- macOS ?+

## Declaration

```swift
var matrix: UnsafePointer<CGFloat> { get }
```

#### Discussion

This property contains a standard six-element transformation matrix as used in the PostScript language, specifically with the `makefont` operator. In most cases, with a font of `fontSize`, this matrix is [`fontSize` 0 0 `fontSize` 0 0].

## See Also

- [init?(descriptor: NSFontDescriptor, size: CGFloat)](nsfont/init(descriptor:size:).md)
  Returns a font object for the specified font descriptor and font size.
- [var textTransform: AffineTransform](nsfont/texttransform.md)
  The current transformation matrix of the font.
- [class var identityMatrix: UnsafePointer<CGFloat>](nsfont/identitymatrix.md)
  The identify matrix for the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/matrix)*