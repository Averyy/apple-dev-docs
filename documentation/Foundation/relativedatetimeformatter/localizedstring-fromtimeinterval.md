# localizedString(fromTimeInterval:)

**Framework**: Foundation  
**Kind**: method

Formats the specified time interval using the formatter’s calendar.

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
func localizedString(fromTimeInterval timeInterval: TimeInterval) -> String
```

#### Return Value

A string that represents the formatted time interval.

#### Discussion

The formatter interprets a negative time interval as a date in the past.

```swift
let formatter = RelativeDateTimeFormatter()
print(formatter.localizedString(fromTimeInterval: -120))
// Outputs:  2 minutes ago
```

## Parameters

- `timeInterval`: The time interval to format.

## See Also

- [func localizedString(for: Date, relativeTo: Date) -> String](relativedatetimeformatter/localizedstring(for:relativeto:).md)
  Formats the date interval from the reference date to the specified date using the formatter’s calendar.
- [func localizedString(from: DateComponents) -> String](relativedatetimeformatter/localizedstring(from:).md)
  Formats a relative time represented by the specified date components.
- [func string(for: Any?) -> String?](relativedatetimeformatter/string(for:).md)
  Creates a formatted string for a date relative to the current date and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/localizedstring(fromtimeinterval:))*