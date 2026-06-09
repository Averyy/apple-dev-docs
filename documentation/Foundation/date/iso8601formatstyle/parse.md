# parse(_:)

**Framework**: Foundation  
**Kind**: method

Parses a string into a date.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func parse(_ value: String) throws -> Date
```

#### Return Value

An instance of `Date` parsed from the input string.

#### Discussion

This method attempts to parse a provided string into an instance of date using the source date format style. The function throws an error if it can’t parse the input string into a date instance.

The date format style guides parsing the date instance from an input string, as the following example illustrates.

```swift
let birthdayFormatStyle = Date.ISO8601FormatStyle()    
    .dateSeparator(.dash)
    .timeSeparator(.colon)
    .year()
    .month()
    .day()
    .time(includingFractionalSeconds: false)

// Create a date instance from a string representation of a date.
let yourBirthdayString = "2021-02-17T14:33:25"
let yourBirthday = try? birthdayFormatStyle.parse(yourBirthdayString)
// Feb 17, 2021 at 8:33 AM
```

## Parameters

- `value`: The string to parse.

## See Also

- [var parseStrategy: Date.ISO8601FormatStyle](date/iso8601formatstyle/parsestrategy.md)
  The strategy used to parse a string into a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/parse(_:))*