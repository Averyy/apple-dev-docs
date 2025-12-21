# BlendTreeAnimation

**Framework**: RealityKit  
**Kind**: struct

A collection of animations on the same property that the framework blends to a single animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct BlendTreeAnimation<Value> where Value : AnimatableData
```

#### Overview

This structure provides a way to form a single animation by mixing several other animations together. You define a source node for each animation, and a weight, which determines how much each individual animation takes effect in the resulting animation.

To create the blended animation, you define a  that sprouts from [`root`](blendtreeanimation/root.md), which consists of one or more blend-tree nodes ([`BlendTreeNode`](blendtreenode.md)). Each node may be one of the following conforming types:

- [`BlendTreeBlendNode`](blendtreeblendnode.md), which branches the tree for every element in [`sources`](blendtreeblendnode/sources.md)
- [`BlendTreeSourceNode`](blendtreesourcenode.md), which defines one of the animations to blend via its [`source`](blendtreesourcenode/source.md) property

Because source nodes reference no other nodes, they represent leaf nodes in the tree.

##### Blending Two Skeletal Movements to a Single Movement

The following animation plays a sampling of the animations named `anim1` and `anim2`. To fine-tune the interplay between the two animations, the code sets a blend weight for each animation. The weight of `0.25` for `anim1` determines that the first animation’s behavior is 25% prominent in the final result. The `anim2` weight is `0.75`, as the cumulative blend weight across all animations in the tree needs to equal `1`. This determines that the second animation influences 75% of the visual behavior of the blended animation.

```swift
let anim1 = FromToByAnimation<JointTransforms>(
    name: "anim1",
    from: JointTransforms([Transform(scale: SIMD3<Float>(1, 2, 3),
    rotation: simd_quatf(ix: 5, iy: 6, iz: 7, r: 8),
    translation: SIMD3<Float>(10, 20, 30))]),
    to: JointTransforms([Transform(scale: SIMD3<Float>(11, 21, 31),
    rotation: simd_quatf(ix: 50, iy: 60, iz: 70, r: 80),
    translation: SIMD3<Float>(100, 200, 300))]),
    duration: 1.0)

let anim2 = FromToByAnimation<JointTransforms>(
    name: "anim2",
    from: JointTransforms([Transform(scale: SIMD3<Float>(10, 20, 30),
    rotation: simd_quatf(ix: 4, iy: 5, iz: 5, r: 7),
    translation: SIMD3<Float>(100, 200, 300))]),
    to: JointTransforms([Transform(scale: SIMD3<Float>(110, 210, 310),
    rotation: simd_quatf(ix: 500, iy: 60, iz: 70, r: 80),
    translation: SIMD3<Float>(1000, 2000, 3000))]),
    duration: 10.0)

let blendTree = BlendTreeAnimation<JointTransforms>(
    blend(
        BlendTreeSourceNode(
            source: anim1,
            name: "anim1",
            weight: .value(0.25)),
        BlendTreeSourceNode(
            source: anim2,
            name: "anim2",
            weight: .value(0.75)),
        name: "blend"),
    name: "blendTree",
    bindTarget: .parameter("bar")
)
```

> 💡 **Tip**: To modify the weights for each frame, create a source node with a dynamic [`BlendWeight`](blendweight.md), such as with the [`BlendWeight.bindTarget(_:defaultWeight:)`](blendweight/bindtarget(_:defaultweight:).md) or [`BlendWeight.parameter(_:defaultWeight:)`](blendweight/parameter(_:defaultweight:).md) enumeration cases.

## Topics

### Creating an animation
- [init(any BlendTreeNode, name: String, isAdditive: Bool, bindTarget: BindTarget?, blendLayer: Int32, repeatMode: AnimationRepeatMode, fillMode: AnimationFillMode, trimStart: TimeInterval?, trimEnd: TimeInterval?, trimDuration: TimeInterval?, offset: TimeInterval, delay: TimeInterval, speed: Float)](blendtreeanimation/init(_:name:isadditive:bindtarget:blendlayer:repeatmode:fillmode:trimstart:trimend:trimduration:offset:delay:speed:).md)
  Creates a unique animation from a combination of other animations in the form of a tree.
### Configuring the animation
- [var root: any BlendTreeNode](blendtreeanimation/root.md)
  The first node in a tree of animations.
- [var name: String](blendtreeanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](blendtreeanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](blendtreeanimation/blendlayer.md)
  The order in which the framework composites the animation.
- [var isAdditive: Bool](blendtreeanimation/isadditive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.
### Timing the animation
- [var speed: Float](blendtreeanimation/speed.md)
  A factor that increases or decreases the animation’s rate of playback.
- [var delay: TimeInterval](blendtreeanimation/delay.md)
  An amount of time that lapses before the animation plays.
- [var duration: TimeInterval](blendtreeanimation/duration.md)
  The total playback time of the animation.
- [var offset: TimeInterval](blendtreeanimation/offset.md)
  The time, in seconds, at which the animation begins within the duration.
- [var trimDuration: TimeInterval?](blendtreeanimation/trimduration.md)
  An optional duration that overrides the calculated duration.
- [var trimStart: TimeInterval?](blendtreeanimation/trimstart.md)
  The optional time, in seconds, at which the source animation plays.
- [var trimEnd: TimeInterval?](blendtreeanimation/trimend.md)
  The optional time, in seconds, at which the source animation stops.
### Repeating animation playback
- [var repeatMode: AnimationRepeatMode](blendtreeanimation/repeatmode.md)
  An option that determines how the animation repeats.
- [var fillMode: AnimationFillMode](blendtreeanimation/fillmode.md)
  An option that determines which data displays outside of the normal duration.

## Relationships

### Conforms To
- [AnimationDefinition](animationdefinition.md)

## See Also

- [protocol BlendTreeNode](blendtreenode.md)
  An interface for a node that’s a member of a blend tree.
- [struct BlendTreeBlendNode](blendtreeblendnode.md)
  A source node for an animation that mixes several animations to form a single animation.
- [struct BlendTreeSourceNode](blendtreesourcenode.md)
  A blend node that contains an animation.
- [struct BlendTreeInvalidNode](blendtreeinvalidnode.md)
  A blend tree node that’s internal only or sources from an invalid definition.
- [enum BlendWeight](blendweight.md)
  A numerical representation of the impact an animation has on a scene or entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeanimation)*