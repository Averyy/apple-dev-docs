# group

**Framework**: RealityKit  
**Kind**: property

A collection of animations to run.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var group: [any AnimationDefinition] { get set }
```

## See Also

- [var name: String](animationgroup/name.md)
  A textual name for the group.
- [var bindTarget: BindTarget](animationgroup/bindtarget.md)
  A textual name that refers to a property on which to run the grouped animations.
- [var blendLayer: Int32](animationgroup/blendlayer.md)
  The order in which the framework composites the animation.
- [var additive: Bool](animationgroup/additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup/group)*