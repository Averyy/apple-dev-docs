# interactive

**Framework**: SwiftUI  
**Kind**: property

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
static let interactive: ScrollTransitionConfiguration
```

## See Also

- [static let identity: ScrollTransitionConfiguration](scrolltransitionconfiguration/identity.md)
  Creates a new configuration that does not change the appearance of the view.
- [static let animated: ScrollTransitionConfiguration](scrolltransitionconfiguration/animated.md)
  Creates a new configuration that discretely animates the transition when the view becomes visible.
- [static func animated(Animation) -> ScrollTransitionConfiguration](scrolltransitionconfiguration/animated(_:).md)
  Creates a new configuration that discretely animates the transition when the view becomes visible.
- [static func interactive(timingCurve: UnitCurve) -> ScrollTransitionConfiguration](scrolltransitionconfiguration/interactive(timingcurve:).md)
  Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/interactive)*