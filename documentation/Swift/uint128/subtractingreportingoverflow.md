# subtractingReportingOverflow(_:)

**Framework**: Swift  
**Kind**: method

Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func subtractingReportingOverflow(_ other: UInt128) -> (partialValue: UInt128, overflow: Bool)
```

#### Return Value

A tuple containing the result of the subtraction along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire difference. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains the truncated result of `rhs` subtracted from this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/subtractingreportingoverflow(_:))*