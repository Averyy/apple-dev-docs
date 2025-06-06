# UIBandSelectionInteraction.State.began

**Framework**: UIKit  
**Kind**: case

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

#### Discussion

The interaction object enters this state once at the beginning of each interaction, and subsequently transitions to the [`UIBandSelectionInteraction.State.selecting`](uibandselectioninteraction/state-swift.enum/selecting.md) or [`UIBandSelectionInteraction.State.ended`](uibandselectioninteraction/state-swift.enum/ended.md) state. When in this state, perform any one-time tasks that you need to manage your app’s state. For example, you might prepare your view to start the selection of items.

## See Also

- [UIBandSelectionInteraction.State.possible](uibandselectioninteraction/state-swift.enum/possible.md)
  A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteraction.State.selecting](uibandselectioninteraction/state-swift.enum/selecting.md)
  A state that indicates the interaction object is tracking changes to the selection rectangle.
- [UIBandSelectionInteraction.State.ended](uibandselectioninteraction/state-swift.enum/ended.md)
  A state that indicates the current interaction ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum/began)*