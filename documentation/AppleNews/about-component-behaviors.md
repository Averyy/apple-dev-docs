# About Component Behaviors

**Framework**: Apple News

Learn how to affect components’ reactions to device motion and scrolling.

#### Overview

In Apple News Format, a behavior defines the physics of a component and its context and determines how a component responds to user actions. A behavior can specify the gravitational effect of a component or how the component reacts to the motion of the device. For example, a behavior can move the background of a component slightly more slowly than the user is scrolling.

Apple News Format has these behaviors for components:

- [`BackgroundMotion`](https://developer.apple.com/documentation/applenewsformat/backgroundmotion). Causes the background of a component to move in the opposite direction from the motion of the device.
- [`BackgroundParallax`](https://developer.apple.com/documentation/applenewsformat/backgroundparallax). Causes the background of a component to move slightly more slowly than the user’s scroll speed.
- [`Motion`](https://developer.apple.com/documentation/applenewsformat/motion). Causes a component to react to movement of the device.
- [`Parallax`](https://developer.apple.com/documentation/applenewsformat/parallax). Causes a component to move at a specific speed.
- [`Springy`](https://developer.apple.com/documentation/applenewsformat/springy). Causes a component to act as if it is held in place with a short spring.

A  is different from an . A behavior is persistent and always in effect as long as the user is viewing the article. An animation occurs only once each time the user views the article. See [`About Component Animations`](about-component-animations.md).

## See Also

- [Adding Parallax Behavior](adding-parallax-behavior.md)
  Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.
- [object Behavior](../applenewsformat/behavior.md)
  Properties shared by all the behaviors you can use to affect how components react to device motion and scrolling.
- [object BackgroundMotion](../applenewsformat/backgroundmotion.md)
  The behavior whereby the background of a component moves in the opposite direction from the motion of the device.
- [object BackgroundParallax](../applenewsformat/backgroundparallax.md)
  The behavior whereby the background of a component moves slightly slower than a person’s scroll speed.
- [object Motion](../applenewsformat/motion.md)
  The behavior whereby a component reacts to the motion of the person’s device.
- [object Parallax](../applenewsformat/parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object Springy](../applenewsformat/springy.md)
  The behavior whereby a component acts as if it’s on a short spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/about-component-behaviors)*