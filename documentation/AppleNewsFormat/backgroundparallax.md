# BackgroundParallax

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The behavior whereby the background of a component moves slightly slower than a person’s scroll speed.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object BackgroundParallax
```

## Mentions

- [About Component Behaviors](../AppleNews/about-component-behaviors.md)

## Discussion

When you apply the `BackgroundParallax` behavior to a component, the background of the component moves slightly more slowly than a person’s scroll speed, as shown in [this video](https://developer.apple.com/apple-news/videos/background-parallax.mp4).

### Example

```json
{
  "components": [
    {
      "role": "container",
      "behavior": {
        "type": "background_parallax"
      },
      "style": {
        "fill": {
          "type": "image",
          "URL": "bundle://image.jpg",
          "fillMode": "cover",
          "verticalAlignment": "top"
        }
      },
      "layout": {
        "minimumHeight": "77.2cw"
      }
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This behavior always has the type `background_parallax`.

  **Allowed Values**: `background_parallax`

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
- [object Motion](./motion.md)
  The behavior whereby a component reacts to the motion of the person’s device.
- [object Parallax](./parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object Springy](./springy.md)
  The behavior whereby a component acts as if it’s on a short spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/backgroundparallax)*