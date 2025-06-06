# CTFontCopyVariationAxes(_:)

**Framework**: Core Text  
**Kind**: func

Returns an array of variation axes.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontCopyVariationAxes(_ font: CTFont) -> CFArray?
```

#### Return Value

An array of variation axes dictionaries. Each variation axis dictionary contains the five variation axis keys listed in [`Font Variation Axis Dictionary Keys`](font-variation-axis-dictionary-keys.md).

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontCopyVariation(CTFont) -> CFDictionary?](ctfontcopyvariation(_:).md)
  Returns a variation dictionary from the font reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyvariationaxes(_:))*