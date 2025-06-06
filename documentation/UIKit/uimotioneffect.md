# UIMotionEffect

**Framework**: UIKit  
**Kind**: class

An abstract superclass for defining motion-based modifiers for views.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIMotionEffect
```

#### Overview

Subclasses of [`UIMotionEffect`](uimotioneffect.md) are responsible for defining the behavior to apply to a view when motion is detected. They do this by overriding the [`keyPathsAndRelativeValues(forViewerOffset:)`](uimotioneffect/keypathsandrelativevalues(forvieweroffset:).md) method and returning one or more key paths representing the view properties to modify.

##### Subclassing Notes

This class is abstract and can’t be instantiated directly. You can use the [`UIInterpolatingMotionEffect`](uiinterpolatingmotioneffect.md) class to implement effects or you can subclass and implement your own effects. If you subclass, your subclass must conform to the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) and [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocols and must implement the [`keyPathsAndRelativeValues(forViewerOffset:)`](uimotioneffect/keypathsandrelativevalues(forvieweroffset:).md) method.

## Topics

### Initializing a motion effect
- [init()](uimotioneffect/init.md)
  Initializes the motion effect to its default state.
- [init?(coder: NSCoder)](uimotioneffect/init(coder:).md)
  Creates a motion effect from data in an unarchiver.
### Getting the key paths
- [func keyPathsAndRelativeValues(forViewerOffset: UIOffset) -> [String : Any]?](uimotioneffect/keypathsandrelativevalues(forvieweroffset:).md)
  For a given set of offset values, returns the view properties (and corresponding values) to update.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIInterpolatingMotionEffect](uiinterpolatingmotioneffect.md)
- [UIMotionEffectGroup](uimotioneffectgroup.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimotioneffect)*