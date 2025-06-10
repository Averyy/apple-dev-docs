# attributedStringForCandidate

**Framework**: AppKit  
**Kind**: property

A block that converts a candidate object into an attributed string for display in the candidate list item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)? { get set }
```

#### Discussion

This property is not required if the object type of your candidates is [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString), or [`NSTextCheckingResult`](https://developer.apple.com/documentation/Foundation/NSTextCheckingResult). The default value of this property is `nil`.

If the attributed string you return does not specify [`font`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/font) or [`foregroundColor`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/foregroundColor) then the candidate is displayed with the standard appearance font and color.

## See Also

- [func setCandidates([CandidateType], forSelectedRange: NSRange, in: String?)](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md)
  Sets an array of candidate objects to be displayed in the candidate list bar item.
- [var candidates: [CandidateType]](nscandidatelisttouchbaritem/candidates.md)
  The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md).
- [var allowsTextInputContextCandidates: Bool](nscandidatelisttouchbaritem/allowstextinputcontextcandidates.md)
  A Boolean value that specifies whether a candidate list item displays candidates from text input providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/attributedstringforcandidate)*