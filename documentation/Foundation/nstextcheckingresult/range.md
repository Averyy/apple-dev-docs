# range

**Framework**: Foundation  
**Kind**: property

Returns the range of the result that the receiver represents.

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
var range: NSRange { get }
```

#### Discussion

This property will be present for all returned `NSTextCheckingResult` instances.

## See Also

- [var resultType: NSTextCheckingResult.CheckingType](nstextcheckingresult/resulttype.md)
  Returns the text checking result type that the receiver represents.
- [var numberOfRanges: Int](nstextcheckingresult/numberofranges.md)
  Returns the number of ranges.
- [func range(at: Int) -> NSRange](nstextcheckingresult/range(at:).md)
  Returns the result type that the range represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/range)*