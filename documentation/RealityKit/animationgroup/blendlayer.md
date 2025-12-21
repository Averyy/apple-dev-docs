# blendLayer

**Framework**: RealityKit  
**Kind**: property

The order in which the framework composites the animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var blendLayer: Int32 { get set }
```

#### Discussion

The framework applies multiple animations on the same target in ascending order of this property’s value. Animations in a lower layer run before animations in a higher layer. Animations that share the same value apply in the order they execute.

## See Also

- [var group: [any AnimationDefinition]](animationgroup/group.md)
  A collection of animations to run.
- [var name: String](animationgroup/name.md)
  A textual name for the group.
- [var bindTarget: BindTarget](animationgroup/bindtarget.md)
  A textual name that refers to a property on which to run the grouped animations.
- [var additive: Bool](animationgroup/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup/blendlayer)*