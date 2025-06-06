# localizedString(from:unitsStyle:)

**Framework**: Foundation  
**Kind**: method

Returns a localized string based on the specified date components and style option.

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
class func localizedString(from components: DateComponents, unitsStyle: DateComponentsFormatter.UnitsStyle) -> String?
```

#### Return Value

A string containing the localized date and time information.

#### Discussion

Use this convenience method to format a string using the default formatter values, with the exception of the `unitsStyle` value.

## Parameters

- `components`: The value to format.
- `unitsStyle`: The style for the resulting units. Use this parameter to specify whether you want to the resulting string to use an abbreviated or more spelled out format.

## See Also

- [func string(from: DateComponents) -> String?](datecomponentsformatter/string(from:)-9exxn.md)
  Returns a formatted string based on the specified date component information.
- [func string(for: Any?) -> String?](datecomponentsformatter/string(for:).md)
  Returns a formatted string based on the date information in the specified object.
- [func string(from: Date, to: Date) -> String?](datecomponentsformatter/string(from:to:).md)
  Returns a formatted string based on the time difference between two dates.
- [func string(from: TimeInterval) -> String?](datecomponentsformatter/string(from:)-7sj4j.md)
  Returns a formatted string based on the specified number of seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/localizedstring(from:unitsstyle:))*