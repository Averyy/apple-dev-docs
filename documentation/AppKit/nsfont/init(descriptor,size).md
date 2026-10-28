# init(descriptor:size:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a font object for the specified font descriptor and font size.

**Availability**:
- macOS

## Declaration

```swift
init?(descriptor fontDescriptor: NSFontDescriptor, size fontSize: CGFloat)
```

```objc
+ (NSFont *) fontWithDescriptor:(NSFontDescriptor *) fontDescriptor size:(CGFloat) fontSize;
```

## Return Value

A font object for the specified descriptor and size.

## Discussion

In most cases, you can simply use [`init(name:size:)`](./init%28name,size%29.md) to create standard scaled fonts.

## Parameters

- `fontDescriptor`: A font descriptor object.
- `fontSize`: The size in points to which the font is scaled.

## See Also

### Creating Arbitrary Fonts
- [init?(name: String, size: CGFloat)](./init%28name,size%29.md)
  Creates a font object for the specified font name and font size.
- [init?(descriptor: NSFontDescriptor, textTransform: AffineTransform?)](./init%28descriptor,texttransform%29.md)
  Returns a font object for the specified font descriptor and text transform.
- [init?(name: String, matrix: UnsafePointer<CGFloat>)](./init%28name,matrix%29.md)
  Returns a font object for the specified font name and matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/init(descriptor:size:))*