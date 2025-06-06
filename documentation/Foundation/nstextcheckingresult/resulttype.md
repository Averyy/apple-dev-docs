# resultType

**Framework**: Foundation  
**Kind**: property

Returns the text checking result type that the receiver represents.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var resultType: NSTextCheckingResult.CheckingType { get }
```

#### Discussion

The possible result types for the built in checking capabilities are described in [`NSTextCheckingResult.CheckingType`](nstextcheckingresult/checkingtype.md).

This property will be present for all returned `NSTextCheckingResult` instances.

## See Also

- [var range: NSRange](nstextcheckingresult/range.md)
  Returns the range of the result that the receiver represents.
- [var numberOfRanges: Int](nstextcheckingresult/numberofranges.md)
  Returns the number of ranges.
- [func range(at: Int) -> NSRange](nstextcheckingresult/range(at:).md)
  Returns the result type that the range represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/resulttype)*