# NSFontDescriptor.AttributeName

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants for the names of font attributes.

**Availability**:
- macOS

## Declaration

```swift
struct AttributeName
```

```c
typedef NSString * NSFontDescriptorAttributeName;
```

#### Discussion

You can retrieve the values for these attributes using [`object(forKey:)`](./object%28forkey%29.md).

## Topics

### Font Attributes
- [static let family: NSFontDescriptor.AttributeName](./attributename/family.md)
  An optional string object that specifies the font family.
- [static let name: NSFontDescriptor.AttributeName](./attributename/name.md)
  An optional string object that specifies the font name.
- [static let face: NSFontDescriptor.AttributeName](./attributename/face.md)
  An optional string object that specifies the font face.
- [static let size: NSFontDescriptor.AttributeName](./attributename/size.md)
  An optional floating-point number that specifies the font size.
- [static let visibleName: NSFontDescriptor.AttributeName](./attributename/visiblename.md)
  An optional string object that specifies the font’s visible name.
- [static let matrix: NSFontDescriptor.AttributeName](./attributename/matrix.md)
  An affine transform that specifies the font’s transformation matrix.
- [static let variation: NSFontDescriptor.AttributeName](./attributename/variation.md)
  A dictionary that describes the font’s variation axis.
- [static let characterSet: NSFontDescriptor.AttributeName](./attributename/characterset.md)
  The set of Unicode characters covered by the font.
- [static let cascadeList: NSFontDescriptor.AttributeName](./attributename/cascadelist.md)
  An array, each member of which is a sub-descriptor.
- [static let traits: NSFontDescriptor.AttributeName](./attributename/traits.md)
  A dictionary that fully describes the font traits.
- [static let fixedAdvance: NSFontDescriptor.AttributeName](./attributename/fixedadvance.md)
  A floating-point value that overrides the glyph advancement specified by the font.
- [static let featureSettings: NSFontDescriptor.AttributeName](./attributename/featuresettings.md)
  An array of dictionaries representing non-default font feature settings.
### Initializers
- [init(String)](./attributename/init%28_%29.md)
- [init(rawValue: String)](./attributename/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Font Attributes
- [var fontAttributes: [NSFontDescriptor.AttributeName : Any]](./fontattributes.md)
  The receiver’s dictionary of attributes.
- [func object(forKey: NSFontDescriptor.AttributeName) -> Any?](./object%28forkey%29.md)
  Returns the font attribute specified by the given key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/attributename)*