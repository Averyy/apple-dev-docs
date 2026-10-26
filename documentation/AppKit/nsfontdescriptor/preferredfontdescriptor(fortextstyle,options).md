# preferredFontDescriptor(forTextStyle:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a font descriptor that contains the text style.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func preferredFontDescriptor(forTextStyle style: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any] = [:]) -> NSFontDescriptor
```

```objc
+ (NSFontDescriptor *) preferredFontDescriptorForTextStyle:(NSFontTextStyle) style options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

The font descriptor that contains the text style.

#### Discussion

The font descriptor contains a dictionary of attributes that you use to create an [`NSFont`](../nsfont.md) object. See [`NSFontDescriptor`](../nsfontdescriptor.md) for more information.

## Parameters

- `style`: The text style for which to return a font descriptor. See [`NSFont.TextStyle`](../nsfont/textstyle.md) for available values.
- `options`: A dictionary you use to further configure the returned font descriptor. See [`NSFont.TextStyleOptionKey`](../nsfont/textstyleoptionkey.md) for a list of valid keys. Pass an empty dictionary to use the default configuration.

## See Also

### Creating a Font Descriptor
- [init(name: String, matrix: AffineTransform)](./init%28name,matrix%29.md)
  Returns a font descriptor with the name and matrix attributes set to the given values.
- [init(name: String, size: CGFloat)](./init%28name,size%29.md)
  Returns a font descriptor with the name and size attributes set to the given values.
- [init(fontAttributes: [NSFontDescriptor.AttributeName : Any]?)](./init%28fontattributes%29.md)
  Initializes and returns a new font descriptor with the specified attributes.
- [+ fontDescriptorWithFontAttributes:](./fontdescriptorwithfontattributes_.md)
  Returns a font descriptor with a dictionary of attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/preferredfontdescriptor(fortextstyle:options:))*