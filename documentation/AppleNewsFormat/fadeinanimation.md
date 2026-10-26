# FadeInAnimation

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The animation whereby a component fades into view.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object FadeInAnimation
```

## Mentions

- [About Component Animations](../AppleNews/about-component-animations.md)

#### Discussion

With this animation type the component fades in as it enters the person’s view. The initial transparency (alpha value) of the component is configurable. A `FadeInAnimation` with the `userControllable` property set to `true` is shown in [this video](https://developer.apple.com/apple-news/videos/fade-in-true.mp4).

##### Example

```json
{
  "components": [
    {
      "role": "heading1",
      "text": "2. Unbeatable Heat"
    },
    {
      "role": "figure",
      "URL": "bundle://figure.jpg",
      "animation": {
        "type": "fade_in",
        "userControllable": false,
        "initialAlpha": 0
      }
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This animation always has the type `fade_in`.

  **Allowed Values**: `fade_in`
- `initialAlpha` (number): The initial transparency of the component (and the animation). Set `initialAlpha` to a value between `0` (completely transparent) and `1` (completely visible).

  **Default**: `0.3`; **Minimum**: `0`; **Maximum**: `1`
- `userControllable` (boolean): Indicates whether user action like scrolling controls the animation (`true`), or the animation happens when the component is within the visible area of the document (`false`).

  **Default**: `false`

## Relationships

### Inherits From
- [ComponentAnimation](./componentanimation.md)

## See Also

### Related Documentation
- [Adding Animations](../AppleNews/adding-animations.md)
  Use animations to affect how parts of your article come into view the first time they appear.
### Animations
- [About Component Animations](../AppleNews/about-component-animations.md)
  Learn how to affect the way in which components come into view.
- [object ComponentAnimation](./componentanimation.md)
  Properties that all types of animations share.
- [object AppearAnimation](./appearanimation.md)
  An animation type whereby a component appears on the screen.
- [object MoveInAnimation](./moveinanimation.md)
  The animation whereby a component moves in from the side of the screen.
- [object ScaleFadeAnimation](./scalefadeanimation.md)
  The animation in which a component scales up and fades into view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/fadeinanimation)*