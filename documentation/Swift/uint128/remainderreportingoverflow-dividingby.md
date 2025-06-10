# remainderReportingOverflow(dividingBy:)

**Framework**: Swift  
**Kind**: method

Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.

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
func remainderReportingOverflow(dividingBy other: UInt128) -> (partialValue: UInt128, overflow: Bool)
```

#### Return Value

A tuple containing the result of the operation along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire remainder. If the `overflow` component is `true`, an overflow occurred during division and the `partialValue` component contains either the entire remainder or, if the remainder is undefined, the dividend.

#### Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.remainderReportingOverflow(dividingBy: 0)` is `(x, true)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/remainderreportingoverflow(dividingby:))*