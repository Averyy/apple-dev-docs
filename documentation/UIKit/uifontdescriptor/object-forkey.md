# object(forKey:)

**Framework**: UIKit  
**Kind**: method

Returns the font attribute that the corresponding key specifies.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func object(forKey anAttribute: UIFontDescriptor.AttributeName) -> Any?
```

#### Return Value

The font attribute corresponding to `anAttribute`. For valid values of `anAttribute`, see [`UIFontDescriptor.AttributeName`](uifontdescriptor/attributename.md).

## Parameters

- `anAttribute`: The font attribute key.

## See Also

- [var fontAttributes: [UIFontDescriptor.AttributeName : Any]](uifontdescriptor/fontattributes.md)
  The font descriptor’s dictionary of attributes.
- [var matrix: CGAffineTransform](uifontdescriptor/matrix.md)
  The current transform matrix of the font descriptor.
- [var pointSize: CGFloat](uifontdescriptor/pointsize.md)
  The point size of the font descriptor.
- [var postscriptName: String](uifontdescriptor/postscriptname.md)
  The PostScript name of the font descriptor.
- [var symbolicTraits: UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.property.md)
  The traits of the font descriptor.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/object(forkey:))*