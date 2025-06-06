# string(from:timeZone:formatOptions:)

**Framework**: Foundation  
**Kind**: method

Creates a representation of the specified date with a given time zone and format options.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func string(from date: Date, timeZone: TimeZone, formatOptions: ISO8601DateFormatter.Options = []) -> String
```

#### Return Value

A user-readable string representing the date.

#### Discussion

This method uses a date formatter configured with the specified time zone and format options. The following code examples produce the same string value:

## Parameters

- `date`: The date to be represented.
- `timeZone`: The time zone used.
- `formatOptions`: The options used. For possible values, see  .

## See Also

- [func string(from: Date) -> String](iso8601dateformatter/string(from:).md)
  Creates and returns an ISO 8601 formatted string representation of the specified date.
- [func date(from: String) -> Date?](iso8601dateformatter/date(from:).md)
  Creates and returns a date object from the specified ISO 8601 formatted string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/iso8601dateformatter/string(from:timezone:formatoptions:))*