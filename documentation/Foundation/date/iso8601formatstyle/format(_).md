# format(_:)

**Framework**: Foundation  
**Kind**: method

Creates a locale-aware ISO 8601 string representation from a date value.

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
func format(_ value: Date) -> String
```

#### Return Value

A string ISO 8601 representation of the date.

#### Discussion

The [`format(_:)`](date/iso8601formatstyle/format(_:).md) instance method generates a ISO 8601 formatted string from the provided date. Once you create a style, you can use it to format dates multiple times.

In the following example, a format style is created to guide parsing a set of string representations of dates. Another format style is created and applied repeatedly to produce customized ISO 8601 string representations of those dates for a different locale.

```swift
let input8601Format = Date.ISO8601FormatStyle()
    .dateSeparator(.dash)
    .year()
    .month()
    .day()

// Parse dates from strings using the input format defined above.
let introDate01 = try? Date("2007-01-09", strategy: input8601Format)
let introDate02 = try? Date("2010-01-27", strategy: input8601Format)
let meetingDate2021 = try? Date("2021-06-07", strategy: input8601Format)

let outputFormat = Date.ISO8601FormatStyle() // define format style for string output
    .locale(Locale(identifier: "en_US"))
    .year()
    .month()
    .day()
    .weekOfYear()

// Apply the output format to the three dates below.
if let meet2021 = meetingDate2021 {
    print(outputFormat.format(meet2021))
}
// 202106W2301
if let intro02 = introDate02 {
    print(outputFormat.format(intro02))
}
// 201001W0403
if let intro01 = introDate01 {
    print(outputFormat.format(intro01))
}
// 200701W0202
```

## Parameters

- `value`: The date to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/format(_:))*