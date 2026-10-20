# candidates

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](./setcandidates%28_,forselectedrange,in%29.md).

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var candidates: [CandidateType] { get }
```

```objc
@property (copy, readonly) NSArray<id> * candidates;
```

## See Also

### Populating the candidate list
- [func setCandidates([CandidateType], forSelectedRange: NSRange, in: String?)](./setcandidates%28_,forselectedrange,in%29.md)
  Sets an array of candidate objects to be displayed in the candidate list bar item.
- [var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)?](./attributedstringforcandidate.md)
  A block that converts a candidate object into an attributed string for display in the candidate list item.
- [var allowsTextInputContextCandidates: Bool](./allowstextinputcontextcandidates.md)
  A Boolean value that specifies whether a candidate list item displays candidates from text input providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/candidates)*