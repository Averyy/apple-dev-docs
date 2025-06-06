# UIBandSelectionInteraction.State

**Framework**: UIKit  
**Kind**: enum

Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
enum State
```

#### Overview

Use the [`UIBandSelectionInteraction.State`](uibandselectioninteraction/state-swift.enum.md) constants in the handler of a [`UIBandSelectionInteraction`](uibandselectioninteraction.md) object to determine the current state of the interaction. When the interaction object is idle, it sets the state to [`UIBandSelectionInteraction.State.possible`](uibandselectioninteraction/state-swift.enum/possible.md). After the interaction starts, the state changes to other values to reflect the progress toward the completion of that interaction.

## Topics

### Getting the selection state
- [UIBandSelectionInteraction.State.possible](uibandselectioninteraction/state-swift.enum/possible.md)
  A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteraction.State.began](uibandselectioninteraction/state-swift.enum/began.md)
  A state that indicates the interaction object began a new interaction.
- [UIBandSelectionInteraction.State.selecting](uibandselectioninteraction/state-swift.enum/selecting.md)
  A state that indicates the interaction object is tracking changes to the selection rectangle.
- [UIBandSelectionInteraction.State.ended](uibandselectioninteraction/state-swift.enum/ended.md)
  A state that indicates the current interaction ended.
### Initializers
- [init?(rawValue: Int)](uibandselectioninteraction/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIBandSelectionInteraction](uibandselectioninteraction.md)
  An object that tracks the selection of multiple items using pointer-based input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum)*