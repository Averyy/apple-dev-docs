# secondsFromGMT(for:)

**Framework**: Foundation  
**Kind**: method

The current difference in seconds between the time zone and Greenwich Mean Time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func secondsFromGMT(for date: Date = Date()) -> Int
```

## Parameters

- `date`: The date to use for the calculation. The default value is the current date.

## See Also

- [var identifier: String](timezone/identifier.md)
  The geopolitical region identifier that identifies the time zone.
- [func abbreviation(for: Date) -> String?](timezone/abbreviation(for:).md)
  Returns the abbreviation for the time zone at a given date.
- [static var timeZoneDataVersion: String](timezone/timezonedataversion.md)
  Returns the time zone data version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timezone/secondsfromgmt(for:))*