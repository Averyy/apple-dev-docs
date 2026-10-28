# allowsTextInputContextCandidates

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether a candidate list item displays candidates from text input providers.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var allowsTextInputContextCandidates: Bool { get set }
```

```objc
@property BOOL allowsTextInputContextCandidates;
```

## Discussion

When [`true`](../../Swift/true.md), the candidate list item shows candidates from the text input client provided in the [`client`](./client.md) property, before those in the [`candidates`](./candidates.md) property.

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Populating the candidate list
- [func setCandidates([CandidateType], forSelectedRange: NSRange, in: String?)](./setcandidates%28_,forselectedrange,in%29.md)
  Sets an array of candidate objects to be displayed in the candidate list bar item.
- [var candidates: [CandidateType]](./candidates.md)
  The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](./setcandidates%28_,forselectedrange,in%29.md).
- [var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)?](./attributedstringforcandidate.md)
  A block that converts a candidate object into an attributed string for display in the candidate list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/allowstextinputcontextcandidates)*