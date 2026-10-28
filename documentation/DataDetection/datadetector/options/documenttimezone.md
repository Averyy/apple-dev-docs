# documentTimeZone

**Framework**: DataDetection  
**Kind**: property  
**Role**: Instance Property

A date that represents the date of the scanned string.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var documentTimeZone: TimeZone?
```

## Discussion

This is the date that’s relevant to the subject of the string the system in scanning, such as a text message reception date. The default is “now.”

## See Also

### Hints you can provide to add more context for the matching process
- [var documentDate: Date?](./documentdate.md)
  The creation date of the scanned string.
- [var documentLanguageCode: Locale.LanguageCode?](./documentlanguagecode.md)
  An optional value that represents the language code of a specific locale.
- [var documentRegion: Locale.Region?](./documentregion.md)
  A locale region that’s relevant to the scanned string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/options/documenttimezone)*