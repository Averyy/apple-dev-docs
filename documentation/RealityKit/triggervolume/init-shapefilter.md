# init(shape:filter:)

**Framework**: RealityKit  
**Kind**: init

Creates a trigger volume with the given shape and collision filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(shape: ShapeResource, filter: CollisionFilter = .sensor)
```

## Parameters

- `shape`: The shape of the trigger volume.
- `filter`: A collision filter that lets you differentiate among collision   groups.

## See Also

- [init()](triggervolume/init.md)
  Creates a trigger volume.
- [init(shapes: [ShapeResource], filter: CollisionFilter)](triggervolume/init(shapes:filter:).md)
  Creates a trigger volume with the given composite shape and collision filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/triggervolume/init(shape:filter:))*