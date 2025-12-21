# variations

**Framework**: Core Graphics  
**Kind**: property

Returns the variation specification dictionary for a font.

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
var variations: CFDictionary? { get }
```

#### Discussion

The variation specification dictionary contains keys that correspond to the variation axis names of the font. Each key is a variation axis name. The value for each key is the value specified for that particular variation axis represented as a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object.

## See Also

- [func copy(withVariations: CFDictionary?) -> CGFont?](cgfont/copy(withvariations:).md)
  Creates a copy of a font using a variation specification dictionary.
- [var variationAxes: CFArray?](cgfont/variationaxes.md)
  Returns an array of the variation axis dictionaries for a font.
- [Font Variation Axis Keys](font-variation-axis-keys.md)
  Keys used for a font variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/variations)*