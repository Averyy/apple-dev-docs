# NSCandidateListTouchBarItemDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that a candidate list item delegate uses to enable selection state and list visibility.

**Availability**:
- macOS

## Declaration

```swift
protocol NSCandidateListTouchBarItemDelegate : NSObjectProtocol
```

```objc
@protocol NSCandidateListTouchBarItemDelegate <NSObject>
```

## Topics

### Handling selection changes
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, beginSelectingCandidateAt: Int)](./nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem%28_,beginselectingcandidateat%29.md)
  Tells the delegate that the user has started touching one of the candidates in the candidate list item.
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, changeSelectionFromCandidateAt: Int, to: Int)](./nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem%28_,changeselectionfromcandidateat,to%29.md)
  Tells the delegate that user has moved from touching one candidate in the candidate list item to another.
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, endSelectingCandidateAt: Int)](./nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem%28_,endselectingcandidateat%29.md)
  Tells the delegate that a user has stopped touching candidates in the candidate list item.
### Handling visibility changes
- [func candidateListTouchBarItem(NSCandidateListTouchBarItem<AnyObject>, changedCandidateListVisibility: Bool)](./nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem%28_,changedcandidatelistvisibility%29.md)
  Tells the delegate that the visibility of the candidate list has changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSTextView](./nstextview.md)

## See Also

### Providing a client and a delegate
- [var client: (any NSView & NSTextInputClient)?](./nscandidatelisttouchbaritem/client.md)
  The client object for the candidate list item.
- [var delegate: (any NSCandidateListTouchBarItemDelegate)?](./nscandidatelisttouchbaritem/delegate.md)
  The delegate of the candidate list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritemdelegate)*