# copy(withVariations:)

**Framework**: Core Graphics  
**Kind**: method

Creates a copy of a font using a variation specification dictionary.

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
func copy(withVariations variations: CFDictionary?) -> CGFont?
```

#### Return Value

The font object.

## Parameters

- `variations`: A variation specification dictionary that contains keys corresponding to the variation axis names of the font. Each key in the dictionary is a variation axis name. The value for each key is the value specified for that particular variation axis represented as a CFNumber object. If a variation axis name is not specified in  , then the current value from   is used.

## See Also

- [var variations: CFDictionary?](cgfont/variations.md)
  Returns the variation specification dictionary for a font.
- [var variationAxes: CFArray?](cgfont/variationaxes.md)
  Returns an array of the variation axis dictionaries for a font.
- [Font Variation Axis Keys](font-variation-axis-keys.md)
  Keys used for a font variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/copy(withvariations:))*