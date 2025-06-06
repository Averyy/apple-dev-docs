# CTFontCopyFeatures(_:)

**Framework**: Core Text  
**Kind**: func

Returns an array of font features.

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
func CTFontCopyFeatures(_ font: CTFont) -> CFArray?
```

#### Return Value

An array of font feature dictionaries for the font reference.

## Parameters

- `font`: The font reference.

## See Also

- [func CTFontCopyFeatureSettings(CTFont) -> CFArray?](ctfontcopyfeaturesettings(_:).md)
  Returns an array of font feature-setting tuples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontcopyfeatures(_:))*