# DataDetector.Options

**Framework**: DataDetection  
**Kind**: struct

A set of options you can use to refine the behavior of text scanning, and better interpret the semantic domain of the matches.

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
struct Options
```

#### Overview

These properties are only hints, so it’s best to not make assumptions about how the framework uses them:

- Set `documentDate` to the creation date of the scanned string, such as a text message reception date. The default is now.
- Set `documentTimeZone` to the time zone matching the `documentDate`. The default is a person’s current time zone.
- Set `documentLanguageCode` to the language code of the scanned string, for example, “en” for English. Only set this property if you know the target language with a high degree of confidence; otherwise, set to `nil`.
- Set `documentRegion` to the region relevant to the scanned string, if any. Only set this property if you know the region with a high degree of confidence; otherwise, set to `nil`.

## Topics

### Hints you can provide to add more context for the matching process
- [var documentDate: Date?](datadetector/options/documentdate.md)
  The creation date of the scanned string.
- [var documentLanguageCode: Locale.LanguageCode?](datadetector/options/documentlanguagecode.md)
  An optional value that represents the language code of a specific locale.
- [var documentRegion: Locale.Region?](datadetector/options/documentregion.md)
  A locale region that’s relevant to the scanned string.
- [var documentTimeZone: TimeZone?](datadetector/options/documenttimezone.md)
  A date that represents the date of the scanned string.
### Initializers
- [init()](datadetector/options/init.md)
  Initializes a new data detector.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DataDetector.Match](datadetector/match.md)
  A representation of a match that includes common properties and an enumeration that represents the match type and its specific semantic components.
- [DataDetector.MatchType](datadetector/matchtype.md)
  A set of types of matches that the system can find in a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/options)*