# setCandidates(_:forSelectedRange:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets an array of candidate objects to be displayed in the candidate list bar item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func setCandidates(_ candidates: [CandidateType], forSelectedRange selectedRange: NSRange, in originalString: String?)
```

```objc
- (void) setCandidates:(NSArray<id> *) candidates forSelectedRange:(NSRange) selectedRange inString:(NSString *) originalString;
```

## Discussion

The item uses the block in the [`attributedStringForCandidate`](./attributedstringforcandidate.md) property to convert each candidate in the array into an attributed string. If the value of the [`attributedStringForCandidate`](./attributedstringforcandidate.md) property is `nil` then [`NSCandidateListTouchBarItem`](../nscandidatelisttouchbaritem.md) can format candidates of type [`NSString`](../../Foundation/nsstring.md), [`NSAttributedString`](../../Foundation/nsattributedstring.md), and [`NSTextCheckingResult`](../../Foundation/nstextcheckingresult.md).

## Parameters

- `candidates`: The array of candidates you wish to display in the candidate list item.
- `selectedRange`: A range ([`NSRange`](../../Foundation/nsrange-c.struct.md)) within the string that the candidates represent.
- `originalString`: The original string from which the candidate list was derived.

## See Also

### Populating the candidate list
- [var candidates: [CandidateType]](./candidates.md)
  The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](./setcandidates%28_,forselectedrange,in%29.md).
- [var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)?](./attributedstringforcandidate.md)
  A block that converts a candidate object into an attributed string for display in the candidate list item.
- [var allowsTextInputContextCandidates: Bool](./allowstextinputcontextcandidates.md)
  A Boolean value that specifies whether a candidate list item displays candidates from text input providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:))*