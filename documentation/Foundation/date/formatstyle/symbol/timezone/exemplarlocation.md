# exemplarLocation

**Framework**: Foundation  
**Kind**: property

The exemplar city for a timezone.

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
static var exemplarLocation: Date.FormatStyle.Symbol.TimeZone { get }
```

#### Discussion

If the exemplar city is unavailable, the system provides the localized exemplar city name for the special zone or `unknown`. For example, `Los Angeles`.

## See Also

- [static func specificName(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/specificname(_:).md)
  Returns the specific, non-location representation of a timezone.
- [static func genericName(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/genericname(_:).md)
  Returns the generic, non-location representation of a timezone.
- [static func iso8601(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/iso8601(_:).md)
  Creates the ISO 8601 representation of the timezone with hours, minutes, and optional seconds.
- [static func localizedGMT(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/localizedgmt(_:).md)
  Returns the localized GMT format representation of a timezone.
- [static func identifier(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/identifier(_:).md)
  Returns the timezone identifier.
- [static var genericLocation: Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/genericlocation.md)
  The generic location representation of a timezone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/timezone/exemplarlocation)*