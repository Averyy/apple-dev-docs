# BackgroundMotion

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The behavior whereby the background of a component moves in the opposite direction from the motion of the device.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object BackgroundMotion
```

## Mentions

- [About Component Behaviors](../AppleNews/about-component-behaviors.md)

#### Discussion

When you apply the `BackgroundMotion` behavior to a component, the background of the component moves in the opposite direction of the device motion — much like the background image on the Home Screen on iPhone. [This video](https://developer.apple.com/apple-news/videos/background-motion.mp4) shows an example of the `BackgroundMotion` behavior.

##### Example

```json
{
  "components": [
    {
      "role": "container",
      "behavior": {
        "type": "background_motion"
      },
      "style": {
        "fill": {
          "type": "image",
          "URL": "bundle://summer.jpg",
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

- `type` (string) *(required)*: This behavior always has the type `background_motion`.

  **Allowed Values**: `background_motion`

## Relationships

### Inherits From
- [Behavior](./behavior.md)

## See Also

### Behaviors
- [About Component Behaviors](../AppleNews/about-component-behaviors.md)
  Learn how to affect components’ reactions to device motion and scrolling.
- [object Behavior](./behavior.md)
  Properties shared by all the behaviors you can use to affect how components react to device motion and scrolling.
- [object BackgroundParallax](./backgroundparallax.md)
  The behavior whereby the background of a component moves slightly slower than a person’s scroll speed.
- [object Motion](./motion.md)
  The behavior whereby a component reacts to the motion of the person’s device.
- [object Parallax](./parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object Springy](./springy.md)
  The behavior whereby a component acts as if it’s on a short spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/backgroundmotion)*