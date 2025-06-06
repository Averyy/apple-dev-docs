# variationAxes

**Framework**: Core Graphics  
**Kind**: property

Returns an array of the variation axis dictionaries for a font.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var variationAxes: CFArray? { get }
```

#### Discussion

A variation axis is a range included in a font by the font designer that allows a font to produce different type styles. Each variation axis dictionary contains key-value pairs that specify the variation axis name and the minimum, maximum, and default values for that variation axis.

## See Also

- [func copy(withVariations: CFDictionary?) -> CGFont?](cgfont/copy(withvariations:).md)
  Creates a copy of a font using a variation specification dictionary.
- [var variations: CFDictionary?](cgfont/variations.md)
  Returns the variation specification dictionary for a font.
- [Font Variation Axis Keys](font-variation-axis-keys.md)
  Keys used for a font variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/variationaxes)*