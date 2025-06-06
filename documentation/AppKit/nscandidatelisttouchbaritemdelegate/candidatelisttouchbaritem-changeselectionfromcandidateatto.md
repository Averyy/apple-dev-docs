# candidateListTouchBarItem(_:changeSelectionFromCandidateAt:to:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that user has moved from touching one candidate in the candidate list item to another.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func candidateListTouchBarItem(_ anItem: NSCandidateListTouchBarItem<AnyObject>, changeSelectionFromCandidateAt previousIndex: Int, to index: Int)
```

## Parameters

- `anItem`: The candidate list item that the user is interacting with.
- `previousIndex`: The index of the candidate that the user was previously touching.
- `index`: The index of the candidate that the user is currently touching.

## See Also

- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, beginSelectingCandidateAt: Int)](nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:beginselectingcandidateat:).md)
  Tells the delegate that the user has started touching one of the candidates in the candidate list item.
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, endSelectingCandidateAt: Int)](nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:endselectingcandidateat:).md)
  Tells the delegate that a user has stopped touching candidates in the candidate list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:changeselectionfromcandidateat:to:))*