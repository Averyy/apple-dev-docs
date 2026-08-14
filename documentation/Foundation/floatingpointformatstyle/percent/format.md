# format(_:)

**Framework**: Foundation  
**Kind**: method

Formats an floating-point value, using this style.

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

Use this method when you want to create a single style instance, and then use it to format multiple floating-point values. To format a single floating-point value, use the [`BinaryFloatingPoint`](https://developer.apple.com/documentation/swift/binaryfloatingpoint) instance method [`formatted(_:)`](https://developer.apple.com/documentation/swift/binaryfloatingpoint/formatted(_:)-83x4n), passing in an instance of [`FloatingPointFormatStyle.Percent`](floatingpointformatstyle/percent.md), or call [`formatted()`](https://developer.apple.com/documentation/swift/binaryfloatingpoint/formatted()) to use a default style.

## Parameters

- `value`: The floating-point value to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/percent/format(_:))*