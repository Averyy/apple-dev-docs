# init(name:size:)

**Framework**: AppKit  
**Kind**: init

Returns a font descriptor with the name and size attributes set to the given values.

**Availability**:
- macOS ?+

## Declaration

```swift
init(name fontName: String, size: CGFloat)
```

#### Return Value

The new font descriptor.

## Parameters

- `fontName`: The value for  .
- `size`: The value for  .

## See Also

- [class func preferredFontDescriptor(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFontDescriptor](nsfontdescriptor/preferredfontdescriptor(fortextstyle:options:).md)
  Returns a font descriptor that contains the text style.
- [init(name: String, matrix: AffineTransform)](nsfontdescriptor/init(name:matrix:).md)
  Returns a font descriptor with the name and matrix attributes set to the given values.
- [init(fontAttributes: [NSFontDescriptor.AttributeName : Any]?)](nsfontdescriptor/init(fontattributes:).md)
  Initializes and returns a new font descriptor with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/init(name:size:))*