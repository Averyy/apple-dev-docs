# init(fontAttributes:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a new font descriptor with the specified attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
init(fontAttributes attributes: [NSFontDescriptor.AttributeName : Any]? = nil)
```

#### Return Value

The new font descriptor.

## Parameters

- `attributes`: The attributes for the new font descriptor. If  , the font descriptor’s attribute dictionary will be empty.

## See Also

- [class func preferredFontDescriptor(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFontDescriptor](nsfontdescriptor/preferredfontdescriptor(fortextstyle:options:).md)
  Returns a font descriptor that contains the text style.
- [init(name: String, matrix: AffineTransform)](nsfontdescriptor/init(name:matrix:).md)
  Returns a font descriptor with the name and matrix attributes set to the given values.
- [init(name: String, size: CGFloat)](nsfontdescriptor/init(name:size:).md)
  Returns a font descriptor with the name and size attributes set to the given values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/init(fontattributes:))*