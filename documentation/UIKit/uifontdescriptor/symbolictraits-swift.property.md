# symbolicTraits

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The traits of the font descriptor.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var symbolicTraits: UIFontDescriptor.SymbolicTraits { get }
```

```objc
@property (nonatomic, readonly) UIFontDescriptorSymbolicTraits symbolicTraits;
```

#### Discussion

The traits describe the font’s characteristics. For possible values, see [`UIFontDescriptor.SymbolicTraits`](./symbolictraits-swift.struct.md).

## See Also

### Querying a font descriptor
- [var fontAttributes: [UIFontDescriptor.AttributeName : Any]](./fontattributes.md)
  The font descriptor’s dictionary of attributes.
- [var matrix: CGAffineTransform](./matrix.md)
  The current transform matrix of the font descriptor.
- [func object(forKey: UIFontDescriptor.AttributeName) -> Any?](./object%28forkey%29.md)
  Returns the font attribute that the corresponding key specifies.
- [var pointSize: CGFloat](./pointsize.md)
  The point size of the font descriptor.
- [var postscriptName: String](./postscriptname.md)
  The PostScript name of the font descriptor.
- [UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.property)*