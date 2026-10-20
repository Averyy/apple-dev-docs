# group

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A collection of animations to run.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var group: [any AnimationDefinition] { get set }
```

## See Also

### Configuring the group
- [var name: String](./name.md)
  A textual name for the group.
- [var bindTarget: BindTarget](./bindtarget.md)
  A textual name that refers to a property on which to run the grouped animations.
- [var blendLayer: Int32](./blendlayer.md)
  The order in which the framework composites the animation.
- [var additive: Bool](./additive.md)
  A Boolean value that indicates whether the animation builds on the current state of the target entity or resets the state before running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgroup/group)*