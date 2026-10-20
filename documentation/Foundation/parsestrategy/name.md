# name

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A parse strategy for person name components.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var name: PersonNameComponents.ParseStrategy { get }
```

Available when `Self` is `PersonNameComponents.ParseStrategy`.

## See Also

### Commonly-used parsers
- [static func fixed(format: Date.FormatString, timeZone: TimeZone, locale: Locale?) -> Self](./fixed%28format,timezone,locale%29.md)
  A fixed-format date parse strategy.
- [static var url: URL.ParseStrategy](./url.md)
  A parse strategy for URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parsestrategy/name)*