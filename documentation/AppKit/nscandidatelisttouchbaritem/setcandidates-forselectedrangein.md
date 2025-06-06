# setCandidates(_:forSelectedRange:in:)

**Framework**: AppKit  
**Kind**: method

Sets an array of candidate objects to be displayed in the candidate list bar item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func setCandidates(_ candidates: [CandidateType], forSelectedRange selectedRange: NSRange, in originalString: String?)
```

#### Discussion

The item uses the block in the [`attributedStringForCandidate`](nscandidatelisttouchbaritem/attributedstringforcandidate.md) property to convert each candidate in the array into an attributed string. If the value of the [`attributedStringForCandidate`](nscandidatelisttouchbaritem/attributedstringforcandidate.md) property is `nil` then [`NSCandidateListTouchBarItem`](nscandidatelisttouchbaritem.md) can format candidates of type [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString), and [`NSTextCheckingResult`](https://developer.apple.com/documentation/Foundation/NSTextCheckingResult).

## Parameters

- `candidates`: The array of candidates you wish to display in the candidate list item.
- `selectedRange`: A range ( ) within the string that the candidates represent.
- `originalString`: The original string from which the candidate list was derived.

## See Also

- [var candidates: [CandidateType]](nscandidatelisttouchbaritem/candidates.md)
  The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md).
- [var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)?](nscandidatelisttouchbaritem/attributedstringforcandidate.md)
  A block that converts a candidate object into an attributed string for display in the candidate list item.
- [var allowsTextInputContextCandidates: Bool](nscandidatelisttouchbaritem/allowstextinputcontextcandidates.md)
  A Boolean value that specifies whether a candidate list item displays candidates from text input providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:))*