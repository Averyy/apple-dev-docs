# Mosaic

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The component for displaying a set of images as tiles in no particular order.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Mosaic
```

## Mentions

- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

#### Discussion

Use the `Mosaic` component to display a group of images in no particular order. (To display a group of images in a particular order, use the `Gallery` component.) Users can tap an image in a mosaic to see a full-screen version.

> **Note**:  If you use an animated GIF as an image in a Mosaic, the animation plays only when the image is full screen.

![Screenshot of an Apple News article with a mosaic on iPad.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-3591437@2x.png)

##### Example

```json
{
  "components": [
    {
      "role": "title",
      "text": "Article Title"
    },
    {
      "role": "body",
      "format": "html",
      "text": "Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
    },
    {
      "role": "mosaic",
      "items": [
        {
          "URL": "bundle://mosaic-01.jpg",
          "caption": "A caption for the first image in the mosaic."
        },
        {
          "URL": "bundle://mosaic-02.jpg",
          "caption": "A caption for the second image in the mosaic."
        },
        {
          "URL": "bundle://mosaic-03.jpg",
          "caption": "A caption for the third image in the mosaic."
        },
        {
          "URL": "bundle://mosaic-04.jpg",
          "caption": "A caption for the fourth image in the mosaic."
        },
        {
          "URL": "bundle://mosaic-05.jpg",
          "caption": "A caption for the fifth image in the mosaic."
        }
      ]
    }
  ]
}
```

## Properties

- `items` ([GalleryItem]) *(required)*: An array of the images that appear in the mosaic. The order you use in the array may affect layout and positioning in the mosaic, depending on the device or width.

  Mosaic items can be JPEG (with `.jpg` or `.jpeg` extension), WebP, PNG, or GIF images. If the GIF is animated, the animation plays only in full screen.

  > **Note**:  If you add an animated WebP image, Apple News removes the animation from the WebP image.
- `role` (string) *(required)*: Always `mosaic` for this component.

  **Allowed Values**: `mosaic`
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation you apply to the component.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  Use the none value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `Behavior`, `string("none")`
- `conditional` ((ConditionalComponent | [ConditionalComponent])): An instance or array of component properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponent`, `[ConditionalComponent]`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `identifier` (string): An optional unique identifier for this component. If you use `identifier`, it must be unique across the entire document. You  need an `identifier` for your component if you want to anchor other components to it.
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that is defined at the top level of the document.

  If you don’t define layout, size and position are based on various factors, such as the device type, the length of the content, and the role of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  Use the `none` value for conditional design elements. Adding it here has no effect.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherits From
- [Component](./component.md)

## See Also

### Related Documentation
- [Adding a Mosaic of Images](../AppleNews/adding-a-mosaic-of-images.md)
  Display five images as mosaic tiles.
### Galleries and Mosaics
- [object Gallery](./gallery.md)
  The component for displaying a sequence of images in a specific order as a horizontal strip.
- [object GalleryItem](./galleryitem.md)
  An object used in a gallery or mosaic component for displaying an individual image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/mosaic)*