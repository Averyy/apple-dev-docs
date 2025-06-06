# named(_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a named coordinate space using the given value.

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
static func named(_ name: some Hashable) -> NamedCoordinateSpace
```

#### Return Value

A named coordinate space identified by the given value.

#### Discussion

Use the `coordinateSpace(_:)` modifier to assign a name to the local coordinate space of a  parent view. Child views can then refer to that coordinate space using `.named(_:)`.

## Parameters

- `name`: A unique value that identifies the coordinate space.

## See Also

- [static var immersiveSpace: NamedCoordinateSpace](coordinatespaceprotocol/immersivespace.md)
  The named coordinate space that represents the currently opened [`ImmersiveSpace`](immersivespace.md) scene. If no immersive space is currently opened, this CoordinateSpace provides the same behavior as the `.global` coordinate space.
- [static var global: GlobalCoordinateSpace](coordinatespaceprotocol/global.md)
  The global coordinate space at the root of the view hierarchy.
- [static var local: LocalCoordinateSpace](coordinatespaceprotocol/local.md)
  The local coordinate space of the current view.
- [static var scrollView: NamedCoordinateSpace](coordinatespaceprotocol/scrollview.md)
  The named coordinate space that is added by the system for the innermost containing scroll view.
- [static func scrollView(axis: Axis) -> Self](coordinatespaceprotocol/scrollview(axis:).md)
  The named coordinate space that is added by the system for the innermost containing scroll view that allows scrolling along the provided axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/coordinatespaceprotocol/named(_:))*