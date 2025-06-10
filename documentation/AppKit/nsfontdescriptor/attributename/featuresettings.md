# featureSettings

**Framework**: AppKit  
**Kind**: property

An array of dictionaries representing non-default font feature settings.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let featureSettings: NSFontDescriptor.AttributeName
```

#### Discussion

The value of this attribute is an [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) of [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) objects. Each dictionary contains [`typeIdentifier`](nsfontdescriptor/featurekey/typeidentifier.md) and [`selectorIdentifier`](nsfontdescriptor/featurekey/selectoridentifier.md).

## See Also

- [static let family: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/family.md)
  An optional string object that specifies the font family.
- [static let name: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/name.md)
  An optional string object that specifies the font name.
- [static let face: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/face.md)
  An optional string object that specifies the font face.
- [static let size: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/size.md)
  An optional floating-point number that specifies the font size.
- [static let visibleName: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/visiblename.md)
  An optional string object that specifies the font’s visible name.
- [static let matrix: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/matrix.md)
  An affine transform that specifies the font’s transformation matrix.
- [static let variation: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/variation.md)
  A dictionary that describes the font’s variation axis.
- [static let characterSet: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/characterset.md)
  The set of Unicode characters covered by the font.
- [static let cascadeList: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/cascadelist.md)
  An array, each member of which is a sub-descriptor.
- [static let traits: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/traits.md)
  A dictionary that fully describes the font traits.
- [static let fixedAdvance: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/fixedadvance.md)
  A floating-point value that overrides the glyph advancement specified by the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/attributename/featuresettings)*