# format(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Formats an integer, using this style.

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
func format(_ value: Value) -> String
```

Available when `Value` conforms to `BinaryInteger`.

## Return Value

A string representation of `value`, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple integers. To format a single integer, use the [`BinaryInteger`](../../../Swift/binaryinteger.md) instance method [`formatted(_:)`](../../../Swift/binaryinteger/formatted%28_%29-4qd73.md), passing in an instance of [`IntegerFormatStyle.Percent`](../percent.md), or [`formatted()`](../../../Swift/binaryinteger/formatted%28%29.md) to use a default style.

## Parameters

- `value`: The integer to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/percent/format(_:))*