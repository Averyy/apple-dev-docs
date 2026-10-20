# init(name:matrix:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a font descriptor with the name and matrix attributes set to the given values.

**Availability**:
- macOS

## Declaration

```swift
init(name fontName: String, matrix: AffineTransform)
```

```objc
+ (NSFontDescriptor *) fontDescriptorWithName:(NSString *) fontName matrix:(NSAffineTransform *) matrix;
```

#### Return Value

The new font descriptor.

## Parameters

- `fontName`: The value for `NSFontNameAttribute`.
- `matrix`: The value for `NSFontMatrixAttribute`.

## See Also

### Creating a Font Descriptor
- [class func preferredFontDescriptor(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFontDescriptor](./preferredfontdescriptor%28fortextstyle,options%29.md)
  Returns a font descriptor that contains the text style.
- [init(name: String, size: CGFloat)](./init%28name,size%29.md)
  Returns a font descriptor with the name and size attributes set to the given values.
- [init(fontAttributes: [NSFontDescriptor.AttributeName : Any]?)](./init%28fontattributes%29.md)
  Initializes and returns a new font descriptor with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/init(name:matrix:))*