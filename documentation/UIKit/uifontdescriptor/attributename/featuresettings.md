# featureSettings

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The font feature settings attribute.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let featureSettings: UIFontDescriptor.AttributeName
```

```c
extern UIFontDescriptorAttributeName const UIFontDescriptorFeatureSettingsAttribute;
```

## Discussion

The value is an array of dictionaries that represents nondefault font feature settings. Each dictionary contains a [`type`](../featurekey/type.md) and [`selector`](../featurekey/selector.md) key.

## See Also

### Constants
- [static let cascadeList: UIFontDescriptor.AttributeName](./cascadelist.md)
  The cascading list attribute.
- [static let characterSet: UIFontDescriptor.AttributeName](./characterset.md)
  The character set attribute.
- [static let face: UIFontDescriptor.AttributeName](./face.md)
  The font face attribute.
- [static let family: UIFontDescriptor.AttributeName](./family.md)
  The font family attribute.
- [static let fixedAdvance: UIFontDescriptor.AttributeName](./fixedadvance.md)
  The glyph advancement attribute.
- [static let matrix: UIFontDescriptor.AttributeName](./matrix.md)
  The font’s transformation matrix attribute.
- [static let name: UIFontDescriptor.AttributeName](./name.md)
  The font name attribute.
- [static let size: UIFontDescriptor.AttributeName](./size.md)
  The font size attribute.
- [static let textStyle: UIFontDescriptor.AttributeName](./textstyle.md)
  The text style attribute.
- [static let traits: UIFontDescriptor.AttributeName](./traits.md)
  The font traits dictionary attribute.
- [static let visibleName: UIFontDescriptor.AttributeName](./visiblename.md)
  The font’s visible name attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/featuresettings)*