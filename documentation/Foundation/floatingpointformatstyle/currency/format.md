# format(_:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

A string representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple floating-point values. To format a single value, use the [`BinaryFloatingPoint`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint) instance method [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryFloatingPoint/formatted(_:)-83x4n), passing in an instance of [`FloatingPointFormatStyle.Currency`](floatingpointformatstyle/currency.md).

## Parameters

- `value`: The floating-point value to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/currency/format(_:))*