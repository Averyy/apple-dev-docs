# ScrollPhase

**Framework**: SwiftUI  
**Kind**: enum

A type that describes the state of a scroll gesture of a scrollable view like a scroll view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
enum ScrollPhase
```

#### Overview

A scroll gesture can be in one of four phases: - idle: No active scroll is occurring. - panning: An active scroll being driven by the user is occurring. - decelerating: The user has stopped driving a scroll and the scroll view is decelerating to its final target. - animating: The system is animating to a final target as a result of a programmatic animated scroll from using a [`ScrollViewReader`](scrollviewreader.md) or [`scrollPosition(id:anchor:)`](view/scrollposition(id:anchor:).md) modifier.

SwiftUI provides you a value of this type when using the [`onScrollPhaseChange(_:)`](view/onscrollphasechange(_:).md) modifier.

## Topics

### Getting scroll gesture states
- [ScrollPhase.animating](scrollphase/animating.md)
  The animating phase where the scroll view is animating towards a final target.
- [ScrollPhase.decelerating](scrollphase/decelerating.md)
  The decelerating phase where the user use has stopped interacting with the scroll view and the scroll view is decelerating towards its final target.
- [ScrollPhase.idle](scrollphase/idle.md)
  The idle phase where no kind of scrolling is occurring.
- [ScrollPhase.interacting](scrollphase/interacting.md)
  The interacting phase where the user is interacting with the scroll view.
- [ScrollPhase.tracking](scrollphase/tracking.md)
  The tracking phase where the scroll view is tracking a potential scroll by the user but the user hasn’t started a scroll.
### Checking for active scrolling
- [var isScrolling: Bool](scrollphase/isscrolling.md)
  Whether the scroll view is actively scrolling.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](view/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](view/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](view/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onScrollPhaseChange(_:)](view/onscrollphasechange(_:).md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [struct ScrollGeometry](scrollgeometry.md)
  A type that defines the geometry of a scroll view.
- [struct ScrollPhaseChangeContext](scrollphasechangecontext.md)
  A type that provides you with more content when the phase of a scroll view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollphase)*