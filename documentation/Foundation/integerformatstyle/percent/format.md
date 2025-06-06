# format(_:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

A string representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple integers. To format a single integer, use the [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger) instance method [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryInteger/formatted(_:)-4qd73), passing in an instance of [`IntegerFormatStyle.Percent`](integerformatstyle/percent.md), or [`formatted()`](https://developer.apple.com/documentation/Swift/BinaryInteger/formatted()) to use a default style.

## Parameters

- `value`: The integer to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/integerformatstyle/percent/format(_:))*