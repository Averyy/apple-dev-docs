# init(definition:nodeResourceMapping:skeletonResource:)

**Framework**: RealityKit  
**Kind**: init

Compiles an animation graph definition into a resource that can drive animation on an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(definition: Data, nodeResourceMapping: [Int : AnimationResource] = [:], skeletonResource: SkeletonResource) throws
```

#### Discussion

To validate a definition without producing a resource — for example, when surfacing errors in editor tooling — call [`validate(definition:nodeResourceMapping:skeletonResource:)`](animationgraphresource/validate(definition:noderesourcemapping:skeletonresource:).md) instead.

> **Note**: An error if the compiler couldn’t produce a resource from the definition. The thrown error carries every diagnostic the compiler reported.

## Parameters

- `definition`: The animation graph definition to compile.
- `nodeResourceMapping`: A mapping from graph-node IDs to the [`AnimationResource`](animationresource.md) clips those nodes reference. Defaults to empty.
- `skeletonResource`: The [`SkeletonResource`](skeletonresource.md) the graph targets.

## See Also

- [static func validate(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) -> [String]](animationgraphresource/validate(definition:noderesourcemapping:skeletonresource:).md)
  Compiles an animation graph definition and returns any diagnostic messages the compiler produced, without producing a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphresource/init(definition:noderesourcemapping:skeletonresource:))*