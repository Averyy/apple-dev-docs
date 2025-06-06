# ScrollGeometry

**Framework**: SwiftUI  
**Kind**: struct

A type that defines the geometry of a scroll view.

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
struct ScrollGeometry
```

#### Overview

SwiftUI provides you values of this type when using modifiers like `View/onScrollGeometryChange(_:action:)` or [`onScrollPhaseChange(_:)`](view/onscrollphasechange(_:).md).

## Topics

### Initializers
- [init(contentOffset: CGPoint, contentSize: CGSize, contentInsets: EdgeInsets, containerSize: CGSize)](scrollgeometry/init(contentoffset:contentsize:contentinsets:containersize:).md)
  Creates a scroll geometry.
### Instance Properties
- [var bounds: CGRect](scrollgeometry/bounds.md)
  The bounds rect of the scroll view.
- [var containerSize: CGSize](scrollgeometry/containersize.md)
  The size of the container of the scroll view.
- [var contentInsets: EdgeInsets](scrollgeometry/contentinsets.md)
  The content insets of the scroll view.
- [var contentOffset: CGPoint](scrollgeometry/contentoffset.md)
  The content offset of the scroll view.
- [var contentSize: CGSize](scrollgeometry/contentsize.md)
  The size of the content of the scroll view.
- [var visibleRect: CGRect](scrollgeometry/visiblerect.md)
  The visible rect of the scroll view.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](view/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](view/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](view/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onScrollPhaseChange(_:)](view/onscrollphasechange(_:).md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [enum ScrollPhase](scrollphase.md)
  A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
- [struct ScrollPhaseChangeContext](scrollphasechangecontext.md)
  A type that provides you with more content when the phase of a scroll view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollgeometry)*