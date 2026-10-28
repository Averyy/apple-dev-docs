# init(descriptor:textTransform:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a font object for the specified font descriptor and text transform.

**Availability**:
- macOS

## Declaration

```swift
init?(descriptor fontDescriptor: NSFontDescriptor, textTransform: AffineTransform?)
```

```objc
+ (NSFont *) fontWithDescriptor:(NSFontDescriptor *) fontDescriptor textTransform:(NSAffineTransform *) textTransform;
```

## Return Value

A font object for the specified name and transform.

## Discussion

In most cases, you can simply use [`init(name:size:)`](./init%28name,size%29.md) to create standard scaled fonts. If `textTransform` is non-nil, it has precedence over `NSFontMatrixAttribute` in `fontDescriptor`.

## Parameters

- `fontDescriptor`: The font descriptor object describing the font to return.
- `textTransform`: An affine transformation applied to the font.

## See Also

### Creating Arbitrary Fonts
- [init?(name: String, size: CGFloat)](./init%28name,size%29.md)
  Creates a font object for the specified font name and font size.
- [init?(descriptor: NSFontDescriptor, size: CGFloat)](./init%28descriptor,size%29.md)
  Returns a font object for the specified font descriptor and font size.
- [init?(name: String, matrix: UnsafePointer<CGFloat>)](./init%28name,matrix%29.md)
  Returns a font object for the specified font name and matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/init(descriptor:texttransform:))*