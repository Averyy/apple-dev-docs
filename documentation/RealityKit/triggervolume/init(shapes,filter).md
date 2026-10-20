# init(shapes:filter:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a trigger volume with the given composite shape and collision filter.

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
@preconcurrency init(shapes: [ShapeResource], filter: CollisionFilter = .sensor)
```

## Parameters

- `shapes`: A collection of shapes which taken together define the composite shape of the trigger volume.
- `filter`: A collision filter that lets you differentiate among collision groups.

## See Also

### Creating a trigger volume
- [init()](./init%28%29.md)
  Creates a trigger volume.
- [convenience init(shape: ShapeResource, filter: CollisionFilter)](./init%28shape,filter%29.md)
  Creates a trigger volume with the given shape and collision filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/triggervolume/init(shapes:filter:))*