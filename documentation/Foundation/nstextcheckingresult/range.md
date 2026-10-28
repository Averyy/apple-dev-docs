# range

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSRange range;
```

## Discussion

This property will be present for all returned `NSTextCheckingResult` instances.

## See Also

### Text Checking Type Range and Type
- [var resultType: NSTextCheckingResult.CheckingType](./resulttype.md)
  Returns the text checking result type that the receiver represents.
- [var numberOfRanges: Int](./numberofranges.md)
  Returns the number of ranges.
- [func range(at: Int) -> NSRange](./range%28at%29.md)
  Returns the result type that the range represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/range)*