# init(definition:nodeResourceMapping:skeletonResource:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Compiles an animation graph definition into a resource that can drive animation on an entity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
convenience init(definition: Data, nodeResourceMapping: [Int : AnimationResource] = [:], skeletonResource: SkeletonResource) throws
```

## Discussion

To validate a definition without producing a resource — for example, when surfacing errors in editor tooling — call [`validate(definition:nodeResourceMapping:skeletonResource:)`](./validate%28definition,noderesourcemapping,skeletonresource%29.md) instead.

> **Throws**: An error if the compiler couldn’t produce a resource from the definition. The thrown error carries every diagnostic the compiler reported.

## Parameters

- `definition`: The animation graph definition to compile.
- `nodeResourceMapping`: A mapping from graph-node IDs to the [`AnimationResource`](../animationresource.md) clips those nodes reference. Defaults to empty.
- `skeletonResource`: The [`SkeletonResource`](../skeletonresource.md) the graph targets.

## See Also

### Creating an animation graph
- [static func validate(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) -> [String]](./validate%28definition,noderesourcemapping,skeletonresource%29.md)
  Compiles an animation graph definition and returns any diagnostic messages the compiler produced, without producing a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphresource/init(definition:noderesourcemapping:skeletonresource:))*