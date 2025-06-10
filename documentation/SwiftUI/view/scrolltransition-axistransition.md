# scrollTransition(_:axis:transition:)

**Framework**: SwiftUI  
**Kind**: method

Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.

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
nonisolated
func scrollTransition(_ configuration: ScrollTransitionConfiguration = .interactive, axis: Axis? = nil, transition: @escaping (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View
```

## Parameters

- `configuration`: The configuration controlling how the   transition will be applied. The configuration will be applied both   while the view is coming into view and while it is disappearing (the   transition is symmetrical).
- `axis`: The axis of the containing scroll view over which the   transition will be applied. The default value of   uses the   axis of the innermost containing scroll view, or   if   the innermost scroll view is scrollable along both axes.
- `transition`: A closure that applies visual effects as a function of   the provided phase.

## See Also

- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](view/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [enum ScrollTransitionPhase](scrolltransitionphase.md)
  The phases that a view transitions between when it scrolls among other views.
- [struct ScrollTransitionConfiguration](scrolltransitionconfiguration.md)
  The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolltransition(_:axis:transition:))*