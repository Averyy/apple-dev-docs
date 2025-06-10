# date(from:)

**Framework**: Foundation  
**Kind**: method

Returns a date representation of a specified string that the system interprets using the receiver’s current settings.

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
func date(from string: String) -> Date?
```

#### Return Value

A date representation of `string`. If [`date(from:)`](dateformatter/date(from:).md) can’t parse the string, returns `nil`.

#### Discussion

For more information about using [`DateFormatter`](dateformatter.md) to convert a string to a date, see [`Working With Fixed Format Date Representations`](dateformatter#Working-With-Fixed-Format-Date-Representations.md). For a sample code playground, see [`Displaying Human-Friendly Content`](displaying_human-friendly_content.md).

## Parameters

- `string`: The string to parse.

## See Also

- [func string(from: Date) -> String](dateformatter/string(from:).md)
  Returns a string representation of a specified date that the system formats using the receiver’s current settings.
- [class func localizedString(from: Date, dateStyle: DateFormatter.Style, timeStyle: DateFormatter.Style) -> String](dateformatter/localizedstring(from:datestyle:timestyle:).md)
  Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](dateformatter/getobjectvalue(_:for:range:).md)
  Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/date(from:))*