# allowsTextInputContextCandidates

**Framework**: AppKit  
**Kind**: property

A Boolean value that specifies whether a candidate list item displays candidates from text input providers.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var allowsTextInputContextCandidates: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/swift/true), the candidate list item shows candidates from the text input client provided in the [`client`](nscandidatelisttouchbaritem/client.md) property, before those in the [`candidates`](nscandidatelisttouchbaritem/candidates.md) property.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func setCandidates([CandidateType], forSelectedRange: NSRange, in: String?)](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md)
  Sets an array of candidate objects to be displayed in the candidate list bar item.
- [var candidates: [CandidateType]](nscandidatelisttouchbaritem/candidates.md)
  The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md).
- [var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)?](nscandidatelisttouchbaritem/attributedstringforcandidate.md)
  A block that converts a candidate object into an attributed string for display in the candidate list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/allowstextinputcontextcandidates)*