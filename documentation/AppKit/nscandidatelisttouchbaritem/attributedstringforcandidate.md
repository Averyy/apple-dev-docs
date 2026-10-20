# attributedStringForCandidate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A block that converts a candidate object into an attributed string for display in the candidate list item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)? { get set }
```

```objc
@property (copy, nullable) NSAttributedString *(^)(id, long) attributedStringForCandidate;
```

#### Discussion

This property is not required if the object type of your candidates is [`NSString`](../../Foundation/nsstring.md), [`NSAttributedString`](../../Foundation/nsattributedstring.md), or [`NSTextCheckingResult`](../../Foundation/nstextcheckingresult.md). The default value of this property is `nil`.

If the attributed string you return does not specify [`font`](../../Foundation/nsattributedstring/key/font.md) or [`foregroundColor`](../../Foundation/nsattributedstring/key/foregroundcolor.md) then the candidate is displayed with the standard appearance font and color.

## See Also

### Populating the candidate list
- [func setCandidates([CandidateType], forSelectedRange: NSRange, in: String?)](./setcandidates%28_,forselectedrange,in%29.md)
  Sets an array of candidate objects to be displayed in the candidate list bar item.
- [var candidates: [CandidateType]](./candidates.md)
  The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](./setcandidates%28_,forselectedrange,in%29.md).
- [var allowsTextInputContextCandidates: Bool](./allowstextinputcontextcandidates.md)
  A Boolean value that specifies whether a candidate list item displays candidates from text input providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/attributedstringforcandidate)*