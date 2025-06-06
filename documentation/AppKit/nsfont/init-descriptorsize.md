# init(descriptor:size:)

**Framework**: AppKit  
**Kind**: init

Returns a font object for the specified font descriptor and font size.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(descriptor fontDescriptor: NSFontDescriptor, size fontSize: CGFloat)
```

#### Return Value

A font object for the specified descriptor and size.

#### Discussion

In most cases, you can simply use [`init(name:size:)`](nsfont/init(name:size:).md) to create standard scaled fonts.

## Parameters

- `fontDescriptor`: A font descriptor object.
- `fontSize`: The size in points to which the font is scaled.

## See Also

- [init?(name: String, size: CGFloat)](nsfont/init(name:size:).md)
  Creates a font object for the specified font name and font size.
- [init?(descriptor: NSFontDescriptor, textTransform: AffineTransform?)](nsfont/init(descriptor:texttransform:).md)
  Returns a font object for the specified font descriptor and text transform.
- [init?(name: String, matrix: UnsafePointer<CGFloat>)](nsfont/init(name:matrix:).md)
  Returns a font object for the specified font name and matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/init(descriptor:size:))*