# Portrait

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for including an image of a person.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Portrait
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)
- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)

## Discussion

Use the `portrait` component to display the image of a person in an article. Other components are available for other types of images, such as [`Figure`](./figure.md), [`Photo`](./photo.md), and [`Logo`](./logo.md).

See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).

### Example

```json
{
  "components": [
    {
      "role": "portrait",
      "URL": "bundle://louis-armstrong.jpg",
      "caption": "Louis Armstrong, jazz trumpeter (August 4, 1901-July 6, 1971)"
    }
  ]
}
```

## Properties

- `role` (string) *(required)*: Always `portrait` for this component.

  **Allowed Values**: `portrait`
- `URL` (uri) *(required)*: The `URL` of an image file.

  Image URLs can begin with `http://`, `https://`, or `bundle://`. If the image URL begins with `bundle://`, the image file must be in the same directory as the document.

  Encode image filenames as URLs.

  See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `accessibilityCaption` (string): A caption that describes the portrait.  VoiceOver uses this text. For more information about VoiceOver, see the [Vision](https://www.apple.com/accessibility/vision/) page in Accessibility. If you don’t provide `accessibilityCaption`, VoiceOver uses the `caption` value.
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

### Images
- [object Image](./image.md)
  The component for displaying JPEG, WebP, PNG, or GIF images.
- [object Photo](./photo.md)
  The component for including a photograph.
- [object Figure](./figure.md)
  The component for including a figure.
- [object Logo](./logo.md)
  The component for including a logo image.
- [object ReplicaAdvertisement](./replicaadvertisement.md)
  The component for delivering digital versions of print advertisements.
- [object CaptionDescriptor](./captiondescriptor.md)
  The object you use in image components for displaying captions when the image is full-screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/portrait)*