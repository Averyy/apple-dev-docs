# About Component Animations

**Framework**: Apple News

Learn how to affect the way in which components come into view.

#### Overview

An animation is an effect, such as a fade-in, that’s applied to an individual component. Apple News Format has these animations for components:

- [`AppearAnimation`](https://developer.apple.com/documentation/applenewsformat/appearanimation). Causes the component to appear.
- [`FadeInAnimation`](https://developer.apple.com/documentation/applenewsformat/fadeinanimation). Causes the component to fade into view.
- [`MoveInAnimation`](https://developer.apple.com/documentation/applenewsformat/moveinanimation). Causes the component to move into view from the left or right side of the screen.
- [`ScaleFadeAnimation`](https://developer.apple.com/documentation/applenewsformat/scalefadeanimation). Causes the component to fade into view and scale up.

An  is different from a . An animation occurs only once each time the user views the article, while a behavior is persistent and always in effect as long as the user is viewing the article. See [`About Component Behaviors`](about-component-behaviors.md).

You can apply a combination of animations and behaviors to a `chapter` or `section` component by using a scene. See [`Adding a Scene to a Chapter or a Section Header`](adding-a-scene-to-a-chapter-or-a-section-header.md).

## See Also

- [object ComponentAnimation](../applenewsformat/componentanimation.md)
  Properties that all types of animations share.
- [object AppearAnimation](../applenewsformat/appearanimation.md)
  An animation type whereby a component appears on the screen.
- [object FadeInAnimation](../applenewsformat/fadeinanimation.md)
  The animation whereby a component fades into view.
- [object MoveInAnimation](../applenewsformat/moveinanimation.md)
  The animation whereby a component moves in from the side of the screen.
- [object ScaleFadeAnimation](../applenewsformat/scalefadeanimation.md)
  The animation in which a component scales up and fades into view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/about-component-animations)*