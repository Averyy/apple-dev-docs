# Music

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for adding a playable music file.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Music
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

## Discussion

Use the `Music` component to play an audio file. You can also include album art (or another image that represents the music).

See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).

### Example

```json
{
  "components": [
    {
      "role": "music",
      "URL": "http://www.example.com/files/sample.mp3",
      "imageURL": "bundle://album_cover.jpg",
      "caption": "Cosmic-Karmic by Retake Chorus"
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `music` for this component.

  **Allowed Values**: `music`
- `URL` (uri) *(required)*: The URL of an audio file (HTTP or HTTPS only). This component supports all [`AVPlayer`](../AVFoundation/avplayer.md) audio formats, including the following:

  - MP3: MPEG-1 audio layer 3
  - AAC: MPEG-4 Advanced Audio Coding
  - ALAC: Apple Lossless
  - HE-AAC: MPEG-4 High Efficiency AAC
- `accessibilityCaption` (string): A caption that describes the content of the audio file. The text is used for VoiceOver. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `caption` (string): A caption that describes the content of the audio file. This text is used by VoiceOver if `accessibilityCaption` is not provided, or it can be shown when the audio cannot be played.  For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility.
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `explicitContent` (boolean): A Boolean value that indicates that the audio may contain explicit content.
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You need an identifier for your component if you want to anchor other components to it.
- `imageURL` (uri): The URL of an image file that represents the audio file, such as a cover image.

  Image URLs can begin with `http://`, `https://`, or `bundle://`. If the image URL begins with `bundle://`, the image file must be in the same directory as the document.

  Encode image filenames as URLs.

  See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If you don’t define `layout`, size and position are based on various factors, such as the device type, the length of the content, and the `role` of this component..

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Audio and Video
- [object Audio](./audio.md)
  The component for adding a playable audio clip.
- [object Podcast](./podcast.md)
  The component for adding a Podcast show or episode.
- [object Video](./video.md)
  The component for adding a video.
- [object EmbedWebVideo](./embedwebvideo.md)
  The component for adding a web video from Dailymotion, Vimeo, or YouTube.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/music)*