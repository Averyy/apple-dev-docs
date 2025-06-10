# with12s(_:)

**Framework**: Foundation  
**Kind**: method

Static factory method that creates a custom day period format style using a style that represents midday and midnight.

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
static func with12s(_ width: Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod
```

#### Return Value

A day period format style appropriate for the locale and specified width.

## Parameters

- `width`: Specifies the width of the string result.

## See Also

- [static func conversational(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod/conversational(_:).md)
  Static factory method that creates a custom day period format style using a conversational style.
- [static func standard(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod/standard(_:).md)
  Static factory method that creates a custom day period format style using a standard style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayperiod/with12s(_:))*