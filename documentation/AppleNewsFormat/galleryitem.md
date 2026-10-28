# GalleryItem

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

An object used in a gallery or mosaic component for displaying an individual image.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object GalleryItem
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

## Discussion

Use an array of `GalleryItem` objects to define the individual items used in a gallery or mosaic component. When the user taps an image in a gallery or mosaic to see it full-screen (as shown in the following figure), the caption from the caption descriptor property is shown. Note that this is different from the [`Caption`](./caption.md) component.

![Screenshot of a full screen gallery image with a caption.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-4085707@2x.png)

This object can be used in [`Gallery`](./gallery.md) and [`Mosaic`](./mosaic.md).

### Example

```json
{
  "components": [
    {
      "role": "gallery",
      "items": [
        {
          "URL": "bundle://gallery-01.jpg",
          "caption": "Thanks to the record drought, mountain lions have begun to descend from the peaks, sometimes into urban settings."
        },
        {
          "URL": "bundle://gallery-02.jpg",
          "caption": "Coyotes are also seen in cities more often."
        },
        {
          "URL": "bundle://gallery-03.jpg",
          "explicitContent": true
        }
      ]
    }
  ]
}
```

## Properties

- `URL` (uri) *(required)*: The `URL` of an image to display in a gallery or mosaic.

  Image URLs can begin with `http://`, `https://`, or `bundle://`. If the image URL begins with `bundle://`, the image file must be in the same directory as the document.

  Encode image filenames as `URLs`.

  See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `accessibilityCaption` (string): A caption that describes the image. The text is used for VoiceOver. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
- `caption` ((CaptionDescriptor | string)): A caption that describes the image. The article displays this text when the image is full screen, and VoiceOver uses this text if you don’t provide `accessibilityCaption` text. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. The caption text doesn’t appear in the main article view. To display a caption in the main article view, use the [`Caption`](./caption.md) component.

  **Allowed Types**: `CaptionDescriptor`, `string`
- `explicitContent` (boolean): A Boolean value that indicates the image may contain explicit content.

## See Also

### Related Documentation
- [Adding a Gallery of Images](../AppleNews/adding-a-gallery-of-images.md)
  Display three images as a sequential gallery.
- [Adding a Mosaic of Images](../AppleNews/adding-a-mosaic-of-images.md)
  Display five images as mosaic tiles.
### Galleries and Mosaics
- [object Gallery](./gallery.md)
  The component for displaying a sequence of images in a specific order as a horizontal strip.
- [object Mosaic](./mosaic.md)
  The component for displaying a set of images as tiles in no particular order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/galleryitem)*