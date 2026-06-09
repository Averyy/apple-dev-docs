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

The [`parse(_:)`](date/formatstyle/parse(_:).md) instance method attempts to parse a provided string into an instance of date using the source date format style. The function throws an error if it can’t parse the input string into a date instance.

The date format style guides parsing the date instance from an input string, as the example below illustrates.

```swift
let birthdayFormatStyle = Date.FormatStyle()
    .year(.defaultDigits)
    .month(.abbreviated)
    .day(.twoDigits)
    .hour(.defaultDigits(amPM: .abbreviated))
    .minute(.twoDigits)
    .timeZone(.identifier(.long))
    .era(.abbreviated)
    .weekday(.abbreviated)

let yourBirthdayString = "Mon, Feb 17, 1997 AD, 1:27 AM America/Chicago"

// Create a date instance from a string representation of a date.
let yourBirthday = try? birthdayFormatStyle.parse(yourBirthdayString)
// Feb 17, 1997 at 1:27 AM

```

## Parameters

- `value`: The string to parse.

## See Also

- [var parseStrategy: Date.FormatStyle](date/formatstyle/parsestrategy.md)
  The strategy used to parse a string into a date.
- [struct ParseStrategy](date/parsestrategy.md)
  Options for parsing string representations of dates to create a `Date` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/parse(_:))*