# matrix

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current transform matrix of the font descriptor.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var matrix: CGAffineTransform { get }
```

```objc
@property (nonatomic, readonly) CGAffineTransform matrix;
```

## See Also

### Querying a font descriptor
- [var fontAttributes: [UIFontDescriptor.AttributeName : Any]](./fontattributes.md)
  The font descriptor’s dictionary of attributes.
- [func object(forKey: UIFontDescriptor.AttributeName) -> Any?](./object%28forkey%29.md)
  Returns the font attribute that the corresponding key specifies.
- [var pointSize: CGFloat](./pointsize.md)
  The point size of the font descriptor.
- [var postscriptName: String](./postscriptname.md)
  The PostScript name of the font descriptor.
- [var symbolicTraits: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.property.md)
  The traits of the font descriptor.
- [UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/matrix)*