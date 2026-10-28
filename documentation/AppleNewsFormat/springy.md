# Springy

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The behavior whereby a component acts as if it’s on a short spring.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Springy
```

## Mentions

- [About Component Behaviors](../AppleNews/about-component-behaviors.md)

## Discussion

When you apply the `Springy` behavior to a component, the component behaves as if it’s held in place with a short spring, as shown in [this video](https://developer.apple.com/apple-news/videos/springy.mp4).

### Example

```json
{
  "components": [
    {
      "role": "figure",
      "behavior": {
        "type": "springy"
      },
      "URL": "bundle://figure.jpg"
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This behavior always has the type `springy`.

  **Allowed Values**: `springy`

## Relationships

### Inherits From
- [Behavior](./behavior.md)

## See Also

### Behaviors
- [About Component Behaviors](../AppleNews/about-component-behaviors.md)
  Learn how to affect components’ reactions to device motion and scrolling.
- [object Behavior](./behavior.md)
  Properties shared by all the behaviors you can use to affect how components react to device motion and scrolling.
- [object BackgroundMotion](./backgroundmotion.md)
  The behavior whereby the background of a component moves in the opposite direction from the motion of the device.
- [object BackgroundParallax](./backgroundparallax.md)
  The behavior whereby the background of a component moves slightly slower than a person’s scroll speed.
- [object Motion](./motion.md)
  The behavior whereby a component reacts to the motion of the person’s device.
- [object Parallax](./parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/springy)*