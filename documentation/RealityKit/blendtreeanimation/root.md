# root

**Framework**: RealityKit  
**Kind**: property

The first node in a tree of animations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var root: any BlendTreeNode { get set }
```

#### Discussion

This property defines the node that represents the root of a blend tree. If you assign this property a [`BlendTreeBlendNode`](blendtreeblendnode.md) instance, the root branches for every member you add to the instance’s [`sources`](blendtreeblendnode/sources.md) property.

If you define a [`BlendTreeSourceNode`](blendtreesourcenode.md) instance to this property, the tree contains a single animation, which blends with no other animations.

## See Also

- [var name: String](blendtreeanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](blendtreeanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var blendLayer: Int32](blendtreeanimation/blendlayer.md)
  The order in which the framework composites the animation.
- [var isAdditive: Bool](blendtreeanimation/isadditive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeanimation/root)*