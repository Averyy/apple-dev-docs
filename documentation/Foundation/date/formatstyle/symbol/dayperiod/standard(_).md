# standard(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Static factory method that creates a custom day period format style using a standard style.

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
static func standard(_ width: Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod
```

## Return Value

A day period format style appropriate for the locale and specified width.

## Parameters

- `width`: Specifies the width of the string result.

## See Also

### Modifying a Day Period
- [static func conversational(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](./conversational%28_%29.md)
  Static factory method that creates a custom day period format style using a conversational style.
- [static func with12s(Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod](./with12s%28_%29.md)
  Static factory method that creates a custom day period format style using a style that represents midday and midnight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayperiod/standard(_:))*