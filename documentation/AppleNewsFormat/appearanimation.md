# AppearAnimation

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

An animation type whereby a component appears on the screen.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object AppearAnimation
```

## Mentions

- [About Component Animations](../AppleNews/about-component-animations.md)

#### Discussion

With this animation type, the component starts out invisible and then appears. As the component enters the person’s view, it appears with a slight fade-in as shown in [this video](https://developer.apple.com/apple-news/videos/appear.mp4).

See also [`FadeInAnimation`](./fadeinanimation.md), where you can set the initial appearance of the component.

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
        "type": "appear"
      }
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This animation always has the type `appear`.

  **Allowed Values**: `appear`

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
- [object FadeInAnimation](./fadeinanimation.md)
  The animation whereby a component fades into view.
- [object MoveInAnimation](./moveinanimation.md)
  The animation whereby a component moves in from the side of the screen.
- [object ScaleFadeAnimation](./scalefadeanimation.md)
  The animation in which a component scales up and fades into view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/appearanimation)*