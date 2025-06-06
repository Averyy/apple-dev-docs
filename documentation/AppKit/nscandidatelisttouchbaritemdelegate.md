# NSCandidateListTouchBarItemDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that a candidate list item delegate uses to enable selection state and list visibility.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSCandidateListTouchBarItemDelegate : NSObjectProtocol
```

## Topics

### Handling selection changes
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, beginSelectingCandidateAt: Int)](nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:beginselectingcandidateat:).md)
  Tells the delegate that the user has started touching one of the candidates in the candidate list item.
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, changeSelectionFromCandidateAt: Int, to: Int)](nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:changeselectionfromcandidateat:to:).md)
  Tells the delegate that user has moved from touching one candidate in the candidate list item to another.
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, endSelectingCandidateAt: Int)](nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:endselectingcandidateat:).md)
  Tells the delegate that a user has stopped touching candidates in the candidate list item.
### Handling visibility changes
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, changedCandidateListVisibility: Bool)](nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:changedcandidatelistvisibility:).md)
  Tells the delegate that the visibility of the candidate list has changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTextView](nstextview.md)

## See Also

- [var client: (any NSView & NSTextInputClient)?](nscandidatelisttouchbaritem/client.md)
  The client object for the candidate list item.
- [var delegate: (any NSCandidateListTouchBarItemDelegate)?](nscandidatelisttouchbaritem/delegate.md)
  The delegate of the candidate list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritemdelegate)*