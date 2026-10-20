# NSFontFamilyClassMask

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Constant you use to access `NSFontFamilyClass` values in the upper four bits of `NSFontSymbolicTraits`.

**Availability**:
- macOS

## Declaration

```swift
var NSFontFamilyClassMask: UInt32 { get }
```

```c
NSFontFamilyClassMask
```

#### Discussion

The font family class mask you use to access `NSFontFamilyClass` values.

## See Also

### Getting the Font Attributes
- [var fontAttributes: [NSFontDescriptor.AttributeName : Any]](./nsfontdescriptor/fontattributes.md)
  The receiver’s dictionary of attributes.
- [func object(forKey: NSFontDescriptor.AttributeName) -> Any?](./nsfontdescriptor/object%28forkey%29.md)
  Returns the font attribute specified by the given key.
- [NSFontDescriptor.AttributeName](./nsfontdescriptor/attributename.md)
  Constants for the names of font attributes.
- [NSFontDescriptor.SymbolicTraits](./nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [var matrix: AffineTransform?](./nsfontdescriptor/matrix.md)
  The current transform matrix of the receiver.
- [var pointSize: CGFloat](./nsfontdescriptor/pointsize.md)
  The point size of the receiver.
- [var postscriptName: String?](./nsfontdescriptor/postscriptname.md)
  The PostScript name of the receiver.
- [NSFontDescriptor.FeatureKey](./nsfontdescriptor/featurekey.md)
  Constants to use as keys to retrieve information about a font descriptor from its feature dictionary.
- [typealias NSFontFamilyClass](./nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [Typeface Information](./typeface-information.md)
  Constants for type faces such as italic or bold.
- [NSFontDescriptor.VariationKey](./nsfontdescriptor/variationkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontfamilyclassmask)*