# Instagram

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding an Instagram post.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Instagram
```

#### Discussion

Use the `instagram` object to include an Instagram post by specifying a `URL` for the post.

##### Example

```json
{
  "components": [
    {
      "role": "title",
      "text": "iTunes"
    },
    {
      "role": "body",
      "text": "iTunes is the best way to organize and enjoy the music, movies, and TV shows you already have — and shop for the ones you want."
    },
    {
      "role": "heading2",
      "text": "Instagram"
    },
    {
      "role": "instagram",
      "URL": "https://www.instagram.com/p/BpiRTBYlkY5/"
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `instagram` for this component.

  **Allowed Values**: `instagram`
- `URL` (uri) *(required)*: The URL of the Instagram post you want to embed.

  Apple News supports the following URL formats for Instagram posts:

  - `https://www.instagram.com/p/{media-shortcode}`
  - `https://www.instagram.com/tv/{media-shortcode}`
  - `https://www.instagram.com/reel/{media-shortcode}`
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You need an identifier for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define `layout`, size and position are based on various factors, such as the device type, the length of the content, and the role of this component

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Social Media
- [object FacebookPost](./facebookpost.md)
  The component for adding a Facebook post.
- [object TikTok](./tiktok.md)
  The component for adding a TikTok post.
- [object Tweet](./tweet.md)
  The component for adding a Tweet that was posted to Twitter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/instagram)*