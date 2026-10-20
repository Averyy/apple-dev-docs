# UIPageControl.InteractionState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that define the interaction states of the page control.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum InteractionState
```

```c
enum UIPageControlInteractionState : NSInteger;
```

## Topics

### Constants
- [UIPageControl.InteractionState.none](./interactionstate-swift.enum/none.md)
  The default interaction state, where no interaction has occurred.
- [UIPageControl.InteractionState.discrete](./interactionstate-swift.enum/discrete.md)
  The interaction state for which the page changes through a single, discrete interaction.
- [UIPageControl.InteractionState.continuous](./interactionstate-swift.enum/continuous.md)
  The interaction state for which the page changes through a continuous interaction.
### Initializers
- [init?(rawValue: Int)](./interactionstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing the interaction state
- [var allowsContinuousInteraction: Bool](./allowscontinuousinteraction.md)
  A Boolean value that determines whether the page control allows continuous interaction.
- [var interactionState: UIPageControl.InteractionState](./interactionstate-swift.property.md)
  The interaction state when the current page changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/interactionstate-swift.enum)*