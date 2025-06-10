# blendLayer

**Framework**: RealityKit  
**Kind**: property

The order in which the framework composites the animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var blendLayer: Int32 { get set }
```

#### Discussion

The framework applies multiple animations on the same target in ascending order of this property’s value. Animations in a lower layer run before animations in a higher layer. Animations that share the same value apply in the order that they execute.

## See Also

- [var root: any BlendTreeNode](blendtreeanimation/root.md)
  The first node in a tree of animations.
- [var name: String](blendtreeanimation/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](blendtreeanimation/bindtarget.md)
  A textual name that identifies the particular property that animates.
- [var isAdditive: Bool](blendtreeanimation/isadditive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendtreeanimation/blendlayer)*