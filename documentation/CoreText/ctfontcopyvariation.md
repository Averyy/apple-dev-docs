# CTFontCopyVariation(_:)

**Framework**: Core Text  
**Kind**: func

Returns a variation dictionary from the font reference.

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
func CTFontCopyVariation(_ font: CTFont) -> CFDictionary?
```

#### Return Value

The current variation instance as a dictionary.

#### Discussion

The keys for each variation correspond to the variation identifier obtained via [`kCTFontVariationAxisIdentifierKey`](kctfontvariationaxisidentifierkey.md), which represents the four-character axis code as a CFNumber object.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontCopyVariationAxes(CTFont) -> CFArray?](ctfontcopyvariationaxes(_:).md)
  Returns an array of variation axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyvariation(_:))*