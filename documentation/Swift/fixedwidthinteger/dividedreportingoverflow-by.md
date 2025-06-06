# dividedReportingOverflow(by:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

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
func dividedReportingOverflow(by rhs: Self) -> (partialValue: Self, overflow: Bool)
```

#### Return Value

A tuple containing the result of the division along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire quotient. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains either the truncated quotient or, if the quotient is undefined, the dividend.

#### Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.dividedReportingOverflow(by: 0)` is `(x, true)`.

## Parameters

- `rhs`: The value to divide this value by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/fixedwidthinteger/dividedreportingoverflow(by:))*