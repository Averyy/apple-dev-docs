# string(from:)

**Framework**: Foundation  
**Kind**: method

Returns a string representation of a specified date that the system formats using the receiver’s current settings.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func string(from date: Date) -> String
```

#### Return Value

A string representation of `date`.

#### Discussion

For more information about using [`DateFormatter`](dateformatter.md) to produce a string representation of a date, see [`Working With User-Visible Representations of Dates and Times`](dateformatter#Working-With-User-Visible-Representations-of-Dates-and-Times.md). For a sample code playground, see [`Displaying Human-Friendly Content`](formatter/displaying_human-friendly_content.md).

## Parameters

- `date`: The date to format.

## See Also

- [func date(from: String) -> Date?](dateformatter/date(from:).md)
  Returns a date representation of a specified string that the system interprets using the receiver’s current settings.
- [class func localizedString(from: Date, dateStyle: DateFormatter.Style, timeStyle: DateFormatter.Style) -> String](dateformatter/localizedstring(from:datestyle:timestyle:).md)
  Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](dateformatter/getobjectvalue(_:for:range:).md)
  Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/string(from:))*