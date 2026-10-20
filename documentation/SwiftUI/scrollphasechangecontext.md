# ScrollPhaseChangeContext

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A type that provides you with more content when the phase of a scroll view changes.

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
struct ScrollPhaseChangeContext
```

#### Overview

You don’t create this type directly. Instead, SwiftUI provides an instance of this type in the [`onScrollPhaseChange(_:)`](./view/onscrollphasechange%28_%29.md) modifier.

## Topics

### Instance Properties
- [var geometry: ScrollGeometry](./scrollphasechangecontext/geometry.md)
  The geometry of the scroll view at the time of the scroll phase change.
- [var velocity: CGVector?](./scrollphasechangecontext/velocity.md)
  The velocity of the scroll view at the time of the scroll phase change.

## See Also

### Responding to scroll view changes
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](./view/onscrollgeometrychange%28for,of,action%29.md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](./view/onscrolltargetvisibilitychange%28idtype,threshold,_%29.md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](./view/onscrollvisibilitychange%28threshold,_%29.md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onScrollPhaseChange(_:)](./view/onscrollphasechange%28_%29.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [struct ScrollGeometry](./scrollgeometry.md)
  A type that defines the geometry of a scroll view.
- [enum ScrollPhase](./scrollphase.md)
  A type that describes the state of a scroll gesture of a scrollable view like a scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollphasechangecontext)*