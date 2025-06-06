# group_

**Framework**: RealityKit  
**Kind**: property

An optional collection of animations to run.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
var group_: [any AnimationDefinition]? { get set }
```

#### Discussion

Don’t use this property. Use [`group`](animationgroup/group.md) instead.

## See Also

- [var group: [any AnimationDefinition]](animationgroup/group.md)
  A collection of animations to run.
- [var name: String](animationgroup/name.md)
  A textual name for the group.
- [var bindTarget: BindTarget](animationgroup/bindtarget.md)
  A textual name that refers to a property on which to run the grouped animations.
- [var blendLayer: Int32](animationgroup/blendlayer.md)
  The order in which the framework composites the animation.
- [var additive: Bool](animationgroup/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup/group_)*