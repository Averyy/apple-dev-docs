# EntityTargetValue

**Framework**: RealityKit  
**Kind**: struct

A value containing an original gesture value along with a targeted entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@dynamicMemberLookup
struct EntityTargetValue<Value>
```

#### Overview

Spatial data from a [`location`](https://developer.apple.com/documentation/SwiftUI/DragGesture/Value/location) returned by a gesture can be converted to and from the entity using functions defined in [`RealityCoordinateSpaceConverting`](realitycoordinatespaceconverting.md).

For example, here’s how to convert [`location`](https://developer.apple.com/documentation/SwiftUI/DragGesture/Value/location) from a [`DragGesture`](https://developer.apple.com/documentation/SwiftUI/DragGesture) to the parent of an [`Entity`](entity.md):

```swift
DragGesture(coordinateSpace: .global).targetedToEntity().updating($state) { state, value, _ in
    let location = value.convert(
        value.location, from: .global, to: value.entity.parent
    )
    ...
}
```

## Topics

### Accessing gesture info
- [var entity: Entity](entitytargetvalue/entity.md)
  The targeted entity.
- [var gestureValue: Value](entitytargetvalue/gesturevalue.md)
  The gesture value updated by the gesture.
- [subscript<T>(dynamicMember _: KeyPath<Value, T>) -> T](entitytargetvalue/subscript(dynamicmember:).md)
### Instance Methods
- [func unproject(CGPoint, from: some CoordinateSpaceProtocol, to: some RealityCoordinateSpace) -> SIMD3<Float>?](entitytargetvalue/unproject(_:from:to:).md)
  Unproject `point` from a 2D coordinate space into 3D world coordinates.
- [func unproject(KeyPath<Value, CGPoint>, to: some RealityCoordinateSpace) -> SIMD3<Float>?](entitytargetvalue/unproject(_:to:).md)
  Unproject a 2D point from the gesture value into 3D world coordinates.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [RealityCoordinateSpaceConverting](realitycoordinatespaceconverting.md)
- [RealityCoordinateSpaceProjecting](realitycoordinatespaceprojecting.md)

## See Also

- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [struct InputTargetComponent](inputtargetcomponent.md)
  A component that gives an entity the ability to receive system input.
- [struct ManipulationComponent](manipulationcomponent.md)
  A component that adds fluid and immersive interactive behaviors and effects.
- [struct GestureComponent](gesturecomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitytargetvalue)*