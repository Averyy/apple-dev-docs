# string(for:)

**Framework**: Foundation  
**Kind**: method

Creates a formatted string for a date relative to the current date and time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func string(for obj: Any?) -> String?
```

#### Return Value

A string that represents the date interval between a date and the current date and time, or `nil` if obj isn’t an instance of [`NSDate`](nsdate.md).

#### Discussion

To determine the relative interval, the formatter uses [`date`](nsdate/date.md) as the reference date.

## Parameters

- `obj`: A date object to format.

## See Also

- [func localizedString(for: Date, relativeTo: Date) -> String](relativedatetimeformatter/localizedstring(for:relativeto:).md)
  Formats the date interval from the reference date to the specified date using the formatter’s calendar.
- [func localizedString(from: DateComponents) -> String](relativedatetimeformatter/localizedstring(from:).md)
  Formats a relative time represented by the specified date components.
- [func localizedString(fromTimeInterval: TimeInterval) -> String](relativedatetimeformatter/localizedstring(fromtimeinterval:).md)
  Formats the specified time interval using the formatter’s calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/string(for:))*