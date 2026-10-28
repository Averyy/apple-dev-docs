# Motion

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The behavior whereby a component reacts to the motion of the person’s device.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Motion
```

## Mentions

- [About Component Behaviors](../AppleNews/about-component-behaviors.md)

## Discussion

When you apply the `Motion` behavior to a component, the component reacts to the movement of the device. For example, when the user tilts the device, the component moves in the same direction. [This video](https://developer.apple.com/apple-news/videos/motion.mp4) shows an example of the `motion` behavior.

### Example

```json
{
  "components": [
    {
      "role": "figure",
      "behavior": {
        "type": "motion"
      },
      "URL": "bundle://figure.jpg"
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This behavior always has the type `motion`.

  **Allowed Values**: `motion`

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
- [object Parallax](./parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object Springy](./springy.md)
  The behavior whereby a component acts as if it’s on a short spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/motion)*