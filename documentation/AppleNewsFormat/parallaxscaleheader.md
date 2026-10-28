# ParallaxScaleHeader

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The scene that gives the impression of a parallax effect by zooming out and scrolling slightly more slowly than the person’s action.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ParallaxScaleHeader
```

## Mentions

- [Adding a Scene to a Chapter or a Section Header](../AppleNews/adding-a-scene-to-a-chapter-or-a-section-header.md)

## Discussion

In the `ParallaxScale` scene, as the person scrolls down (away from the header), the background of the `header` component zooms out and scrolls slightly slower than the person, giving the impression of a parallax effect, as shown in [this video](https://developer.apple.com/apple-news/videos/parallax-scale.mp4).

You can use a `parallax_scale` scene with a s`ection` or c`hapter` component that has a child `header` component. (The `section` or `chapter` component must contain a component with a `role` of `header`.)

> 💡 **Tip**:  When you use parallax behavior, you might notice text becoming illegible as it covers an image. You can fix this easily, and create a cleaner, more legible article, by adding a background color.

### Example

```json
{
  "components": [
    {
      "role": "section",
      "scene": {
        "type": "parallax_scale"
      },
      "components": [
        {
          "role": "header",
          "style": {
            "fill": {
              "type": "image",
              "URL": "bundle://header.jpg",
              "fillMode": "cover",
              "verticalAlignment": "top",
              "horizontalAlignment": "center"
            }
          },
          "layout": {
            "minimumHeight": "75cw"
          },
          "components": [
            {
              "role": "title",
              "text": "Article Title",
              "textStyle": {
                "textAlignment": "center"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

## Properties

- `type` (string) *(required)*: This scene always has the type `parallax_scale`.

  Version 1.0

  **Allowed Values**: `parallax_scale`

## Relationships

### Inherits From
- [Scene](./scene.md)

## See Also

### Scene Types
- [object Scene](./scene.md)
  A combination of animations and behaviors to use in sections and chapters that have headers.
- [object FadingStickyHeader](./fadingstickyheader.md)
  The scene that briefly keeps a header at the top of the screen as the person scrolls through the article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/parallaxscaleheader)*