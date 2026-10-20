# documentRegion

**Framework**: DataDetection  
**Kind**: property  
**Role**: Instance Property

A locale region that’s relevant to the scanned string.

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
var documentRegion: Locale.Region?
```

#### Discussion

Set `documentRegion` to the region relevant to the scanned string, if any.

> ❗ **Important**:  Only set this value if you know it with a high degree of confidence; otherwise, set to `nil`.

## See Also

### Hints you can provide to add more context for the matching process
- [var documentDate: Date?](./documentdate.md)
  The creation date of the scanned string.
- [var documentLanguageCode: Locale.LanguageCode?](./documentlanguagecode.md)
  An optional value that represents the language code of a specific locale.
- [var documentTimeZone: TimeZone?](./documenttimezone.md)
  A date that represents the date of the scanned string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/options/documentregion)*