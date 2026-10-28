# Video

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding a video.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Video
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)
- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)

## Discussion

Use the `video` component to add a video to your article by specifying a video URL. Users can control playback and watch the video from inside the article. You can also include an image to display when the video is not playing. To include a video from Dailymotion, Vimeo, or YouTube, use the [`EmbedWebVideo`](./embedwebvideo.md) component instead of the `video` component.

See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).

### Example

```json
{
  "components": [
    {
      "role": "video",
      "URL": "https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8"
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `video` for this component.

  **Allowed Values**: `video`
- `URL` (uri) *(required)*: The `URL` of a video file that can be played using [`AVPlayer`](../AVFoundation/avplayer.md). HTTP Live Streaming (HLS) is highly recommended (.M3U8). For more information about HLS, see [HTTP Live Streaming](https://developer.apple.com/streaming/),
- `accessibilityCaption` (string): A caption that describes the content of the video file. The text is used for VoiceOver. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
- `allowsPrerollAds` (boolean): A Boolean value that determines if the video player displays a preroll advertisement before playback starts.

  **Default**: `true`
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
- `caption` (string): A caption that describes the content of the video file. This text is used by VoiceOver if `accessibilityCaption` is not provided, or it can be shown when the video cannot be played.  For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility.
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `explicitContent` (boolean): A Boolean value that indicates that the video or its still image may contain explicit content.
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You need an identifier for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define layout, size and position are based on various factors, such as the device type, the length of the content, and the role of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `stillURL` (uri): The `URL` of an image file that should be shown when the video has not yet been played.

  Image URLs can begin with `http://`, `https://`, or `bundle://`. If the image URL begins with `bundle://`, the image file must be in the same directory as the document.

  Encode image filenames as URLs.

  See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Related Documentation
- [Adding a Video](../AppleNews/adding-a-video.md)
  Add a video component inside the header component.
### Audio and Video
- [object Audio](./audio.md)
  The component for adding a playable audio clip.
- [object Music](./music.md)
  The component for adding a playable music file.
- [object Podcast](./podcast.md)
  The component for adding a Podcast show or episode.
- [object EmbedWebVideo](./embedwebvideo.md)
  The component for adding a web video from Dailymotion, Vimeo, or YouTube.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/video)*