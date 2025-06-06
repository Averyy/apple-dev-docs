# range(at:)

**Framework**: Foundation  
**Kind**: method

Returns the result type that the range represents.

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
func range(at idx: Int) -> NSRange
```

#### Return Value

The range of the result.

#### Discussion

A result must have at least one range, but may optionally have more, for example, to represent regular expression capture groups.

Passing [`range(at:)`](nstextcheckingresult/range(at:).md) the value `0` always returns the value of the [`range`](nstextcheckingresult/range.md) property. Additional ranges, if any, will have indexes from `1` to `numberOfRanges``-1`.

## Parameters

- `idx`: The index of the result.

## See Also

- [var range: NSRange](nstextcheckingresult/range.md)
  Returns the range of the result that the receiver represents.
- [var resultType: NSTextCheckingResult.CheckingType](nstextcheckingresult/resulttype.md)
  Returns the text checking result type that the receiver represents.
- [var numberOfRanges: Int](nstextcheckingresult/numberofranges.md)
  Returns the number of ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/range(at:))*