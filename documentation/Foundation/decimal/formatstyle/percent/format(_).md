# format(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Formats an decimal, using this style.

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
func format(_ value: Decimal) -> String
```

#### Return Value

A string representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple decimal. To format a single integer, use the 1414588 instance method [`formatted(_:)`](../../formatted%28_%29.md), passing in an instance of [`Decimal.FormatStyle.Percent`](../percent.md), or call [`formatted()`](../../formatted%28%29.md) to use a default style.

## Parameters

- `value`: The decimal to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/formatstyle/percent/format(_:))*