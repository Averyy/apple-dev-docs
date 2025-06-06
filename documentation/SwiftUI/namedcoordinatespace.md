# NamedCoordinateSpace

**Framework**: SwiftUI  
**Kind**: struct

A named coordinate space.

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
struct NamedCoordinateSpace
```

#### Overview

Use the `coordinateSpace(_:)` modifier to assign a name to the local coordinate space of a  parent view. Child views can then refer to that coordinate space using `.named(_:)`.

## Relationships

### Conforms To
- [CoordinateSpaceProtocol](coordinatespaceprotocol.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct GlobalCoordinateSpace](globalcoordinatespace.md)
  The global coordinate space at the root of the view hierarchy.
- [struct LocalCoordinateSpace](localcoordinatespace.md)
  The local coordinate space of the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/namedcoordinatespace)*