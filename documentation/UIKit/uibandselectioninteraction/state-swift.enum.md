# UIBandSelectionInteraction.State

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIBandSelectionInteractionState : NSInteger;
```

## Overview

Use the [`UIBandSelectionInteraction.State`](./state-swift.enum.md) constants in the handler of a [`UIBandSelectionInteraction`](../uibandselectioninteraction.md) object to determine the current state of the interaction. When the interaction object is idle, it sets the state to [`UIBandSelectionInteraction.State.possible`](./state-swift.enum/possible.md). After the interaction starts, the state changes to other values to reflect the progress toward the completion of that interaction.

## Topics

### Getting the selection state
- [UIBandSelectionInteraction.State.possible](./state-swift.enum/possible.md)
  A state that indicates the interaction object is ready to start a new interaction.
- [UIBandSelectionInteraction.State.began](./state-swift.enum/began.md)
  A state that indicates the interaction object began a new interaction.
- [UIBandSelectionInteraction.State.selecting](./state-swift.enum/selecting.md)
  A state that indicates the interaction object is tracking changes to the selection rectangle.
- [UIBandSelectionInteraction.State.ended](./state-swift.enum/ended.md)
  A state that indicates the current interaction ended.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Band selection
- [class UIBandSelectionInteraction](../uibandselectioninteraction.md)
  An object that tracks the selection of multiple items using pointer-based input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.enum)*