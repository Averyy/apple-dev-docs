# immersiveSpace

**Framework**: SwiftUI  
**Kind**: property

The named coordinate space that represents the currently opened [`ImmersiveSpace`](immersivespace.md) scene. If no immersive space is currently opened, this CoordinateSpace provides the same behavior as the `.global` coordinate space.

**Availability**:
- visionOS 1.1+

## Declaration

```swift
static var immersiveSpace: NamedCoordinateSpace { get }
```

## See Also

- [static var global: GlobalCoordinateSpace](coordinatespaceprotocol/global.md)
  The global coordinate space at the root of the view hierarchy.
- [static var local: LocalCoordinateSpace](coordinatespaceprotocol/local.md)
  The local coordinate space of the current view.
- [static func named(some Hashable) -> NamedCoordinateSpace](coordinatespaceprotocol/named(_:).md)
  Creates a named coordinate space using the given value.
- [static var scrollView: NamedCoordinateSpace](coordinatespaceprotocol/scrollview.md)
  The named coordinate space that is added by the system for the innermost containing scroll view.
- [static func scrollView(axis: Axis) -> Self](coordinatespaceprotocol/scrollview(axis:).md)
  The named coordinate space that is added by the system for the innermost containing scroll view that allows scrolling along the provided axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/coordinatespaceprotocol/immersivespace)*