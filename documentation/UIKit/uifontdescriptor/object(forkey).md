# object(forKey:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the font attribute that the corresponding key specifies.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func object(forKey anAttribute: UIFontDescriptor.AttributeName) -> Any?
```

```objc
- (id) objectForKey:(UIFontDescriptorAttributeName) anAttribute;
```

#### Return Value

The font attribute corresponding to `anAttribute`. For valid values of `anAttribute`, see [`UIFontDescriptor.AttributeName`](./attributename.md).

## Parameters

- `anAttribute`: The font attribute key.

## See Also

### Querying a font descriptor
- [var fontAttributes: [UIFontDescriptor.AttributeName : Any]](./fontattributes.md)
  The font descriptor’s dictionary of attributes.
- [var matrix: CGAffineTransform](./matrix.md)
  The current transform matrix of the font descriptor.
- [var pointSize: CGFloat](./pointsize.md)
  The point size of the font descriptor.
- [var postscriptName: String](./postscriptname.md)
  The PostScript name of the font descriptor.
- [var symbolicTraits: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.property.md)
  The traits of the font descriptor.
- [UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/object(forkey:))*