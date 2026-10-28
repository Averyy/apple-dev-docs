# url

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A parse strategy for URLs.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var url: URL.ParseStrategy { get }
```

Available when `Self` is `URL.ParseStrategy`.

## Discussion

Use the dot-notation form of this type property when the call point allows the use of [`URL.ParseStrategy`](../url/parsestrategy.md). Typically, you use this with the URL initializer [`init(_:strategy:)`](../url/init%28_,strategy%29.md).

## See Also

### Commonly-used parsers
- [static func fixed(format: Date.FormatString, timeZone: TimeZone, locale: Locale?) -> Self](./fixed%28format,timezone,locale%29.md)
  A fixed-format date parse strategy.
- [static var name: PersonNameComponents.ParseStrategy](./name.md)
  A parse strategy for person name components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parsestrategy/url)*