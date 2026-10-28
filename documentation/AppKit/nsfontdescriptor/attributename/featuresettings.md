# featureSettings

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An array of dictionaries representing non-default font feature settings.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let featureSettings: NSFontDescriptor.AttributeName
```

```c
extern NSFontDescriptorAttributeName NSFontFeatureSettingsAttribute;
```

## Discussion

The value of this attribute is an [`NSArray`](../../../Foundation/nsarray.md) of [`NSDictionary`](../../../Foundation/nsdictionary.md) objects. Each dictionary contains [`typeIdentifier`](../featurekey/typeidentifier.md) and [`selectorIdentifier`](../featurekey/selectoridentifier.md).

## See Also

### Font Attributes
- [static let family: NSFontDescriptor.AttributeName](./family.md)
  An optional string object that specifies the font family.
- [static let name: NSFontDescriptor.AttributeName](./name.md)
  An optional string object that specifies the font name.
- [static let face: NSFontDescriptor.AttributeName](./face.md)
  An optional string object that specifies the font face.
- [static let size: NSFontDescriptor.AttributeName](./size.md)
  An optional floating-point number that specifies the font size.
- [static let visibleName: NSFontDescriptor.AttributeName](./visiblename.md)
  An optional string object that specifies the font’s visible name.
- [static let matrix: NSFontDescriptor.AttributeName](./matrix.md)
  An affine transform that specifies the font’s transformation matrix.
- [static let variation: NSFontDescriptor.AttributeName](./variation.md)
  A dictionary that describes the font’s variation axis.
- [static let characterSet: NSFontDescriptor.AttributeName](./characterset.md)
  The set of Unicode characters covered by the font.
- [static let cascadeList: NSFontDescriptor.AttributeName](./cascadelist.md)
  An array, each member of which is a sub-descriptor.
- [static let traits: NSFontDescriptor.AttributeName](./traits.md)
  A dictionary that fully describes the font traits.
- [static let fixedAdvance: NSFontDescriptor.AttributeName](./fixedadvance.md)
  A floating-point value that overrides the glyph advancement specified by the font.
- [NSFontColorAttribute](../../nsfontcolorattribute.md)
  An optional `NSData` object that specifies the font color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/attributename/featuresettings)*