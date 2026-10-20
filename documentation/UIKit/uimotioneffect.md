# UIMotionEffect

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An abstract superclass for defining motion-based modifiers for views.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIMotionEffect
```

```objc
@interface UIMotionEffect : NSObject
```

#### Overview

Subclasses of [`UIMotionEffect`](./uimotioneffect.md) are responsible for defining the behavior to apply to a view when motion is detected. They do this by overriding the [`keyPathsAndRelativeValues(forViewerOffset:)`](./uimotioneffect/keypathsandrelativevalues%28forvieweroffset%29.md) method and returning one or more key paths representing the view properties to modify.

##### Subclassing notes

This class is abstract and can’t be instantiated directly. You can use the [`UIInterpolatingMotionEffect`](./uiinterpolatingmotioneffect.md) class to implement effects or you can subclass and implement your own effects. If you subclass, your subclass must conform to the [`NSCopying`](../Foundation/nscopying.md) and [`NSCoding`](../Foundation/nscoding.md) protocols and must implement the [`keyPathsAndRelativeValues(forViewerOffset:)`](./uimotioneffect/keypathsandrelativevalues%28forvieweroffset%29.md) method.

## Topics

### Initializing a motion effect
- [init()](./uimotioneffect/init%28%29.md)
  Initializes the motion effect to its default state.
- [init?(coder: NSCoder)](./uimotioneffect/init%28coder%29.md)
  Creates a motion effect from data in an unarchiver.
### Getting the key paths
- [func keyPathsAndRelativeValues(forViewerOffset: UIOffset) -> [String : Any]?](./uimotioneffect/keypathsandrelativevalues%28forvieweroffset%29.md)
  For a given set of offset values, returns the view properties (and corresponding values) to update.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UIInterpolatingMotionEffect](./uiinterpolatingmotioneffect.md)
- [UIMotionEffectGroup](./uimotioneffectgroup.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimotioneffect)*