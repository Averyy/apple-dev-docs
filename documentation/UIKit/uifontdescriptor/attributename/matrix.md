# matrix

**Framework**: UIKit  
**Kind**: property

The font’s transformation matrix attribute.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let matrix: UIFontDescriptor.AttributeName
```

#### Discussion

The value is a [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) instance that specifies the font’s transformation matrix. The default value is the identity matrix.

Because the system applies the matrix to the text matrix at rendering time, translation isn’t available. The rendering engine determines the translation independently.

## See Also

- [static let cascadeList: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/cascadelist.md)
  The cascading list attribute.
- [static let characterSet: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/characterset.md)
  The character set attribute.
- [static let face: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/face.md)
  The font face attribute.
- [static let family: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/family.md)
  The font family attribute.
- [static let featureSettings: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/featuresettings.md)
  The font feature settings attribute.
- [static let fixedAdvance: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/fixedadvance.md)
  The glyph advancement attribute.
- [static let name: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/name.md)
  The font name attribute.
- [static let size: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/size.md)
  The font size attribute.
- [static let textStyle: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/textstyle.md)
  The text style attribute.
- [static let traits: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/traits.md)
  The font traits dictionary attribute.
- [static let visibleName: UIFontDescriptor.AttributeName](uifontdescriptor/attributename/visiblename.md)
  The font’s visible name attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/matrix)*