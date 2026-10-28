# Parallax

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The behavior whereby a component moves at a speed different from the scroll speed.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Parallax
```

## Mentions

- [About Component Behaviors](../AppleNews/about-component-behaviors.md)

## Discussion

When you apply the `Parallax` behavior to a component, the component moves at a different speed than the scroll speed. Use the `factor` property to set the speed of the component. [This video](https://developer.apple.com/apple-news/videos/parallax.mp4) shows an example of the `parallax` behavior.

> 💡 **Tip**:  When you use parallax behavior, you might notice text becoming illegible as it covers an image. You can fix this easily, and create a cleaner, more legible article, by adding a background color.

### Example

```json
{
  "components": [
    {
      "role": "figure",
      "behavior": {
        "type": "parallax",
        "factor": 0.8
      },
      "URL": "bundle://figure.jpg"
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This behavior always has the type `parallax`.

  **Allowed Values**: `parallax`
- `factor` (number): The speed of the component, as a factor of the scroll speed. Use a value of factor between `0.5` and `2.0`. Values outside this range are reset to the minimum or maximum value.

  The parallax factor `1.0` is equal to the scroll speed.

  A factor lower than `1.0` makes the component move more slowly than the scrolling speed.

  A factor higher than `1.0` makes the component move more quickly than the scrolling speed.

  **Default**: `0.9`; **Minimum**: `0.5`; **Maximum**: `2`

## Relationships

### Inherits From
- [Behavior](./behavior.md)

## See Also

### Related Documentation
- [Adding Parallax Behavior](../AppleNews/adding-parallax-behavior.md)
  Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.
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
- [object Springy](./springy.md)
  The behavior whereby a component acts as if it’s on a short spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/parallax)*