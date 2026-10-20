# global

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The global coordinate space at the root of the view hierarchy.

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
static var global: GlobalCoordinateSpace { get }
```

Available when `Self` is `GlobalCoordinateSpace`.

## See Also

### Getting built-in coordinate spaces
- [static var immersiveSpace: NamedCoordinateSpace](./immersivespace.md)
  The named coordinate space that represents the currently opened [`ImmersiveSpace`](../immersivespace.md) scene. If no immersive space is currently opened, this CoordinateSpace provides the same behavior as the `.global` coordinate space.
- [static var local: LocalCoordinateSpace](./local.md)
  The local coordinate space of the current view.
- [static func named(some Hashable) -> NamedCoordinateSpace](./named%28_%29.md)
  Creates a named coordinate space using the given value.
- [static var scrollView: NamedCoordinateSpace](./scrollview.md)
  The named coordinate space that is added by the system for the innermost containing scroll view.
- [static func scrollView(axis: Axis) -> Self](./scrollview%28axis%29.md)
  The named coordinate space that is added by the system for the innermost containing scroll view that allows scrolling along the provided axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/coordinatespaceprotocol/global)*