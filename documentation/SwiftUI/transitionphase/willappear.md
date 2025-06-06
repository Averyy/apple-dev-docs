# TransitionPhase.willAppear

**Framework**: SwiftUI  
**Kind**: case

The transition is being applied to a view that is about to be inserted into the view hierarchy.

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
case willAppear
```

#### Discussion

In this phase, a transition should show the appearance that will be animated from to make the appearance transition.

## See Also

- [TransitionPhase.identity](transitionphase/identity.md)
  The transition is being applied to a view that is in the view hierarchy.
- [TransitionPhase.didDisappear](transitionphase/diddisappear.md)
  The transition is being applied to a view that has been requested to be removed from the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transitionphase/willappear)*