# DateIntervalFormatter.Style.short

**Framework**: Foundation  
**Kind**: case

An abbreviated date or time format.

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
case short
```

#### Discussion

For dates, this style displays the day, month, and year in numerical form using a format appropriate for the current locale. For example, formatting the date January 15, 2015 with this style results in the value “1/15/15” for US English and the value “15.1.15” for German.

For times, this style displays hours and minutes using a format appropriate for the current locale. For example, 12 hours and 33 minutes in the afternoon using a 12-hour clock results in the value “12:33 PM” for US English format and “12:33 nachm.” for German.

## See Also

- [DateIntervalFormatter.Style.none](dateintervalformatter/style/none.md)
  No information for the date or time. Use this style when you do not want to include date or time information in the resulting string.
- [DateIntervalFormatter.Style.medium](dateintervalformatter/style/medium.md)
  A medium length date or time format.
- [DateIntervalFormatter.Style.long](dateintervalformatter/style/long.md)
  A long length date or time format.
- [DateIntervalFormatter.Style.full](dateintervalformatter/style/full.md)
  A fully spelled out date or time format.
- [DateIntervalFormatter.Style.none](dateintervalformatter/style/none.md)
  No information for the date or time. Use this style when you do not want to include date or time information in the resulting string.
- [DateIntervalFormatter.Style.medium](dateintervalformatter/style/medium.md)
  A medium length date or time format.
- [DateIntervalFormatter.Style.long](dateintervalformatter/style/long.md)
  A long length date or time format.
- [DateIntervalFormatter.Style.full](dateintervalformatter/style/full.md)
  A fully spelled out date or time format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter/style/short)*