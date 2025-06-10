# ScrollTransitionPhase

**Framework**: SwiftUI  
**Kind**: enum

The phases that a view transitions between when it scrolls among other views.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@frozen
enum ScrollTransitionPhase
```

#### Overview

When a view with a scroll transition modifier applied is approaching the visible region of the containing scroll view or other container, the effect  will first be applied with the `topLeading` or `bottomTrailing` phase (depending on which edge the view is approaching), then will be moved to the `identity` phase as the view moves into the visible area. The timing and behavior that determines when a view is visible within the container is controlled by the configuration that is provided to the `scrollTransition` modifier.

In the `identity` phase, scroll transitions should generally not make any visual change to the view they are applied to, since the transition’s view modifications in the `identity` phase will be applied to the view as long as it is visible. In the `topLeading` and `bottomTrailing` phases, transitions should apply a change that will be animated to create the transition.

## Topics

### Getting the phase
- [ScrollTransitionPhase.identity](scrolltransitionphase/identity.md)
  The scroll transition is being applied to a view that is in the visible area.
- [ScrollTransitionPhase.topLeading](scrolltransitionphase/topleading.md)
  The scroll transition is being applied to a view that is about to move into the visible area at the top edge of a vertical scroll view, or the leading edge of a horizont scroll view.
- [ScrollTransitionPhase.bottomTrailing](scrolltransitionphase/bottomtrailing.md)
  The scroll transition is being applied to a view that is about to move into the visible area at the bottom edge of a vertical scroll view, or the trailing edge of a horizontal scroll view.
### Accessing the phase state
- [var isIdentity: Bool](scrolltransitionphase/isidentity.md)
- [var value: Double](scrolltransitionphase/value.md)
  A phase-derived value that can be used to scale or otherwise modify effects.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](view/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](view/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [struct ScrollTransitionConfiguration](scrolltransitionconfiguration.md)
  The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionphase)*