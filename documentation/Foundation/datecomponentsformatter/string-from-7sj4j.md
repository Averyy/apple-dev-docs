# string(from:)

**Framework**: Foundation  
**Kind**: method

Returns a formatted string based on the specified number of seconds.

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
func string(from ti: TimeInterval) -> String?
```

#### Return Value

A formatted string representing the specified time interval.

#### Discussion

This method formats the specified number of seconds into the appropriate units. For example, if the formatter allows the display of minutes and seconds, creating an abbreviated string for the value 70 seconds results in the string “1m 10s”.

## Parameters

- `ti`: The time interval, measured in seconds. The value must be a finite number. Negative numbers are treated as positive numbers when creating the string.

## See Also

- [func string(from: DateComponents) -> String?](datecomponentsformatter/string(from:)-9exxn.md)
  Returns a formatted string based on the specified date component information.
- [func string(for: Any?) -> String?](datecomponentsformatter/string(for:).md)
  Returns a formatted string based on the date information in the specified object.
- [func string(from: Date, to: Date) -> String?](datecomponentsformatter/string(from:to:).md)
  Returns a formatted string based on the time difference between two dates.
- [class func localizedString(from: DateComponents, unitsStyle: DateComponentsFormatter.UnitsStyle) -> String?](datecomponentsformatter/localizedstring(from:unitsstyle:).md)
  Returns a localized string based on the specified date components and style option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(from:)-7sj4j)*