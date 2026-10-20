# UIBandSelectionInteraction.State.began

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A state that indicates the interaction object began a new interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
case began
```

```c
UIBandSelectionInteractionStateBegan
```

#### Discussion

The interaction object enters this state once at the beginning of each interaction, and subsequently transitions to the [`UIBandSelectionInteraction.State.selecting`](./selecting.md) or [`UIBandSelectionInteraction.State.ended`](./ended.md) state. When in this state, perform any one-time tasks that you need to manage your app’s state. For example, you might prepare your view to start the selection of items.

## See Also

### Getting the selection state
- [UIBandSelectionInteraction.State.possible](./possible.md)
  A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteraction.State.selecting](./selecting.md)
  A state that indicates the interaction object is tracking changes to the selection rectangle.
- [UIBandSelectionInteraction.State.ended](./ended.md)
  A state that indicates the current interaction ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum/began)*