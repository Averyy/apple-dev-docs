# candidateListTouchBarItem(_:beginSelectingCandidateAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user has started touching one of the candidates in the candidate list item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func candidateListTouchBarItem(_ anItem: NSCandidateListTouchBarItem<AnyObject>, beginSelectingCandidateAt index: Int)
```

```objc
- (void) candidateListTouchBarItem:(NSCandidateListTouchBarItem *) anItem beginSelectingCandidateAtIndex:(NSInteger) index;
```

## Parameters

- `anItem`: The candidate list bar item that the user is interacting with.
- `index`: The index of the candidate that the user is currently touching.

## See Also

### Handling selection changes
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, changeSelectionFromCandidateAt: Int, to: Int)](./candidatelisttouchbaritem%28_,changeselectionfromcandidateat,to%29.md)
  Tells the delegate that user has moved from touching one candidate in the candidate list item to another.
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, endSelectingCandidateAt: Int)](./candidatelisttouchbaritem%28_,endselectingcandidateat%29.md)
  Tells the delegate that a user has stopped touching candidates in the candidate list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:beginselectingcandidateat:))*