# interactive(timingCurve:)

**Framework**: SwiftUI  
**Kind**: method

Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.

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
static func interactive(timingCurve: UnitCurve = .easeInOut) -> ScrollTransitionConfiguration
```

#### Return Value

A configuration that interactively interpolates between transition phases based on the current scroll position.

## Parameters

- `timingCurve`: The curve that adjusts the pace at which the effect   is interpolated between phases of the transition. For example, an    curve causes interpolation to begin slowly as the view   reaches the edge of the scroll view, then speed up as it reaches   the visible threshold. The curve is applied ‘forward’ while the   view is appearing, meaning that time zero corresponds to the   view being just hidden, and time 1.0 corresponds to the pont at   which the view reaches the configuration threshold. This also means   that the timing curve is applied in reversed while the view   is moving away from the center of the scroll view.

## See Also

- [static let identity: ScrollTransitionConfiguration](scrolltransitionconfiguration/identity.md)
  Creates a new configuration that does not change the appearance of the view.
- [static let animated: ScrollTransitionConfiguration](scrolltransitionconfiguration/animated.md)
  Creates a new configuration that discretely animates the transition when the view becomes visible.
- [static func animated(Animation) -> ScrollTransitionConfiguration](scrolltransitionconfiguration/animated(_:).md)
  Creates a new configuration that discretely animates the transition when the view becomes visible.
- [static let interactive: ScrollTransitionConfiguration](scrolltransitionconfiguration/interactive.md)
  Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/interactive(timingcurve:))*