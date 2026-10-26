# EmbedWebVideo

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding a web video from Dailymotion, Vimeo, or YouTube.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object EmbedWebVideo
```

## Mentions

- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)

#### Discussion

Use the `embedwebvideo` component to include a video from Dailymotion, Vimeo, or YouTube by specifying a URL for the video. Users can control playback and watch the video from inside the article. To include other types of videos in your article, use the [`Video`](./video.md) component.

##### Example

```json
{
  "components": [
    {
      "role": "embedwebvideo",
      "aspectRatio": 1.777,
      "URL": "https://www.youtube.com/embed/_p8AsQhaVKI",
      "caption": "Apple - WWDC 2015",
      "accessibilityCaption": "See the announcement of Apple Music, get a preview of OS X v10.11 and iOS 9, and learn what’s next for Apple Watch and developers."
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `embedwebvideo` or `embedvideo` for this component.

  **Allowed Values**: `embedwebvideo`, `embedvideo`
- `URL` (uri) *(required)*: The URL of the embeddable video to display (the Dailymotion, Vimeo, or YouTube embed link). The embed `URL` is usually different from the standard video `URL`.

  A Dailymotion embed `URL` typically looks like this: `https://geo.dailymotion.com/player.html?video=x84sh87`

  A Vimeo embed `URL` typically looks like this: `https://player.vimeo.com/video/121450839`

  A YouTube embed `URL` typically looks like this: `https://www.youtube.com/embed/0qwALOOvUik`
- `accessibilityCaption` (string): A caption that describes the content of the embedded web video. The text is used for VoiceOver. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `aspectRatio` (number): The aspect ratio of the video: width divided by height. The aspect ratio determines the height of the video player.

  When this property is omitted, the video player will have a 16:9 aspect ratio (1.777), and videos with ratios other than 16:9 will automatically be letterboxed.

  **Default**: `1.777`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `caption` (string): A caption that describes the content of the embedded web video. This text is used by VoiceOver if `accessibilityCaption` is not provided, or it can be shown when the embedded web video cannot be played.  For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility.
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `explicitContent` (boolean): A Boolean value that indicates that the embedded web video may contain explicit content.
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You need an identifier for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define layout, size and position are based on various factors, such as the device type, the length of the content, and the role of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that is defined at the top level of the document.

  The `none` value is used for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Audio and Video
- [object Audio](./audio.md)
  The component for adding a playable audio clip.
- [object Music](./music.md)
  The component for adding a playable music file.
- [object Podcast](./podcast.md)
  The component for adding a Podcast show or episode.
- [object Video](./video.md)
  The component for adding a video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/embedwebvideo)*