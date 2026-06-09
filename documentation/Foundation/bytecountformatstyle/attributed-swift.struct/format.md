# format(_:)

**Framework**: Foundation  
**Kind**: method

Formats a numeric byte count, using this style.

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
func format(_ value: Int64) -> AttributedString
```

#### Return Value

A formatted representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values. To format a single integer, use the [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger) instance method [`formatted(_:)`](https://developer.apple.com/documentation/Swift/BinaryInteger/formatted(_:)-4qd73), passing in an instance of [`ByteCountFormatStyle.Attributed`](bytecountformatstyle/attributed-swift.struct.md), or [`formatted()`](https://developer.apple.com/documentation/Swift/BinaryInteger/formatted()) to use a default style.

## Parameters

- `value`: The 64-bit byte count to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/attributed-swift.struct/format(_:))*