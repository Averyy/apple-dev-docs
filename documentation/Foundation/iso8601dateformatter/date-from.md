# date(from:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a date object from the specified ISO 8601 formatted string representation.

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
func date(from string: String) -> Date?
```

#### Return Value

A date object, or `nil` if no valid date was found.

## Parameters

- `string`: The ISO 8601 formatted string representation of a date.

## See Also

- [func string(from: Date) -> String](iso8601dateformatter/string(from:).md)
  Creates and returns an ISO 8601 formatted string representation of the specified date.
- [class func string(from: Date, timeZone: TimeZone, formatOptions: ISO8601DateFormatter.Options) -> String](iso8601dateformatter/string(from:timezone:formatoptions:).md)
  Creates a representation of the specified date with a given time zone and format options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/iso8601dateformatter/date(from:))*