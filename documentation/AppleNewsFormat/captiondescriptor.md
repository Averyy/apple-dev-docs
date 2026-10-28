# CaptionDescriptor

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object you use in image components for displaying captions when the image is full-screen.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object CaptionDescriptor
```

## Mentions

- [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md)
- [Using Markdown with Apple News Format](../AppleNews/using-markdown-with-apple-news-format.md)

## Discussion

Use a `CaptionDescriptor` object to provide a caption or attribution for an image that’s displayed full screen. You can use a caption descriptor with a [`Figure`](./figure.md), [`Portrait`](./portrait.md), or [`Photo`](./photo.md) component, and also with the individual items in a [`Gallery`](./gallery.md) or [`Mosaic`](./mosaic.md) component.

You can use this object in [`Figure`](./figure.md), [`Portrait`](./portrait.md), [`Photo`](./photo.md), and [Gallery Item](https://developer.apple.com/library/archive/documentation/General/Conceptual/Apple_News_Format_Ref/GalleryItem.html#//apple_ref/doc/uid/TP40015408-CH63).

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
          "caption": {
            "text": "<i>Steenbok</i> typically lie low in vegetation cover at the first sign of threat.",
            "format": "html"
          }
        }
      ]
    }
  ]
}
```

## Properties

- `text` (string) *(required)*: The text to display in the caption, including any formatting tags or markup, depending on the format property.
- `additions` ([Addition]): An array of `Link` objects that provide additional information for ranges of the caption text in the text property.

  If you set format to `html` or `markdown`, Apple News Format doesnʼt support `Additions` or `InlineTextStyles`.
- `format` (string): The formatting or markup method applied to the text.

  If you set format to `htm`l or `markdown`, Apple News Format doesn’t support `Additions` or `InlineTextStyles`.

  **Allowed Values**: `markdown`, `html`, `none`
- `inlineTextStyles` ([InlineTextStyle]): An array of `InlineTextStyle` objects you apply to ranges of the caption’s text.

  Apple News Format ignores `InlineTextStyles` when `format` is set to `html` or `markdown`.
- `textStyle` ((ComponentTextStyle | string)): An inline `ComponentTextStyle` object that contains styling information, or a string reference to a component text style object that you define at the top level of the document.

  **Allowed Types**: `ComponentTextStyle`, `string`

## See Also

### Related Documentation
- [Adding an Image and Captions](../AppleNews/adding-an-image-and-captions.md)
  Create a photo that extends to both edges of the display, with captions that appear in the article layout and in full-screen view.
- [Adding a Gallery of Images](../AppleNews/adding-a-gallery-of-images.md)
  Display three images as a sequential gallery.
- [Adding a Mosaic of Images](../AppleNews/adding-a-mosaic-of-images.md)
  Display five images as mosaic tiles.
### Images
- [object Image](./image.md)
  The component for displaying JPEG, WebP, PNG, or GIF images.
- [object Photo](./photo.md)
  The component for including a photograph.
- [object Figure](./figure.md)
  The component for including a figure.
- [object Portrait](./portrait.md)
  The component for including an image of a person.
- [object Logo](./logo.md)
  The component for including a logo image.
- [object ReplicaAdvertisement](./replicaadvertisement.md)
  The component for delivering digital versions of print advertisements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/captiondescriptor)*