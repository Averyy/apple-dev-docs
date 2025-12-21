# DateIntervalFormatter.Style.full

**Framework**: Foundation  
**Kind**: case

A fully spelled out date or time format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case full
```

#### Discussion

For dates, this style displays the numerical day and year and a spelled out version of the month and day of week using a format appropriate for the current locale. For example, formatting the date January 15, 2015 with this style results in the value “Thursday, January 15, 2015” for US English and the value “Donnerstag, 15. Januar 2015” for German.

For times, this style displays hours, minutes, seconds, and the spelled-out time zone information using a format appropriate for the current locale. For example, 12 hours, 33 minutes, and 29 seconds in the afternoon using a 12-hour clock and the Pacific Time Zone results in the value “12:33:29 PM Pacific Standard Time” for US English without daylight savings in effect and “12:33:29 Nordamerikanische Westküsten-Normalzeit” for German.

## See Also

- [DateIntervalFormatter.Style.none](dateintervalformatter/style/none.md)
  No information for the date or time. Use this style when you do not want to include date or time information in the resulting string.
- [DateIntervalFormatter.Style.short](dateintervalformatter/style/short.md)
  An abbreviated date or time format.
- [DateIntervalFormatter.Style.medium](dateintervalformatter/style/medium.md)
  A medium length date or time format.
- [DateIntervalFormatter.Style.long](dateintervalformatter/style/long.md)
  A long length date or time format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter/style/full)*