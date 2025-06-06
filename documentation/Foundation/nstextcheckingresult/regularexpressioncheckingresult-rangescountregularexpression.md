# regularExpressionCheckingResult(ranges:count:regularExpression:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a type checking result with the specified regular expression data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func regularExpressionCheckingResult(ranges: NSRangePointer, count: Int, regularExpression: NSRegularExpression) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`regularExpression`](nstextcheckingresult/checkingtype/regularexpression.md).

## Parameters

- `ranges`: A C array of ranges, which must have at least one element, and the first element represents the overall range.
- `count`: The number of items in the   array.
- `regularExpression`: The regular expression.

## See Also

- [var regularExpression: NSRegularExpression?](nstextcheckingresult/regularexpression.md)
  The regular expression of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/regularexpressioncheckingresult(ranges:count:regularexpression:))*