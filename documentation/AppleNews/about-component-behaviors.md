# About Component Behaviors

**Framework**: Apple News  
**Role**: Article

Learn how to affect components’ reactions to device motion and scrolling.

#### Overview

In Apple News Format, a behavior defines the physics of a component and its context and determines how a component responds to user actions. A behavior can specify the gravitational effect of a component or how the component reacts to the motion of the device. For example, a behavior can move the background of a component slightly more slowly than the user is scrolling.

Apple News Format has these behaviors for components:

- [`BackgroundMotion`](../AppleNewsFormat/backgroundmotion.md). Causes the background of a component to move in the opposite direction from the motion of the device.
- [`BackgroundParallax`](../AppleNewsFormat/backgroundparallax.md). Causes the background of a component to move slightly more slowly than the user’s scroll speed.
- [`Motion`](../AppleNewsFormat/motion.md). Causes a component to react to movement of the device.
- [`Parallax`](../AppleNewsFormat/parallax.md). Causes a component to move at a specific speed.
- [`Springy`](../AppleNewsFormat/springy.md). Causes a component to act as if it is held in place with a short spring.

A *behavior* is different from an *animation*. A behavior is persistent and always in effect as long as the user is viewing the article. An animation occurs only once each time the user views the article. See [About Component Animations](./about-component-animations.md).

## See Also

### Related Documentation
- [Adding Parallax Behavior](./adding-parallax-behavior.md)
  Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.
### Behaviors
- [object Behavior](../AppleNewsFormat/behavior.md)
  Properties shared by all the behaviors you can use to affect how components react to device motion and scrolling.
- [object BackgroundMotion](../AppleNewsFormat/backgroundmotion.md)
  The behavior whereby the background of a component moves in the opposite direction from the motion of the device.
- [object BackgroundParallax](../AppleNewsFormat/backgroundparallax.md)
  The behavior whereby the background of a component moves slightly slower than a person’s scroll speed.
- [object Motion](../AppleNewsFormat/motion.md)
  The behavior whereby a component reacts to the motion of the person’s device.
- [object Parallax](../AppleNewsFormat/parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object Springy](../AppleNewsFormat/springy.md)
  The behavior whereby a component acts as if it’s on a short spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/about-component-behaviors)*