# candidates

**Framework**: AppKit  
**Kind**: property

The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md).

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var candidates: [CandidateType] { get }
```

## See Also

- [func setCandidates([CandidateType], forSelectedRange: NSRange, in: String?)](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md)
  Sets an array of candidate objects to be displayed in the candidate list bar item.
- [var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)?](nscandidatelisttouchbaritem/attributedstringforcandidate.md)
  A block that converts a candidate object into an attributed string for display in the candidate list item.
- [var allowsTextInputContextCandidates: Bool](nscandidatelisttouchbaritem/allowstextinputcontextcandidates.md)
  A Boolean value that specifies whether a candidate list item displays candidates from text input providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/candidates)*