# UIPageControl.InteractionState

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### Constants
- [UIPageControl.InteractionState.none](uipagecontrol/interactionstate-swift.enum/none.md)
  The default interaction state, where no interaction has occurred.
- [UIPageControl.InteractionState.discrete](uipagecontrol/interactionstate-swift.enum/discrete.md)
  The interaction state for which the page changes through a single, discrete interaction.
- [UIPageControl.InteractionState.continuous](uipagecontrol/interactionstate-swift.enum/continuous.md)
  The interaction state for which the page changes through a continuous interaction.
### Initializers
- [init?(rawValue: Int)](uipagecontrol/interactionstate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var allowsContinuousInteraction: Bool](uipagecontrol/allowscontinuousinteraction.md)
  A Boolean value that determines whether the page control allows continuous interaction.
- [var interactionState: UIPageControl.InteractionState](uipagecontrol/interactionstate-swift.property.md)
  The interaction state when the current page changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/interactionstate-swift.enum)*