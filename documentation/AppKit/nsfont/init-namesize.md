# init(name:size:)

**Framework**: AppKit  
**Kind**: init

Creates a font object for the specified font name and font size.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(name fontName: String, size fontSize: CGFloat)
```

#### Return Value

A font object for the specified name and size.

#### Discussion

The value of the `fontName` parameter is a fully specified family-face name, preferably the PostScript name, such as Helvetica-BoldOblique or Times-Roman. (The Font Book app displays PostScript names of fonts in the Font Info panel.)

Specifying `fontSize` is equivalent to using a font matrix of [`fontSize` 0 0 `fontSize` 0 0] with [`init(descriptor:size:)`](nsfont/init(descriptor:size:).md). If you use a `fontSize` of 0.0, this method uses the default User Font size.

Fonts created with this method automatically flip themselves in flipped views. This method is the preferred means for creating fonts.

## Parameters

- `fontName`: The fully specified family-face name of the font.
- `fontSize`: The size in points to which the font is scaled.

## See Also

- [Cocoa Text Architecture Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)
- [init?(descriptor: NSFontDescriptor, size: CGFloat)](nsfont/init(descriptor:size:).md)
  Returns a font object for the specified font descriptor and font size.
- [init?(descriptor: NSFontDescriptor, textTransform: AffineTransform?)](nsfont/init(descriptor:texttransform:).md)
  Returns a font object for the specified font descriptor and text transform.
- [init?(name: String, matrix: UnsafePointer<CGFloat>)](nsfont/init(name:matrix:).md)
  Returns a font object for the specified font name and matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/init(name:size:))*