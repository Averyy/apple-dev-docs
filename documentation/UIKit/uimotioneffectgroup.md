# UIMotionEffectGroup

**Framework**: UIKit  
**Kind**: class

A collection of motion effects that you want to apply to a view at the same time.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIMotionEffectGroup
```

#### Overview

This class behaves similarly to the [`CAAnimationGroup`](https://developer.apple.com/documentation/QuartzCore/CAAnimationGroup) class in Core Animation. The key paths and values returned by each motion effect object are applied simultaneously and with the same timing. Because [`UIMotionEffectGroup`](uimotioneffectgroup.md) is a subclass of [`UIMotionEffect`](uimotioneffect.md), you can treat it like a single motion effect in your code. After setting a value for the [`motionEffects`](uimotioneffectgroup/motioneffects.md) property, add the group object to one or more of your views.

## Topics

### Setting the group items
- [var motionEffects: [UIMotionEffect]?](uimotioneffectgroup/motioneffects.md)
  An array of motion effect objects to apply as a group to the view.

## Relationships

### Inherits From
- [UIMotionEffect](uimotioneffect.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIInterpolatingMotionEffect](uiinterpolatingmotioneffect.md)
  An object that maps the horizontal or vertical tilt of a device to values that you specify so that UIKit can apply those values to your views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimotioneffectgroup)*