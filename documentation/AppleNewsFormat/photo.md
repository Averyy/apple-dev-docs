# Photo

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for including a photograph.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Photo
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)
- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)

## Discussion

Use the `photo` component to display a photograph in an article. A `photo` component is optimized for displaying photographs. Other components are available for other types of images, such as [`Figure`](./figure.md), [`Portrait`](./portrait.md), and [`Logo`](./logo.md).

See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).

### Example

```json
{
  "components": [
    {
      "role": "title",
      "text": "Apple News Format"
    },
    {
      "role": "body",
      "text": "Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
    },
    {
      "role": "photo",
      "URL": "bundle://image.jpg"
    }
  ]
}
```

## Properties

- `URL` (uri) *(required)*: The URL of an image file.

  Image URLs can begin with `http://`, `https://`, or `bundle://`. If the image URL begins with `bundle://`, the image file must be in the same directory as the document.

  Encode image filenames as URLs.

  See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `role` (string) *(required)*: Always `photo` for this component.

  **Allowed Values**: `photo`
- `accessibilityCaption` (string): A caption that describes the photo.  VoiceOver uses this text. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
- `additions` ([ComponentLink]): An array of `ComponentLink` objects you can use to create a `ComponentLink`, allowing a link to anywhere in News.
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `caption` ((CaptionDescriptor | string)): A caption that describes the image. The article displays this text when the image is full screen, and VoiceOver uses this text if you don’t provide `accessibilityCaption` text. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. The caption text doesn’t appear in the main article view. To display a caption in the main article view, use the [`Caption`](./caption.md) component.

  **Allowed Types**: `CaptionDescriptor`, `string`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `explicitContent` (boolean): A Boolean value that indicates the image may contain explicit content.
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use     `identifier`, it must be unique across the entire document. You need an `identifier` for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define `layout`, size and position are based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Related Documentation
- [Adding an Image and Captions](../AppleNews/adding-an-image-and-captions.md)
  Create a photo that extends to both edges of the display, with captions that appear in the article layout and in full-screen view.
### Images
- [object Image](./image.md)
  The component for displaying JPEG, WebP, PNG, or GIF images.
- [object Figure](./figure.md)
  The component for including a figure.
- [object Portrait](./portrait.md)
  The component for including an image of a person.
- [object Logo](./logo.md)
  The component for including a logo image.
- [object ReplicaAdvertisement](./replicaadvertisement.md)
  The component for delivering digital versions of print advertisements.
- [object CaptionDescriptor](./captiondescriptor.md)
  The object you use in image components for displaying captions when the image is full-screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/photo)*