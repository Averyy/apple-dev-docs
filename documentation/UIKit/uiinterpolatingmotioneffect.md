# UIInterpolatingMotionEffect

**Framework**: UIKit  
**Kind**: class

An object that maps the horizontal or vertical tilt of a device to values that you specify so that UIKit can apply those values to your views.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIInterpolatingMotionEffect
```

#### Overview

You use this class to determine the amount of tilt along a single axis to apply to a view. After creating an instance of this class, you must assign appropriate values to the [`minimumRelativeValue`](uiinterpolatingmotioneffect/minimumrelativevalue.md) and [`maximumRelativeValue`](uiinterpolatingmotioneffect/maximumrelativevalue.md) properties. As the user moves the device, the motion effect object translates the fixed offset values returned by the system (which are in the range `-1` to `1`) to the range of values you specified. UIKit then applies the translated values to any target views.

## Topics

### Initializing a motion effect
- [init(keyPath: String, type: UIInterpolatingMotionEffect.EffectType)](uiinterpolatingmotioneffect/init(keypath:type:).md)
  Initializes and returns an interpolating motion effect object configured for the specific tilt direction.
- [init?(coder: NSCoder)](uiinterpolatingmotioneffect/init(coder:).md)
  Creates a motion effect from data in an unarchiver.
### Accessing the motion attributes
- [var keyPath: String](uiinterpolatingmotioneffect/keypath.md)
  The key path you want to modify on the view.
- [var type: UIInterpolatingMotionEffect.EffectType](uiinterpolatingmotioneffect/type.md)
  The tilt direction to monitor.
- [var minimumRelativeValue: Any?](uiinterpolatingmotioneffect/minimumrelativevalue.md)
  The value that maps to the minimum viewer offset.
- [var maximumRelativeValue: Any?](uiinterpolatingmotioneffect/maximumrelativevalue.md)
  The value that maps to the maximum viewer offset.
### Constants
- [UIInterpolatingMotionEffect.EffectType](uiinterpolatingmotioneffect/effecttype.md)
  The axis to use when interpolating values.

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

## See Also

- [class UIMotionEffectGroup](uimotioneffectgroup.md)
  A collection of motion effects that you want to apply to a view at the same time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect)*