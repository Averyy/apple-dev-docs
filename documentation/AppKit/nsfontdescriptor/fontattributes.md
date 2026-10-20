# fontAttributes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s dictionary of attributes.

**Availability**:
- macOS

## Declaration

```swift
var fontAttributes: [NSFontDescriptor.AttributeName : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * fontAttributes;
```

## See Also

### Getting the Font Attributes
- [func object(forKey: NSFontDescriptor.AttributeName) -> Any?](./object%28forkey%29.md)
  Returns the font attribute specified by the given key.
- [NSFontDescriptor.AttributeName](./attributename.md)
  Constants for the names of font attributes.
- [NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [var matrix: AffineTransform?](./matrix.md)
  The current transform matrix of the receiver.
- [var pointSize: CGFloat](./pointsize.md)
  The point size of the receiver.
- [var postscriptName: String?](./postscriptname.md)
  The PostScript name of the receiver.
- [NSFontDescriptor.FeatureKey](./featurekey.md)
  Constants to use as keys to retrieve information about a font descriptor from its feature dictionary.
- [typealias NSFontFamilyClass](../nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [var NSFontFamilyClassMask: UInt32](../nsfontfamilyclassmask.md)
  Constant you use to access `NSFontFamilyClass` values in the upper four bits of `NSFontSymbolicTraits`.
- [Typeface Information](../typeface-information.md)
  Constants for type faces such as italic or bold.
- [NSFontDescriptor.VariationKey](./variationkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/fontattributes)*