# AnimationGraphResource

**Framework**: RealityKit  
**Kind**: class

A compiled animation graph resource that drives skeletal animation on an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class AnimationGraphResource
```

#### Overview

An `AnimationGraphResource` can be produced by compiling a JSON graph definition. Once compiled, assign it to an entity via [`AnimationGraphComponent`](animationgraphcomponent.md) to begin driving animation:

```swift
let resource = try AnimationGraphResource(definition: Data(animationGraphDefinition.utf8), nodeResourceMapping: clips, skeletonResource: skeleton)
entity.components.set(AnimationGraphComponent(graph: resource))
```

#### Parameters

The graph exposes a set of named parameters that control its behavior at runtime, such as movement speed or a trigger to initiate a transition. Read the available parameters via [`parameterNames`](animationgraphresource/parameternames.md). To set values at runtime, use the entity’s parameter binding:

```swift
entity.parameters["MoveSpeed"] = BindableValue(Float(1.0))
```

## Topics

### Creating an animation graph
- [convenience init(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) throws](animationgraphresource/init(definition:noderesourcemapping:skeletonresource:).md)
  Compile a new resource from data, throws on failure.
- [static func validate(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) -> [String]](animationgraphresource/validate(definition:noderesourcemapping:skeletonresource:).md)
  Run the compiler and return all graph errors without producing a resource.
### Accessing parameters
- [var parameterNames: [String]](animationgraphresource/parameternames.md)
  Returns the names of all parameters in the resource.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AnimationGraphComponent](animationgraphcomponent.md)
  A component that drives skeletal animation on an entity using a node-based animation graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphresource)*