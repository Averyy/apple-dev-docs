# kCTFontDownloadedAttribute

**Framework**: Core Text  
**Kind**: var

The download state.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTFontDownloadedAttribute: CFString
```

#### Discussion

The value associated with this key is a doc://com.apple.documentation/documentation/corefoundation/cfboolean-s0p.  If it is [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), corresponding Font Asset has been downloaded.

> **Note**:  It may still be necessary to call appropriate API in order to use the font in the Font Asset.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontdownloadedattribute)*