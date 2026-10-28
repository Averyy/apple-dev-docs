# CAAnimation

**Framework**: Core Animation  
**Kind**: class  
**Role**: Class

The abstract superclass for animations in Core Animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAAnimation
```

```objc
@interface CAAnimation : NSObject
```

## Mentions

- [Optimizing iPhone and iPad apps to support ProMotion displays](./optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md)

## Overview

`CAAnimation` provides the basic support for the [`CAMediaTiming`](./camediatiming.md) and [`CAAction`](./caaction.md) protocols. You do not create instance of [`CAAnimation`](./caanimation.md): to animate Core Animation layers or SceneKit objects, create instances of the concrete subclasses [`CABasicAnimation`](./cabasicanimation.md), [`CAKeyframeAnimation`](./cakeyframeanimation.md), [`CAAnimationGroup`](./caanimationgroup.md), or [`CATransition`](./catransition.md).

### Animating Core Animation Layers

You can animate the contents of your iOS or macOS app’s user interface by attaching animations to [`CALayer`](./calayer.md) objects. For more information, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

### Animating Scene Kit Content

In Scene Kit, animation objects represent not only property-based animations, but also animations of geometry data created with external 3D authoring tools and loaded from a scene file. You use the properties of the [`CAAnimation`](./caanimation.md) object representing a geometry animation to control its timing, monitor its progress, and attach actions for Scene Kit to trigger during the animation. You can attach animations to Scene Kit objects that adopt the [`SCNAnimatable`](../SceneKit/scnanimatable.md) protocol, including nodes, geometries, and materials.

In a Scene Kit app, [`CAAnimation`](./caanimation.md) objects support additional methods and properties, listed under Controlling SceneKit Animation Timing, Fading between SceneKit Animations, and Attaching SceneKit Animation Events.

## Topics

### Creating an Animation
- [init(SCNAnimation: SCNAnimation)](./caanimation/init%28scnanimation%29.md)
  Creates an animation from a SceneKit animation.
- [+ animation](./caanimation/animation.md)
  Creates and returns a new `CAAnimation` instance.
### Animation Attributes
- [var isRemovedOnCompletion: Bool](./caanimation/isremovedoncompletion.md)
  Determines if the animation is removed from the target layer’s animations upon completion.
- [var timingFunction: CAMediaTimingFunction?](./caanimation/timingfunction.md)
  An optional timing function defining the pacing of the animation.
### Providing Default Values
- [class func defaultValue(forKey: String) -> Any?](./caanimation/defaultvalue%28forkey%29.md)
  Specifies the default value of the property with the specified key.
### Designating a Delegate
- [var delegate: (any CAAnimationDelegate)?](./caanimation/delegate.md)
  Specifies the receiver’s delegate object.
### Archiving Properties
- [func shouldArchiveValue(forKey: String) -> Bool](./caanimation/shouldarchivevalue%28forkey%29.md)
  Specifies whether the value of the property for a given key is archived.
### Controlling SceneKit Animation Timing
- [var usesSceneTimeBase: Bool](./caanimation/usesscenetimebase.md)
  For animations attached to SceneKit objects, a Boolean value that determines whether the animation is evaluated using the scene time or the system time.
### Fading between SceneKit Animations
- [var fadeInDuration: CGFloat](./caanimation/fadeinduration.md)
  For animations attached to SceneKit objects, the duration for transitioning into the animation’s effect as it begins.
- [var fadeOutDuration: CGFloat](./caanimation/fadeoutduration.md)
  For animations attached to SceneKit objects, the duration for transitioning out of the animation’s effect as it ends.
### Attaching SceneKit Animation Events
- [var animationEvents: [SCNAnimationEvent]?](./caanimation/animationevents.md)
  For animations attached to SceneKit objects, a list of events attached to an animation.
### Initializers
- [init(SCNAnimation: SCNAnimation)](./caanimation/init%28scnanimation%29.md)
  Creates an animation from a SceneKit animation.
- [init?(coder: NSCoder)](./caanimation/init%28coder%29.md)
### Instance Properties
- [var preferredFrameRateRange: CAFrameRateRange](./caanimation/preferredframeraterange.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CAAnimationGroup](./caanimationgroup.md)
- [CAPropertyAnimation](./capropertyanimation.md)
- [CATransition](./catransition.md)
### Conforms To
- [CAAction](./caaction.md)
- [CAMediaTiming](./camediatiming.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [SCNAnimationProtocol](../SceneKit/scnanimationprotocol.md)

## See Also

### Animation
- [protocol CAAnimationDelegate](./caanimationdelegate.md)
  Methods your app can implement to respond when animations start and stop.
- [class CAPropertyAnimation](./capropertyanimation.md)
  An abstract subclass for creating animations that manipulate the value of layer properties.
- [class CABasicAnimation](./cabasicanimation.md)
  An object that provides basic, single-keyframe animation capabilities for a layer property.
- [class CAKeyframeAnimation](./cakeyframeanimation.md)
  An object that provides keyframe animation capabilities for a layer object.
- [class CASpringAnimation](./caspringanimation.md)
  An animation that applies a spring-like force to a layer’s properties.
- [class CATransition](./catransition.md)
  An object that provides an animated transition between a layer’s states.
- [class CAValueFunction](./cavaluefunction.md)
  An object that provides a flexible method of defining animated transformations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimation)*