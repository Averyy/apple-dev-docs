# remainderReportingOverflow(dividingBy:)

**Framework**: Swift  
**Kind**: method

Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.

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
func remainderReportingOverflow(dividingBy other: UInt16) -> (partialValue: UInt16, overflow: Bool)
```

#### Return Value

A tuple containing the result of the operation along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire remainder. If the `overflow` component is `true`, an overflow occurred during division and the `partialValue` component contains either the entire remainder or, if the remainder is undefined, the dividend.

#### Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.remainderReportingOverflow(dividingBy: 0)` is `(x, true)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint16/remainderreportingoverflow(dividingby:))*