# ScrollTransitionPhase.identity

**Framework**: SwiftUI  
**Kind**: case

The scroll transition is being applied to a view that is in the visible area.

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
case identity
```

#### Discussion

In this phase, a transition should show its steady state appearance, which will generally not make any visual change to the view.

## See Also

- [ScrollTransitionPhase.topLeading](scrolltransitionphase/topleading.md)
  The scroll transition is being applied to a view that is about to move into the visible area at the top edge of a vertical scroll view, or the leading edge of a horizont scroll view.
- [ScrollTransitionPhase.bottomTrailing](scrolltransitionphase/bottomtrailing.md)
  The scroll transition is being applied to a view that is about to move into the visible area at the bottom edge of a vertical scroll view, or the trailing edge of a horizontal scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltransitionphase/identity)*