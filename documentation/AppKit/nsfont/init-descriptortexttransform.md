# init(descriptor:textTransform:)

**Framework**: AppKit  
**Kind**: init

Returns a font object for the specified font descriptor and text transform.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(descriptor fontDescriptor: NSFontDescriptor, textTransform: AffineTransform?)
```

#### Return Value

A font object for the specified name and transform.

#### Discussion

In most cases, you can simply use [`init(name:size:)`](nsfont/init(name:size:).md) to create standard scaled fonts. If `textTransform` is non-nil, it has precedence over `NSFontMatrixAttribute` in `fontDescriptor`.

## Parameters

- `fontDescriptor`: The font descriptor object describing the font to return.
- `textTransform`: An affine transformation applied to the font.

## See Also

- [init?(name: String, size: CGFloat)](nsfont/init(name:size:).md)
  Creates a font object for the specified font name and font size.
- [init?(descriptor: NSFontDescriptor, size: CGFloat)](nsfont/init(descriptor:size:).md)
  Returns a font object for the specified font descriptor and font size.
- [init?(name: String, matrix: UnsafePointer<CGFloat>)](nsfont/init(name:matrix:).md)
  Returns a font object for the specified font name and matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/init(descriptor:texttransform:))*