# bindTarget

**Framework**: RealityKit  
**Kind**: property

A textual name that identifies the animated property.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
var bindTarget: BindTarget { get set }
```

#### Discussion

The property name is a key path. For more information on key paths, see [`Key-Path Expressions`](https://developer.apple.com/documentation/Swift/key-path-expressions).

## See Also

- [var source: (any AnimationDefinition)?](animationview/source.md)
  The original animation that this structure modifies.
- [var name: String](animationview/name.md)
  A textual name for the animation.
- [var blendLayer: Int32](animationview/blendlayer.md)
  The order in which the framework composites the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationview/bindtarget)*