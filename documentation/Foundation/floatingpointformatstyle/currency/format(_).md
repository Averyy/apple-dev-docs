# format(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Formats a floating-point value, using this style.

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

Available when `Value` conforms to `BinaryFloatingPoint`.

#### Return Value

A string representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple floating-point values. To format a single value, use the [`BinaryFloatingPoint`](../../../Swift/binaryfloatingpoint.md) instance method [`formatted(_:)`](../../../Swift/binaryfloatingpoint/formatted%28_%29-83x4n.md), passing in an instance of [`FloatingPointFormatStyle.Currency`](../currency.md).

## Parameters

- `value`: The floating-point value to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/currency/format(_:))*