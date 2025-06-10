# localizedString(from:)

**Framework**: Foundation  
**Kind**: method

Formats a relative time represented by the specified date components.

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
func localizedString(from dateComponents: DateComponents) -> String
```

#### Return Value

A string that represents the formatted relative time from date components.

#### Discussion

The formatter interprets a negative component value as a date in the past.

```swift
let components = DateComponents(day: -2)
let formatter = RelativeDateTimeFormatter()
print(formatter.localizedString(from: components))
// Outputs:  2 days ago
```

This method formats the value of the least granular unit in the [`NSDateComponents`](nsdatecomponents.md) object, and doesn’t provide a compound format of the date component.

> ❗ **Important**:  This method only supports year, month, week of month, day, hour, minute, and second components. The formatter ignores all other date components.

## Parameters

- `dateComponents`: The date components to format.

## See Also

- [func localizedString(for: Date, relativeTo: Date) -> String](relativedatetimeformatter/localizedstring(for:relativeto:).md)
  Formats the date interval from the reference date to the specified date using the formatter’s calendar.
- [func localizedString(fromTimeInterval: TimeInterval) -> String](relativedatetimeformatter/localizedstring(fromtimeinterval:).md)
  Formats the specified time interval using the formatter’s calendar.
- [func string(for: Any?) -> String?](relativedatetimeformatter/string(for:).md)
  Creates a formatted string for a date relative to the current date and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/localizedstring(from:))*