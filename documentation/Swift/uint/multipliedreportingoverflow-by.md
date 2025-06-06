# multipliedReportingOverflow(by:)

**Framework**: Swift  
**Kind**: method

Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.

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
func multipliedReportingOverflow(by other: UInt) -> (partialValue: UInt, overflow: Bool)
```

#### Return Value

A tuple containing the result of the multiplication along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire product. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains the truncated product of this value and `rhs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint/multipliedreportingoverflow(by:))*