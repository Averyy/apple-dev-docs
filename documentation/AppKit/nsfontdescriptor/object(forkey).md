# object(forKey:)

**Framework**: AppKit  
**Kind**: method

Returns the font attribute specified by the given key.

**Availability**:
- macOS ?+

## Declaration

```swift
func object(forKey attribute: NSFontDescriptor.AttributeName) -> Any?
```

#### Return Value

The font attribute corresponding to `anAttribute`. For valid values of `anAttribute`, see `Font Attributes`.

## Parameters

- `attribute`: The font attribute key.

## See Also

- [var symbolicTraits: NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.property.md)
  A bit mask that describes the traits of the receiver.
- [var fontAttributes: [NSFontDescriptor.AttributeName : Any]](nsfontdescriptor/fontattributes.md)
  The receiver’s dictionary of attributes.
- [NSFontDescriptor.AttributeName](nsfontdescriptor/attributename.md)
  Constants for the names of font attributes.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [var matrix: AffineTransform?](nsfontdescriptor/matrix.md)
  The current transform matrix of the receiver.
- [var pointSize: CGFloat](nsfontdescriptor/pointsize.md)
  The point size of the receiver.
- [var postscriptName: String?](nsfontdescriptor/postscriptname.md)
  The PostScript name of the receiver.
- [NSFontDescriptor.FeatureKey](nsfontdescriptor/featurekey.md)
  Constants to use as keys to retrieve information about a font descriptor from its feature dictionary.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [var NSFontFamilyClassMask: UInt32](nsfontfamilyclassmask.md)
  Constant you use to access `NSFontFamilyClass` values in the upper four bits of `NSFontSymbolicTraits`.
- [Typeface Information](typeface-information.md)
  Constants for type faces such as italic or bold.
- [NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/object(forkey:))*