# scrollTransition(topLeading:bottomTrailing:axis:transition:)

**Framework**: RealityKit  
**Kind**: method

Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis? = nil, transition: @escaping (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View
```

## Parameters

- `transition`: The transition to apply.
- `topLeading`: The configuration that drives the transition when   the view is about to appear at the top edge of a vertical   scroll view, or the leading edge of a horizont scroll view.
- `bottomTrailing`: The configuration that drives the transition when   the view is about to appear at the bottom edge of a vertical   scroll view, or the trailing edge of a horizont scroll view.
- `axis`: The axis of the containing scroll view over which the   transition will be applied. The default value of   uses the   axis of the innermost containing scroll view, or   if   the innermost scroll view is scrollable along both axes.
- `transition`: A closure that applies visual effects as a function of   the provided phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/scrolltransition(topleading:bottomtrailing:axis:transition:))*