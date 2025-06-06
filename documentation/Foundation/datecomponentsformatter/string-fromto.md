# string(from:to:)

**Framework**: Foundation  
**Kind**: method

Returns a formatted string based on the time difference between two dates.

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
func string(from startDate: Date, to endDate: Date) -> String?
```

#### Return Value

A formatted string representing the specified time information.

#### Discussion

This method calculates the elapsed time between the `startDate` and `endDate` values and uses that information to generate the string. For example, if there is exactly one hour and ten minutes difference between the start and end dates, generating an abbreviated string would result in a string of “1h 10m”.

## Parameters

- `startDate`: The start time. This parameter must not be  .
- `endDate`: The end time. This parameter must not be  .

## See Also

- [func string(from: DateComponents) -> String?](datecomponentsformatter/string(from:)-9exxn.md)
  Returns a formatted string based on the specified date component information.
- [func string(for: Any?) -> String?](datecomponentsformatter/string(for:).md)
  Returns a formatted string based on the date information in the specified object.
- [func string(from: TimeInterval) -> String?](datecomponentsformatter/string(from:)-7sj4j.md)
  Returns a formatted string based on the specified number of seconds.
- [class func localizedString(from: DateComponents, unitsStyle: DateComponentsFormatter.UnitsStyle) -> String?](datecomponentsformatter/localizedstring(from:unitsstyle:).md)
  Returns a localized string based on the specified date components and style option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(from:to:))*