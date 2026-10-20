# init(name:matrix:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a font object for the specified font name and matrix.

**Availability**:
- macOS

## Declaration

```swift
init?(name fontName: String, matrix fontMatrix: UnsafePointer<CGFloat>)
```

```objc
+ (NSFont *) fontWithName:(NSString *) fontName matrix:(const CGFloat *) fontMatrix;
```

#### Return Value

A font object for the specified name and transformation matrix.

#### Discussion

The  `fontName` is a fully specified family-face name, such as Helvetica-BoldOblique or Times-Roman (not a name as shown in the Font Panel). The `fontMatrix` is a standard 6-element transformation matrix as used in the PostScript language, specifically with the `makefont` operator. In most cases, you can simply use [`init(name:size:)`](./init%28name,size%29.md) to create standard scaled fonts.

You can use the defined value `NSFontIdentityMatrix` for [1 0 0 1 0 0]. Fonts created with a matrix other than `NSFontIdentityMatrix` don’t automatically flip themselves in flipped views.

## Parameters

- `fontName`: The fully specified family-face name of the font.
- `fontMatrix`: A transformation matrix applied to the font.

## See Also

### Related Documentation
- [var isFlipped: Bool](../nsview/isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
### Creating Arbitrary Fonts
- [init?(name: String, size: CGFloat)](./init%28name,size%29.md)
  Creates a font object for the specified font name and font size.
- [init?(descriptor: NSFontDescriptor, size: CGFloat)](./init%28descriptor,size%29.md)
  Returns a font object for the specified font descriptor and font size.
- [init?(descriptor: NSFontDescriptor, textTransform: AffineTransform?)](./init%28descriptor,texttransform%29.md)
  Returns a font object for the specified font descriptor and text transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/init(name:matrix:))*