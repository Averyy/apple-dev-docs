# documentDate

**Framework**: DataDetection  
**Kind**: property

The creation date of the scanned string.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var documentDate: Date?
```

#### Discussion

Set `documentDate` to the creation date of the scanned string. For example, this property can represent the reception date of a text message. The default is now.

## See Also

- [var documentLanguageCode: Locale.LanguageCode?](datadetector/options/documentlanguagecode.md)
  An optional value that represents the language code of a specific locale.
- [var documentRegion: Locale.Region?](datadetector/options/documentregion.md)
  A locale region that’s relevant to the scanned string.
- [var documentTimeZone: TimeZone?](datadetector/options/documenttimezone.md)
  A date that represents the date of the scanned string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/options/documentdate)*