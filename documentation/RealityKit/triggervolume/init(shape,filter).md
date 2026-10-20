# init(shape:filter:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a trigger volume with the given shape and collision filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency convenience init(shape: ShapeResource, filter: CollisionFilter = .sensor)
```

## Parameters

- `shape`: The shape of the trigger volume.
- `filter`: A collision filter that lets you differentiate among collision groups.

## See Also

### Creating a trigger volume
- [init()](./init%28%29.md)
  Creates a trigger volume.
- [init(shapes: [ShapeResource], filter: CollisionFilter)](./init%28shapes,filter%29.md)
  Creates a trigger volume with the given composite shape and collision filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/triggervolume/init(shape:filter:))*