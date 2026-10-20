# dividedReportingOverflow(by:)

**Framework**: Swift  
**Kind**: method

Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.

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
func dividedReportingOverflow(by other: Int) -> (partialValue: Int, overflow: Bool)
```

#### Return Value

A tuple containing the result of the division along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire quotient. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains either the truncated quotient or, if the quotient is undefined, the dividend.

#### Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.dividedReportingOverflow(by: 0)` is `(x, true)`.

## See Also

- [func addingReportingOverflow(Int) -> (partialValue: Int, overflow: Bool)](int/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func subtractingReportingOverflow(Int) -> (partialValue: Int, overflow: Bool)](int/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func multipliedReportingOverflow(by: Int) -> (partialValue: Int, overflow: Bool)](int/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: Int) -> (partialValue: Int, overflow: Bool)](int/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/dividedreportingoverflow(by:))*