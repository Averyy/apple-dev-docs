# characterSet

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The set of Unicode characters covered by the font.

**Availability**:
- macOS

## Declaration

```swift
static let characterSet: NSFontDescriptor.AttributeName
```

```c
extern NSFontDescriptorAttributeName NSFontCharacterSetAttribute;
```

## Discussion

The value of this attribute is an [`NSCharacterSet`](../../../Foundation/nscharacterset.md) object. The default value is supplied by the font.

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
- [static let cascadeList: NSFontDescriptor.AttributeName](./cascadelist.md)
  An array, each member of which is a sub-descriptor.
- [static let traits: NSFontDescriptor.AttributeName](./traits.md)
  A dictionary that fully describes the font traits.
- [static let fixedAdvance: NSFontDescriptor.AttributeName](./fixedadvance.md)
  A floating-point value that overrides the glyph advancement specified by the font.
- [static let featureSettings: NSFontDescriptor.AttributeName](./featuresettings.md)
  An array of dictionaries representing non-default font feature settings.
- [NSFontColorAttribute](../../nsfontcolorattribute.md)
  An optional `NSData` object that specifies the font color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/attributename/characterset)*