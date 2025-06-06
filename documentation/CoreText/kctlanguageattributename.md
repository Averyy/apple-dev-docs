# kCTLanguageAttributeName

**Framework**: Core Text  
**Kind**: var

The name of the text language.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTLanguageAttributeName: CFString
```

#### Discussion

The value of this attribute must be a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) containing a language identifier conforming to [`UTS #35`](https://developer.apple.comhttp://unicode.org/reports/tr35/). The default is unset. When this attribute is set to a valid identifier, it will be used to select localized glyphs (if supported by the font), and locale-specific line-breaking rules.

## See Also

- [var ATSFONTREF_DEFINED: Int32](atsfontref_defined.md)
- [var kBSLNIdeographicHighBaseline: Int](kbslnideographichighbaseline.md)
- [let kCTAdaptiveImageProviderAttributeName: CFString](kctadaptiveimageproviderattributename.md)
- [let kCTBackgroundColorAttributeName: CFString](kctbackgroundcolorattributename.md)
- [let kCTBaselineClassAttributeName: CFString](kctbaselineclassattributename.md)
- [let kCTBaselineClassHanging: CFString](kctbaselineclasshanging.md)
- [let kCTBaselineClassIdeographicCentered: CFString](kctbaselineclassideographiccentered.md)
- [let kCTBaselineClassIdeographicHigh: CFString](kctbaselineclassideographichigh.md)
- [let kCTBaselineClassIdeographicLow: CFString](kctbaselineclassideographiclow.md)
- [let kCTBaselineClassMath: CFString](kctbaselineclassmath.md)
- [let kCTBaselineClassRoman: CFString](kctbaselineclassroman.md)
- [let kCTBaselineInfoAttributeName: CFString](kctbaselineinfoattributename.md)
- [let kCTBaselineOriginalFont: CFString](kctbaselineoriginalfont.md)
- [let kCTBaselineReferenceFont: CFString](kctbaselinereferencefont.md)
- [let kCTBaselineReferenceInfoAttributeName: CFString](kctbaselinereferenceinfoattributename.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctlanguageattributename)*