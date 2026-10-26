# ImageFill

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for adding an image background fill to a component.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ImageFill
```

## Mentions

- [Applying a Background to a Component](../AppleNews/applying-a-background-to-a-component.md)
- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

#### Discussion

Use the `ImageFill` object to fill a component with a background image.

To avoid having the image cut off on different devices, calculate the minimum height needed for the image. For example, the following shows the minimum height calculation of a full display based on an image with dimensions 2184 x 1456 pixels:

100 * (height / width) + “cw”

100 * (1456 / 2184) + “cw”

“66.67cw”

For more information about the use of `cw`, see [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

> **Note**:  The image fill doesn’t open as a full-screen version when tapped.

You can use this object in [`ComponentStyle`](./componentstyle.md).

##### Create a Layered Effect with a Background

You can create a layered or collage effect by using a background image with a header container component. Create a header that contains the other components you want in the top section of your article, such as the `title` and `intro`, and then apply a background image to the `header` component. All content in the `header` component appears in front of the background, creating a layered effect.

##### Set a Fixed Image Fill

One of the most captivating effects in Apple News Format is the fixed image fill. With this background, the image stays still as a person scrolls, with the rest of the content in the article seeming to move independently of the image. As long as any part of the component containing the image is visible in the viewport, the image remains still.

To create this effect, use a [`ComponentStyle`](./componentstyle.md) object with `image` as the `fill` type, and then give the `attachment` property the value of `fixed`.

![Screenshot of an Apple News article with a fixed image fill on iPad.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-3597901@2x.png)

> 💡 **Tip**:  Use structural container components (such as `header`, `section`, and `container`) to have more control over backgrounds in your article. For example, you can specify backgrounds for the components inside the container as well as for the container itself.

##### Example

```json
{
  "components": [
    {
      "role": "container",
      "style": "exampleComponentStyle",
      "layout": {
        "minimumHeight": 150
      },
      "components": [
        {
          "role": "title",
          "text": "Drought",
          "anchor": {
            "targetAnchorPosition": "center"
          },
          "textStyle": {
            "fontSize": 60
          }
        }
      ]
    }
  ],
  "componentStyles": {
    "exampleComponentStyle": {
      "fill": {
        "type": "image",
        "URL": "bundle://image.jpg",
        "fillMode": "cover",
        "verticalAlignment": "top"
      }
    }
  }
}
```

## Properties

- `URL` (uri) *(required)*: The URL of the image file to use for filling the component.

  Image URLs can begin with `http://`, `https://`, or `bundle://`. If the image URL begins with `bundle://`, the referenced image file must be in the same directory as the document.

  Encode image filenames as URLs.

  See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `attachment` (string): A string that indicates how the fill behaves when a person scrolls.

  Valid values:

  - `scroll` (default). The fill scrolls along with its component.
  - `fixed`. The fill stays at a fixed position within the viewport.

  **Default**: `scroll`; **Allowed Values**: `fixed`, `scroll`
- `fillMode` (string): Indicates how Apple News displays the image fill.

  Valid values:

  - `fit`: Scales the image by aspect ratio to fit the component.
  - `cover:`(default): Scales the image by aspect ratio to completely fill the component.

  **Default**: `cover`; **Allowed Values**: `fit`, `cover`
- `horizontalAlignment` (string): Sets the horizontal alignment of the image fill within its component.

  Valid values:

  - `left`: Aligns the left edge of the fill with the left edge of the component.
  - `center` (default): Aligns the horizontal center of the fill with the center of the component.
  - `right`: Aligns the right edge of the fill with the right edge of the component.

  You can use `fillMode` with `horizontalAlignment` to achieve the effect you want. For example, set `fillMode` to `fit` and `horizontalAlignment` to `left` to fit the image based on its aspect ratio and also align the left edge of the fill with the left edge of the component. Or set `fillMode` to `cover` and `horizontalAlignment` to `right` to scale the image horizontally and also align the right edge of the fill with the right edge of the component.

  **Default**: `center`; **Allowed Values**: `left`, `center`, `right`
- `type` (string) *(required)*: The type of fill to apply. Always set this property to `image`.

  **Allowed Values**: `image`
- `verticalAlignment` (string): Sets the vertical alignment of the image fill within its component.

  Valid values:

  - `top`: Aligns the top of the fill with the top edge of the component.
  - `center` (default): Aligns the vertical center of the fill with the center of the component.
  - `bottom`: Aligns the bottom of the fill with the bottom edge of the component.

  You can use `fillMode` with `verticalAlignment` to achieve the effect you want. For example, set `fillMode` to `fit` and `verticalAlignment` to `top` to fit the image based on its aspect ratio and also align the top of the fill with the top edge of the component. Or set `fillMode` to `cover` and `verticalAlignment` to `top` to scale the image vertically and also align the top of the fill with the top edge of the component.

  **Default**: `center`; **Allowed Values**: `top`, `center`, `bottom`

## Relationships

### Inherits From
- [Fill](./fill.md)

## See Also

### Related Documentation
- [Creating a Layered Header](../AppleNews/creating-a-layered-header.md)
  Create a header with a caption that’s layered in front of an image.
- [Adding a Fixed Image Fill](../AppleNews/adding-a-fixed-image-fill.md)
  Add an image that remains stationary when the user scrolls.
### Backgrounds for Components
- [Applying a Background to a Component](../AppleNews/applying-a-background-to-a-component.md)
  Change the appearance of the backgrounds in your article.
- [object RepeatableImageFill](./repeatableimagefill.md)
  The object for adding a background image that Apple News can repeat.
- [object VideoFill](./videofill.md)
  The object for adding a video background fill to a component.
- [object LinearGradientFill](./lineargradientfill.md)
  The object for displaying a linear gradient as a component background.
- [object GradientFill](./gradientfill.md)
  The properties all gradient fill types share.
- [object Fill](./fill.md)
  The object for setting a fill type and attachment for a component’s background fill.
- [object ColorStop](./colorstop.md)
  The object for specifying the color and location for a color stop in a gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/imagefill)*