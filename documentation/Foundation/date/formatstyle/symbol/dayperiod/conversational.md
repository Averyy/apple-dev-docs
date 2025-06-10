# conversational(_:)

**Framework**: Foundation  
**Kind**: method

Static factory method that creates a custom day period format style using a conversational style.

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
static func conversational(_ width: Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod
```

#### Return Value

A day period format style appropriate for the locale and specified width.

## Parameters

- `width`: Specifies the width of the string result.

## See Also

- [static func standard(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod/standard(_:).md)
  Static factory method that creates a custom day period format style using a standard style.
- [static func with12s(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod/with12s(_:).md)
  Static factory method that creates a custom day period format style using a style that represents midday and midnight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayperiod/conversational(_:))*