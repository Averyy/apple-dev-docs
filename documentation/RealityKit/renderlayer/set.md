# RenderLayer.Set

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An unordered collection of unique render layers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Set
```

#### Overview

[`RenderLayer.Set`](./set.md) represents a group of layers - for example, the layers a light illuminates ([`layers`](../directionallightcomponent/layers.md), [`layers`](../pointlightcomponent/layers.md), [`layers`](../spotlightcomponent/layers.md)) or the layers an entity participates in ([`layers`](../renderlayercomponent/layers.md)).

Create a [`RenderLayer.Set`](./set.md) using an array literal:

```swift
let layers: RenderLayer.Set = [.defaultLayer, RenderLayer("com.myapp.hero")]
```

## Topics

### Inspecting the set
- [var count: Int](./set/count.md)
  The number of layers in the set.
- [var isEmpty: Bool](./set/isempty.md)
  A Boolean value indicating whether the set contains no layers.
- [func contains(RenderLayer) -> Bool](./set/contains%28_%29.md)
  Returns a Boolean value indicating whether the set contains the given layer.
### Initializers
- [init()](./set/init%28%29.md)
  Creates an empty set of render layers.
- [init<S>(S)](./set/init%28_%29.md)
  Creates a set of render layers from a sequence.
### Instance Methods
- [func insert(RenderLayer) -> (inserted: Bool, memberAfterInsert: RenderLayer)](./set/insert%28_%29.md)
  Inserts the given layer into the set.
- [func remove(RenderLayer) -> RenderLayer?](./set/remove%28_%29.md)
  Removes the given layer from the set if it exists.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer/set)*