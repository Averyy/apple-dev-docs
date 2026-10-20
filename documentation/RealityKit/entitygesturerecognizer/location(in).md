# location(in:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the unprojected location of the gesture represented by the receiver in the space of the given entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency func location(in entity: Entity?) -> SIMD3<Float>?
```

#### Return Value

The 3D position identifying the location of the gesture in the space specified.

#### Discussion

The location is typically the result of a centroid of touches for a gesture, unprojected onto the associated `entity`, and then converted into the space of the entity passed in, or world space if `nil` is passed in.

## Parameters

- `entity`: An entity in whose space the location is computed. A `nil` entity will result in world space.

## Default Implementations

### EntityGestureRecognizer Implementations
- [func location(in: Entity?) -> SIMD3<Float>?](./location%28in%29-2aecy.md)
  Returns the unprojected location of the gesture represented by the receiver in the space of the given entity.

## See Also

### Using the gesture recognizer
- [var entity: (any HasCollision)?](./entity.md)
  The entity the receiver is associated with


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitygesturerecognizer/location(in:))*