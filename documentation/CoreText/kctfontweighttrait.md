# kCTFontWeightTrait

**Framework**: Core Text  
**Kind**: var

The normalized weight trait from the font traits dictionary.

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
let kCTFontWeightTrait: CFString
```

#### Discussion

The value returned is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) representing a float value between `-1.0` and `1.0` for normalized weight. The value of `0.0` corresponds to the regular or medium font weight.

## See Also

- [let kCTFontSymbolicTrait: CFString](kctfontsymbolictrait.md)
  The symbolic traits value from the font traits dictionary.
- [let kCTFontWidthTrait: CFString](kctfontwidthtrait.md)
  The normalized proportion (width condense or expand) trait from the font traits dictionary.
- [let kCTFontSlantTrait: CFString](kctfontslanttrait.md)
  The normalized slant angle from the font traits dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontweighttrait)*