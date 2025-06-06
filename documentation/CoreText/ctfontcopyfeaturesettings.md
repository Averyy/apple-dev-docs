# CTFontCopyFeatureSettings(_:)

**Framework**: Core Text  
**Kind**: func

Returns an array of font feature-setting tuples.

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
func CTFontCopyFeatureSettings(_ font: CTFont) -> CFArray?
```

#### Return Value

A normalized array of font feature-setting dictionaries. The array contains only the non-default settings that should be applied to the font, or `NULL` if the default settings should be used.

#### Discussion

A feature-setting dictionary is a tuple of a [`kCTFontFeatureTypeIdentifierKey`](kctfontfeaturetypeidentifierkey.md) key-value pair and a [`kCTFontFeatureSelectorIdentifierKey`](kctfontfeatureselectoridentifierkey.md) key-value pair. Each setting dictionary indicates which setting is enabled. It is the caller’s responsibility to handle exclusive and nonexclusive settings as necessary.

The feature settings are verified against those that the font supports and any that do not apply are removed. Further, feature settings that represent a default setting for the font are also removed.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontCopyFeatures(CTFont) -> CFArray?](ctfontcopyfeatures(_:).md)
  Returns an array of font features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyfeaturesettings(_:))*