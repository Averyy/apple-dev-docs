# candidateListTouchBarItem(_:endSelectingCandidateAt:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that a user has stopped touching candidates in the candidate list item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func candidateListTouchBarItem(_ anItem: NSCandidateListTouchBarItem<AnyObject>, endSelectingCandidateAt index: Int)
```

#### Discussion

If `index` is equal to `NSNotFound` then the user didn’t select a candidate.

## Parameters

- `anItem`: The candidate list item that the user is interacting with.
- `index`: The index of the candidate that the user was touching when they lifted their finger.

## See Also

- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, beginSelectingCandidateAt: Int)](nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:beginselectingcandidateat:).md)
  Tells the delegate that the user has started touching one of the candidates in the candidate list item.
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, changeSelectionFromCandidateAt: Int, to: Int)](nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:changeselectionfromcandidateat:to:).md)
  Tells the delegate that user has moved from touching one candidate in the candidate list item to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:endselectingcandidateat:))*