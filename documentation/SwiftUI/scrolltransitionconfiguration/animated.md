# animated(_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a new configuration that discretely animates the transition when the view becomes visible.

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
static func animated(_ animation: Animation = .default) -> ScrollTransitionConfiguration
```

#### Return Value

A configuration that discretely animates between transition phases.

#### Discussion

Unlike the interactive configuration, the transition isn’t interpolated as the scroll view is scrolled. Instead, the transition phase only changes once the threshold has been reached, at which time the given animation is used to animate to the new phase.

## Parameters

- `animation`: The animation to use when transitioning between states.

## See Also

- [static let identity: ScrollTransitionConfiguration](scrolltransitionconfiguration/identity.md)
  Creates a new configuration that does not change the appearance of the view.
- [static let animated: ScrollTransitionConfiguration](scrolltransitionconfiguration/animated.md)
  Creates a new configuration that discretely animates the transition when the view becomes visible.
- [static let interactive: ScrollTransitionConfiguration](scrolltransitionconfiguration/interactive.md)
  Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.
- [static func interactive(timingCurve: UnitCurve) -> ScrollTransitionConfiguration](scrolltransitionconfiguration/interactive(timingcurve:).md)
  Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/animated(_:))*