# CAAnimationGroup

**Framework**: Core Animation  
**Kind**: class

An object that allows multiple animations to be grouped and run concurrently.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAAnimationGroup
```

#### Overview

The grouped animations run in the time space specified by the [`CAAnimationGroup`](caanimationgroup.md) instance.

The duration of the grouped animations are not scaled to the duration of their [`CAAnimationGroup`](caanimationgroup.md). Instead, the animations are clipped to the duration of the animation group. For example, a 10 second animation grouped within an animation group with a duration of 5 seconds displays only the first 5 seconds of the animation.

The following code shows how you can create a grouped animation containing  opacity and scale animations to fade out a layer while expanding it. The animation starts with an opacity of `1` and a scale of `1` on all axes. As the animation’s scale increases to `(3, 3, 3)`, the opacity drops to `0` and the animated layer vanishes.

```swift
let fadeOut = CABasicAnimation(keyPath: "opacity")
fadeOut.fromValue = 1
fadeOut.toValue = 0
fadeOut.duration = 1
     
let expandScale = CABasicAnimation()
expandScale.keyPath = "transform"
expandScale.valueFunction = CAValueFunction(name: kCAValueFunctionScale)
expandScale.fromValue = [1, 1, 1]
expandScale.toValue = [3, 3, 3]
     
let fadeAndScale = CAAnimationGroup()
fadeAndScale.animations = [fadeOut, expandScale]
fadeAndScale.duration = 1
```

> ❗ **Important**:  The [`delegate`](caanimation/delegate.md) and [`isRemovedOnCompletion`](caanimation/isremovedoncompletion.md) properties of animations in the [`animations`](caanimationgroup/animations.md) array are currently ignored. The [`CAAnimationGroup`](caanimationgroup.md) delegate does receive these messages.

## Topics

### Grouped animations
- [var animations: [CAAnimation]?](caanimationgroup/animations.md)
  An array of `CAAnimation` objects to be evaluated in the time space of the receiver.

## Relationships

### Inherits From
- [CAAnimation](caanimation.md)
### Conforms To
- [CAAction](caaction.md)
- [CAMediaTiming](camediatiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CATransaction](catransaction.md)
  A mechanism for grouping multiple layer-tree operations into atomic updates to the render tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationgroup)*