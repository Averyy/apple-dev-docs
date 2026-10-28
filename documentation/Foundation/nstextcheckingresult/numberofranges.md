# numberOfRanges

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the number of ranges.

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
var numberOfRanges: Int { get }
```

```objc
@property (readonly) NSUInteger numberOfRanges;
```

## Discussion

A result must have at least one range, but may optionally have more (for example, to represent regular expression capture groups).

Passing [`range(at:)`](./range%28at%29.md) the value `0` always returns the value of the the [`range`](./range.md) property.  Additional ranges, if any, will have indexes from `1` to `numberOfRanges``-1`.

## See Also

### Text Checking Type Range and Type
- [var range: NSRange](./range.md)
  Returns the range of the result that the receiver represents.
- [var resultType: NSTextCheckingResult.CheckingType](./resulttype.md)
  Returns the text checking result type that the receiver represents.
- [func range(at: Int) -> NSRange](./range%28at%29.md)
  Returns the result type that the range represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/numberofranges)*