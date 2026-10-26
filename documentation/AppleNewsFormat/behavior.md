# Behavior

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

Properties shared by all the behaviors you can use to affect how components react to device motion and scrolling.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Behavior
```

#### Discussion

A behavior defines the physics of a component and its context. The effect of a component behavior is persistent and occurs every time a person views the article. Compare that with an animation which happens just once each time a person views the component in your article.

> **Note**:  You don’t use the `Behavior` object directly; instead, use the specific objects that extend it.

You can use this object in [`Component`](./component.md).

## Properties

- `type` (string) *(required)*: The type of behavior; for example, parallax for a Parallax behavior.

  **Allowed Values**: `background_motion`, `background_parallax`, `motion`, `parallax`, `springy`

## Relationships

### Inherited By
- [BackgroundMotion](./backgroundmotion.md)
- [BackgroundParallax](./backgroundparallax.md)
- [Motion](./motion.md)
- [Parallax](./parallax.md)
- [Springy](./springy.md)

## See Also

### Related Documentation
- [Adding Parallax Behavior](../AppleNews/adding-parallax-behavior.md)
  Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.
### Behaviors
- [About Component Behaviors](../AppleNews/about-component-behaviors.md)
  Learn how to affect components’ reactions to device motion and scrolling.
- [object BackgroundMotion](./backgroundmotion.md)
  The behavior whereby the background of a component moves in the opposite direction from the motion of the device.
- [object BackgroundParallax](./backgroundparallax.md)
  The behavior whereby the background of a component moves slightly slower than a person’s scroll speed.
- [object Motion](./motion.md)
  The behavior whereby a component reacts to the motion of the person’s device.
- [object Parallax](./parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object Springy](./springy.md)
  The behavior whereby a component acts as if it’s on a short spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/behavior)*