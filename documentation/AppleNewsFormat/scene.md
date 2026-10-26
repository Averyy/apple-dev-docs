# Scene

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

A combination of animations and behaviors to use in sections and chapters that have headers.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Scene
```

#### Discussion

A scene is a combination of animations and behaviors that lets you create special effects for the `section` and `chapter` components in an article. You don’t use the `Scene` object directly, but instead use the specific objects that extend scene:

- [`FadingStickyHeader`](./fadingstickyheader.md)
- [`ParallaxScaleHeader`](./parallaxscaleheader.md)

> 💡 **Tip**:  To use a scene, create a child `header` component within your section or chapter, and then specify which scene you want to use in the `scene` property of the section or chapter.

You can use this object in [`Chapter`](./chapter.md) and [`Section`](./section.md).

## Properties

- `type` (string) *(required)*: The type of scene. For example, `parallax_scale` for a Parallax Scale Header scene or `fading_sticky_header` for a Fading Sticky Header.

  Version 1.0

  **Allowed Values**: `fading_sticky_header`, `parallax_scale`

## Relationships

### Inherited By
- [FadingStickyHeader](./fadingstickyheader.md)
- [ParallaxScaleHeader](./parallaxscaleheader.md)

## See Also

### Scene Types
- [object FadingStickyHeader](./fadingstickyheader.md)
  The scene that briefly keeps a header at the top of the screen as the person scrolls through the article.
- [object ParallaxScaleHeader](./parallaxscaleheader.md)
  The scene that gives the impression of a parallax effect by zooming out and scrolling slightly more slowly than the person’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/scene)*