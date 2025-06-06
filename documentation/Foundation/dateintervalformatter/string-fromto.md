# string(from:to:)

**Framework**: Foundation  
**Kind**: method

Returns a formatted string based on the specified start and end dates.

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
func string(from fromDate: Date, to toDate: Date) -> String
```

#### Return Value

A formatted string representing the specified date interval.

#### Discussion

The formatter includes both `fromDate` and `toDate` in the resulting string only when there is enough of a difference in their values to warrant the inclusion of both. If the date and time difference cannot be adequately displayed, the formatter displays one date value. For example, if the [`timeStyle`](dateintervalformatter/timestyle.md) property was set to [`DateIntervalFormatter.Style.none`](dateintervalformatter/style/none.md), the two dates would need to be at least one day apart in order for both to be displayed.

## Parameters

- `fromDate`: The start date. This date appears first in the resulting string.
- `toDate`: The end date. This date appears last after the hyphen in the resulting string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter/string(from:to:))*