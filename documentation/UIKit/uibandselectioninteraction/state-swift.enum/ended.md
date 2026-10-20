# UIBandSelectionInteraction.State.ended

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A state that indicates the current interaction ended.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
case ended
```

```c
UIBandSelectionInteractionStateEnded
```

#### Discussion

Use this state to finalize the interaction. For example, you might finalize the selection of items in your view.

## See Also

### Getting the selection state
- [UIBandSelectionInteraction.State.possible](./possible.md)
  A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteraction.State.began](./began.md)
  A state that indicates the interaction object began a new interaction.
- [UIBandSelectionInteraction.State.selecting](./selecting.md)
  A state that indicates the interaction object is tracking changes to the selection rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum/ended)*