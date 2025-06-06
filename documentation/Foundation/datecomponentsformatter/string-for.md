# string(for:)

**Framework**: Foundation  
**Kind**: method

Returns a formatted string based on the date information in the specified object.

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
func string(for obj: Any?) -> String?
```

#### Return Value

A formatted string representing the specified date information.

#### Discussion

This method has the same behavior as the [`string(from:)`](datecomponentsformatter/string(from:)-9exxn.md) method.

## Parameters

- `obj`: An object containing the date and time information to format. The object in this parameter must be a   object; if it is not, the method raises an exception. This parameter must not be  .

## See Also

- [func string(from: DateComponents) -> String?](datecomponentsformatter/string(from:)-9exxn.md)
  Returns a formatted string based on the specified date component information.
- [func string(from: Date, to: Date) -> String?](datecomponentsformatter/string(from:to:).md)
  Returns a formatted string based on the time difference between two dates.
- [func string(from: TimeInterval) -> String?](datecomponentsformatter/string(from:)-7sj4j.md)
  Returns a formatted string based on the specified number of seconds.
- [class func localizedString(from: DateComponents, unitsStyle: DateComponentsFormatter.UnitsStyle) -> String?](datecomponentsformatter/localizedstring(from:unitsstyle:).md)
  Returns a localized string based on the specified date components and style option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/string(for:))*