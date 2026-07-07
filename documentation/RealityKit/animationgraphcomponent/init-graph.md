# init(graph:)

**Framework**: RealityKit  
**Kind**: init

Creates a component that drives skeletal animation on an entity using the supplied compiled animation graph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(graph: AnimationGraphResource)
```

#### Discussion

Per-instance evaluation state initializes when the entity becomes active in a scene, so accessors such as [`activeNodes`](animationgraphcomponent/activenodes.md) return an empty array until the first evaluation tick has run.

## Parameters

- `graph`: The compiled [`AnimationGraphResource`](animationgraphresource.md) that drives this component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/init(graph:))*