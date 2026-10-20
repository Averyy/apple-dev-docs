# format(_:)

**Framework**: Foundation  
**Kind**: method

Creates a locale-aware string representation from a date value.

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

A string representation of the date.

#### Discussion

The [`format(_:)`](date/formatstyle/format(_:).md) instance method generates a string from the provided date. Once you create a style, you can use it to format dates multiple times.

The following example creates a format style to guide parsing a set of string representations of dates. It also creates a second format style, applying it repeatedly to produce more detailed string representations of those dates for a different locale.

```swift
let inputFormat = Date.FormatStyle()
    .locale(Locale(identifier: "en_GB"))
    .year()
    .month()
    .day()

// Parse dates from strings using the input format defined above.
let iphoneIntroductionDate = try! Date("9 Jan 2007", strategy: inputFormat)
let ipadIntroductionDate = try! Date("27 Jan 2010", strategy: inputFormat)
let wwdc2021Date = try! Date("7 Jun 2021", strategy: inputFormat)

// Define a format style with the desired date fields.
let outputFormat = Date.FormatStyle()
    .locale(Locale(identifier: "en_US"))
    .year()
    .month(.wide)
    .day(.twoDigits)
    .weekday(.abbreviated)

// Apply the output format on the three dates below.
print(outputFormat.format(wwdc2021Date))
// Mon, June 07, 2021

print(outputFormat.format(ipadIntroductionDate))
// Wed, January 27, 2010

print(outputFormat.format(iphoneIntroductionDate))
// Tue, January 09, 2007
```

## Parameters

- `value`: The date to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/format(_:))*