# AnimationGraphResource

**Framework**: RealityKit  
**Kind**: class

A compiled animation graph that drives skeletal animation on an entity by blending and transitioning between animation clips at runtime.

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

Compile an animation graph definition once into an [`AnimationGraphResource`](animationgraphresource.md), then attach it to one or more entities through [`AnimationGraphComponent`](animationgraphcomponent.md). The same resource can drive many entities — each [`AnimationGraphComponent`](animationgraphcomponent.md) keeps its own per-instance evaluation state, so animation timing, state-machine progress, and parameter values stay independent across characters that share a graph.

##### Compile and Attach a Graph

```swift
let resource = try AnimationGraphResource(
    definition: graphDefinition,
    nodeResourceMapping: clips,
    skeletonResource: skeleton
)
entity.components.set(AnimationGraphComponent(graph: resource))
```

##### Drive the Graph with Parameters

A graph exposes a set of named, typed parameters that control its behavior at runtime, such as a movement speed or a trigger that initiates a transition. List the parameters declared by the graph through [`parameterNames`](animationgraphresource/parameternames.md). Set values through the owning entity’s parameter binding rather than through the resource itself:

```swift
entity.parameters["MoveSpeed"] = BindableValue(Float(1.0))
```

When the graph evaluates next, it picks up the values bound on the entity whose names and types match the graph’s declared parameters.

##### Validate Before Compiling

To check a graph definition for errors without producing a resource — for example, in editor tooling — call [`validate(definition:nodeResourceMapping:skeletonResource:)`](animationgraphresource/validate(definition:noderesourcemapping:skeletonresource:).md), which returns compiler diagnostics rather than throwing.

## Topics

### Creating an animation graph
- [convenience init(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) throws](animationgraphresource/init(definition:noderesourcemapping:skeletonresource:).md)
  Compiles an animation graph definition into a resource that can drive animation on an entity.
- [static func validate(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) -> [String]](animationgraphresource/validate(definition:noderesourcemapping:skeletonresource:).md)
  Compiles an animation graph definition and returns any diagnostic messages the compiler produced, without producing a resource.
### Accessing parameters
- [var parameterNames: [String]](animationgraphresource/parameternames.md)
  The names of all parameters declared by the graph definition.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AnimationGraphComponent](animationgraphcomponent.md)
  A component that drives skeletal animation on an entity using an animation graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphresource)*