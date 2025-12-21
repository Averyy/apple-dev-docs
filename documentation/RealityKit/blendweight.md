# BlendWeight

**Framework**: RealityKit  
**Kind**: enum

A numerical representation of the impact an animation has on a scene or entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
enum BlendWeight
```

#### Overview

The [`BlendTreeSourceNode`](blendtreesourcenode.md) structure accepts this enumeration as an initializer argument.

To specify a custom weight, use the value case:

```swift
let node = BlendTreeSourceNode(
    source: animation1,
    name: "anim2",
    weight: .value(0.75))
```

## Topics

### Choosing the blend weight
- [case bindTarget(BindTarget, defaultWeight: Float)](blendweight/bindtarget(_:defaultweight:).md)
  The amount of impact  an animation has on the bind target of an entity.
- [case parameter(String, defaultWeight: Float)](blendweight/parameter(_:defaultweight:).md)
  The amount of impact an animation has on a named parameter of an entity.
- [BlendWeight.value(_:)](blendweight/value(_:).md)
  The numerical representation of the impact an animation has on an entity.
### Comparing blend weights
- [static func == (BlendWeight, BlendWeight) -> Bool](blendweight/==(_:_:).md)
  Returns a Boolean value that indicates whether two blend weights are equal.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct BlendTreeAnimation](blendtreeanimation.md)
  A collection of animations on the same property that the framework blends to a single animation.
- [protocol BlendTreeNode](blendtreenode.md)
  An interface for a node that’s a member of a blend tree.
- [struct BlendTreeBlendNode](blendtreeblendnode.md)
  A source node for an animation that mixes several animations to form a single animation.
- [struct BlendTreeSourceNode](blendtreesourcenode.md)
  A blend node that contains an animation.
- [struct BlendTreeInvalidNode](blendtreeinvalidnode.md)
  A blend tree node that’s internal only or sources from an invalid definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendweight)*