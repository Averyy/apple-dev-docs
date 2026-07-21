# RenderLayer.Set

**Framework**: RealityKit  
**Kind**: struct

An unordered collection of unique render layers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Set
```

#### Overview

[`RenderLayer.Set`](renderlayer/set.md) represents a group of layers - for example, the layers a light illuminates ([`layers`](directionallightcomponent/layers.md), [`layers`](pointlightcomponent/layers.md), [`layers`](spotlightcomponent/layers.md)) or the layers an entity participates in ([`layers`](renderlayercomponent/layers.md)).

Create a [`RenderLayer.Set`](renderlayer/set.md) using an array literal:

```swift
let layers: RenderLayer.Set = [.defaultLayer, RenderLayer("com.myapp.hero")]
```

## Topics

### Inspecting the set
- [var count: Int](renderlayer/set/count.md)
  The number of layers in the set.
- [var isEmpty: Bool](renderlayer/set/isempty.md)
  A Boolean value indicating whether the set contains no layers.
- [func contains(RenderLayer) -> Bool](renderlayer/set/contains(_:).md)
  Returns a Boolean value indicating whether the set contains the given layer.
### Initializers
- [init()](renderlayer/set/init.md)
  Creates an empty set of render layers.
- [init<S>(S)](renderlayer/set/init(_:).md)
  Creates a set of render layers from a sequence.
### Instance Methods
- [func insert(RenderLayer) -> (inserted: Bool, memberAfterInsert: RenderLayer)](renderlayer/set/insert(_:).md)
  Inserts the given layer into the set.
- [func remove(RenderLayer) -> RenderLayer?](renderlayer/set/remove(_:).md)
  Removes the given layer from the set if it exists.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer/set)*