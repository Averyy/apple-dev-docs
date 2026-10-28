# VideoFill

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for adding a video background fill to a component.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object VideoFill
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)
- [Adding a Video](../AppleNews/adding-a-video.md)
- [Applying a Background to a Component](../AppleNews/applying-a-background-to-a-component.md)

## Discussion

Use the `VideoFill` object to fill a component’s background with a video that starts playing automatically with no audio. You can specify whether the video scrolls or stays in one place when a person scrolls, what happens when the video ends, and the position of the video within the component. You can also supply an image to display when the video isn’t playing.

You can use this object in [`ComponentStyle`](./componentstyle.md).

### Example

```json
{
  "components": [
    {
      "role": "container",
      "style": "exampleComponentStyle",
      "layout": {
        "ignoreDocumentMargin": true,
        "minimumHeight": 150
      },
      "components": [
        {
          "role": "title",
          "text": "Season Preview: Nobody Saw This Coming",
          "anchor": {
            "targetAnchorPosition": "center"
          }
        }
      ]
    }
  ],
  "componentStyles": {
    "exampleComponentStyle": {
      "fill": {
        "type": "video",
        "URL": "https://example.com/hls/2014/fded0-1077dae/main.m3u8",
        "stillURL": "bundle://video-still.jpg",
        "fillMode": "cover",
        "verticalAlignment": "top"
      }
    }
  }
}
```

## Properties

- `stillURL` (uri) *(required)*: The URL of the image file to use as a still image when the video is not playing.

  Image URLs can begin with `http://`, `https://`, or `bundle://`. If the image URL begins with `bundle://`, the referenced image file must be in the same directory as the document.

  Encode image filenames as `URLs`.

  See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `URL` (uri) *(required)*: The URL of a video file that you can play using AV Player. HTTP Live Streaming (HLS) is highly recommended (.M3U8). For more information about HLS, see  [HTTP Live Streaming](https://developer.apple.com/streaming/).
- `attachment` (string): A string that indicates how the fill behaves when a person scrolls.

  Valid values:

  - `scroll` (default). The fill scrolls along with its component.
  - `fixed`. The fill stays at a fixed position within the viewport.

  **Default**: `scroll`; **Allowed Values**: `fixed`, `scroll`
- `fillMode` (string): Indicates how Apple News displays the video fill.

  Valid values:

  - `fit`: Preserves the video aspect ratio and fits the fill within the component.
  - `cover` (default): Preserves the video aspect ratio and fills to the boundaries of the component.

  **Default**: `cover`; **Allowed Values**: `fit`, `cover`
- `horizontalAlignment` (string): Sets the horizontal alignment of the video fill within its component.

  Valid values:

  - `left`: Aligns the left edge of the fill with the left edge of the component.
  - `center` (default): Aligns the horizontal center of the fill with the center of the component.
  - `right`: Aligns the right edge of the fill with the right edge of the component.

  You can use `fillMode` with `horizontalAlignment` to achieve the effect you want. For example, set `fillMode` to `fit` and `horizontalAlignment` to `left` to fit the video based on its aspect ratio and also align the left edge of the fill with the left edge of the component. Or set `fillMode` to `cover` and `horizontalAlignment` to `right` to scale the video horizontally and also align the right edge of the fill with the right edge of the component.

  **Default**: `center`; **Allowed Values**: `left`, `center`, `right`
- `loop` (boolean): When `true,` it specifies that the video starts over again when it reaches the end.

  **Default**: `true`
- `type` (string) *(required)*: Describes the type of fill. Use `video` for a video fill.

  **Allowed Values**: `video`
- `verticalAlignment` (string): Sets the vertical alignment of the video fill within its component.

  Valid values:

  - `top`: Aligns the top of the fill with the top edge of the component.
  - `center` (default): Aligns the vertical center of the fill with the center of the component.
  - `bottom`: Aligns the bottom of the fill with the bottom edge of the component.

  You can use `fillMode` with `verticalAlignment` to achieve the effect you want. For example, `set` `fillMode` to `fit` and `verticalAlignment` to `top` to fit the video based on its aspect ratio and also align the top of the fill with the top edge of the component. Or set `fillMode` to cover and `verticalAlignment` to `top` to scale the video vertically and also align the top of the fill with the top edge of the component.

  **Default**: `center`; **Allowed Values**: `top`, `center`, `bottom`

## Relationships

### Inherits From
- [Fill](./fill.md)

## See Also

### Backgrounds for Components
- [Applying a Background to a Component](../AppleNews/applying-a-background-to-a-component.md)
  Change the appearance of the backgrounds in your article.
- [object ImageFill](./imagefill.md)
  The object for adding an image background fill to a component.
- [object RepeatableImageFill](./repeatableimagefill.md)
  The object for adding a background image that Apple News can repeat.
- [object LinearGradientFill](./lineargradientfill.md)
  The object for displaying a linear gradient as a component background.
- [object GradientFill](./gradientfill.md)
  The properties all gradient fill types share.
- [object Fill](./fill.md)
  The object for setting a fill type and attachment for a component’s background fill.
- [object ColorStop](./colorstop.md)
  The object for specifying the color and location for a color stop in a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/videofill)*