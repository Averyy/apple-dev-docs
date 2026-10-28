# init(fontAttributes:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a new font descriptor with the specified attributes.

**Availability**:
- macOS

## Declaration

```swift
init(fontAttributes attributes: [NSFontDescriptor.AttributeName : Any]? = nil)
```

```objc
- (instancetype) initWithFontAttributes:(NSDictionary<NSString *,id> *) attributes;
```

## Return Value

The new font descriptor.

## Parameters

- `attributes`: The attributes for the new font descriptor. If `nil`, the font descriptor’s attribute dictionary will be empty.

## See Also

### Creating a Font Descriptor
- [class func preferredFontDescriptor(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFontDescriptor](./preferredfontdescriptor%28fortextstyle,options%29.md)
  Returns a font descriptor that contains the text style.
- [init(name: String, matrix: AffineTransform)](./init%28name,matrix%29.md)
  Returns a font descriptor with the name and matrix attributes set to the given values.
- [init(name: String, size: CGFloat)](./init%28name,size%29.md)
  Returns a font descriptor with the name and size attributes set to the given values.
### Related Documentation
- [+ fontDescriptorWithFontAttributes:](./fontdescriptorwithfontattributes_.md)
  Returns a font descriptor with a dictionary of attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/init(fontattributes:))*