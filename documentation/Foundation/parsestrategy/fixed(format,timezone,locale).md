# fixed(format:timeZone:locale:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

A fixed-format date parse strategy.

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
static func fixed(format: Date.FormatString, timeZone: TimeZone, locale: Locale? = nil) -> Self where Self == Date.ParseStrategy
```

## Return Value

A strategy for parsing a date.

## Parameters

- `format`: The string describing the parsing format.
- `timeZone`: The [`TimeZone`](../timezone.md) used to create the string representation of the date.
- `locale`: The [`Locale`](../locale.md) used to create the string representation of the date.

## See Also

### Commonly-used parsers
- [static var url: URL.ParseStrategy](./url.md)
  A parse strategy for URLs.
- [static var name: PersonNameComponents.ParseStrategy](./name.md)
  A parse strategy for person name components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parsestrategy/fixed(format:timezone:locale:))*