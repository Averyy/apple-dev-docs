# UIBandSelectionInteraction.State.possible

**Framework**: UIKit  
**Kind**: case

A state that indicates the interaction object is ready to start a new interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
case possible
```

#### Discussion

A [`UIBandSelectionInteraction`](uibandselectioninteraction.md) object in this state is waiting for events to occur that start the interaction. When an interaction concludes, the interaction returns to this state until a new interaction begins.

## See Also

- [UIBandSelectionInteraction.State.began](uibandselectioninteraction/state-swift.enum/began.md)
  A state that indicates the interaction object began a new interaction.
- [UIBandSelectionInteraction.State.selecting](uibandselectioninteraction/state-swift.enum/selecting.md)
  A state that indicates the interaction object is tracking changes to the selection rectangle.
- [UIBandSelectionInteraction.State.ended](uibandselectioninteraction/state-swift.enum/ended.md)
  A state that indicates the current interaction ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum/possible)*