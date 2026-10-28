# localizedGMT(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the localized GMT format representation of a timezone.

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
static func localizedGMT(_ width: Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone
```

## Return Value

A timezone format style appropriate for the locale and specified width.

## Discussion

For example, `GMT-7` ([`Date.FormatStyle.Symbol.TimeZone.Width.short`](./width/short.md)) or `GMT-07:00` ([`Date.FormatStyle.Symbol.TimeZone.Width.long`](./width/long.md)).

## Parameters

- `width`: Specifies the width of the string result.

## See Also

### Modifying a Time Zone
- [static func specificName(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./specificname%28_%29.md)
  Returns the specific, non-location representation of a timezone.
- [static func genericName(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./genericname%28_%29.md)
  Returns the generic, non-location representation of a timezone.
- [static func iso8601(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./iso8601%28_%29.md)
  Creates the ISO 8601 representation of the timezone with hours, minutes, and optional seconds.
- [static func identifier(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./identifier%28_%29.md)
  Returns the timezone identifier.
- [static var exemplarLocation: Date.FormatStyle.Symbol.TimeZone](./exemplarlocation.md)
  The exemplar city for a timezone.
- [static var genericLocation: Date.FormatStyle.Symbol.TimeZone](./genericlocation.md)
  The generic location representation of a timezone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/timezone/localizedgmt(_:))*