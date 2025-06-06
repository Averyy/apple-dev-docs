# scrollTransition(topLeading:bottomTrailing:axis:transition:)

**Framework**: SwiftUI  
**Kind**: method

Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.

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
func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis? = nil, transition: @escaping (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View
```

## Parameters

- `topLeading`: The configuration that drives the transition when   the view is about to appear at the top edge of a vertical   scroll view, or the leading edge of a horizont scroll view.
- `bottomTrailing`: The configuration that drives the transition when   the view is about to appear at the bottom edge of a vertical   scroll view, or the trailing edge of a horizont scroll view.
- `axis`: The axis of the containing scroll view over which the   transition will be applied. The default value of   uses the   axis of the innermost containing scroll view, or   if   the innermost scroll view is scrollable along both axes.
- `transition`: The transition to apply.

## See Also

- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](view/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.
- [enum ScrollTransitionPhase](scrolltransitionphase.md)
  The phases that a view transitions between when it scrolls among other views.
- [struct ScrollTransitionConfiguration](scrolltransitionconfiguration.md)
  The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolltransition(topleading:bottomtrailing:axis:transition:))*