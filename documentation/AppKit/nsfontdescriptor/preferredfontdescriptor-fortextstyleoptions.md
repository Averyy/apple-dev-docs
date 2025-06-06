# preferredFontDescriptor(forTextStyle:options:)

**Framework**: AppKit  
**Kind**: method

Returns a font descriptor that contains the text style.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func preferredFontDescriptor(forTextStyle style: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any] = [:]) -> NSFontDescriptor
```

#### Return Value

The font descriptor that contains the text style.

#### Discussion

The font descriptor contains a dictionary of attributes that you use to create an [`NSFont`](nsfont.md) object. See [`NSFontDescriptor`](nsfontdescriptor.md) for more information.

## Parameters

- `style`: The text style for which to return a font descriptor. See   for available values.
- `options`: A dictionary you use to further configure the returned font descriptor. See   for a list of valid keys. Pass an empty dictionary to use the default configuration.

## See Also

- [init(name: String, matrix: AffineTransform)](nsfontdescriptor/init(name:matrix:).md)
  Returns a font descriptor with the name and matrix attributes set to the given values.
- [init(name: String, size: CGFloat)](nsfontdescriptor/init(name:size:).md)
  Returns a font descriptor with the name and size attributes set to the given values.
- [init(fontAttributes: [NSFontDescriptor.AttributeName : Any]?)](nsfontdescriptor/init(fontattributes:).md)
  Initializes and returns a new font descriptor with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/preferredfontdescriptor(fortextstyle:options:))*