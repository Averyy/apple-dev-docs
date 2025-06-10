# dividedReportingOverflow(by:)

**Framework**: Swift  
**Kind**: method

Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.

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
func dividedReportingOverflow(by other: Int128) -> (partialValue: Int128, overflow: Bool)
```

#### Return Value

A tuple containing the result of the division along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire quotient. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains either the truncated quotient or, if the quotient is undefined, the dividend.

#### Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.dividedReportingOverflow(by: 0)` is `(x, true)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/dividedreportingoverflow(by:))*