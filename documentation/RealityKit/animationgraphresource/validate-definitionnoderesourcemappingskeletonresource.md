# validate(definition:nodeResourceMapping:skeletonResource:)

**Framework**: RealityKit  
**Kind**: method

Compiles an animation graph definition and returns any diagnostic messages the compiler produced, without producing a resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func validate(definition: Data, nodeResourceMapping: [Int : AnimationResource] = [:], skeletonResource: SkeletonResource) -> [String]
```

#### Return Value

An array of diagnostic messages produced by the compiler. An empty array indicates the definition compiled cleanly.

#### Discussion

Call this method to validate a definition at editor time without paying the cost of holding on to the compiled resource and without having to handle a thrown error. To produce a usable [`AnimationGraphResource`](animationgraphresource.md), call [`init(definition:nodeResourceMapping:skeletonResource:)`](animationgraphresource/init(definition:noderesourcemapping:skeletonresource:).md) instead.

## Parameters

- `definition`: The animation graph definition to validate.
- `nodeResourceMapping`: A mapping from graph-node IDs to the [`AnimationResource`](animationresource.md) clips those nodes reference. Defaults to empty.
- `skeletonResource`: The [`SkeletonResource`](skeletonresource.md) the graph targets.

## See Also

- [convenience init(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) throws](animationgraphresource/init(definition:noderesourcemapping:skeletonresource:).md)
  Compiles an animation graph definition into a resource that can drive animation on an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphresource/validate(definition:noderesourcemapping:skeletonresource:))*