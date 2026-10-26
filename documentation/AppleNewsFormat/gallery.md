# Gallery

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for displaying a sequence of images in a specific order as a horizontal strip.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Gallery
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

#### Discussion

Use the `Gallery` component for sequences of images where the ordering of the items is important to the story. To display images in no specific order, use the [`Mosaic`](./mosaic.md) component. People can swipe to view the images in a gallery as shown in this example:

![Screenshot of an Apple News article with a gallery on iPad.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-3591432@2x.png)

##### Example

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

- `items` ([GalleryItem]) *(required)*: An array of the images that appear in the gallery. The order you use in the array is the order of the images in the gallery.

  Gallery items can be JPEG (with `.jpg` or .`jpeg` extension), WebP, PNG, or GIF images. If the GIF is animated, the animation plays only in full screen.

  > **Note**:  If you add an animated WebP image, Apple News removes the animation from the WebP image.
- `role` (string) *(required)*: Always `gallery` for this component.

  **Allowed Values**: `gallery`
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
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You  need an `identifier` for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If `layout` is not defined, size and position will be based on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Related Documentation
- [Adding a Gallery of Images](../AppleNews/adding-a-gallery-of-images.md)
  Display three images as a sequential gallery.
### Galleries and Mosaics
- [object Mosaic](./mosaic.md)
  The component for displaying a set of images as tiles in no particular order.
- [object GalleryItem](./galleryitem.md)
  An object used in a gallery or mosaic component for displaying an individual image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/gallery)*