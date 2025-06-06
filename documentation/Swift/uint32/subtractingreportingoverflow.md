# subtractingReportingOverflow(_:)

**Framework**: Swift  
**Kind**: method

Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func subtractingReportingOverflow(_ other: UInt32) -> (partialValue: UInt32, overflow: Bool)
```

#### Return Value

A tuple containing the result of the subtraction along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire difference. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains the truncated result of `rhs` subtracted from this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint32/subtractingreportingoverflow(_:))*