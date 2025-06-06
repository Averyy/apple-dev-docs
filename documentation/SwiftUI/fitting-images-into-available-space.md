# Fitting images into available space

**Framework**: SwiftUI

Adjust the size and shape of images in your app’s user interface by applying view modifiers.

#### Overview

Image sizes vary widely, from single-pixel PNG files to digital photography images with millions of pixels. Because device sizes also vary, apps commonly need to make runtime adjustments to image sizes so they fit within the visible user interface. SwiftUI provides modifiers to scale, clip, and transform images to fit your interface perfectly.

##### Scale a Large Image to Fit Its Container Using Resizing

Consider the image `Landscape_4.jpg`, a photograph with the dimensions 4032 x 3024, showing a water wheel, the surrounding building, and the sky above.

![A photo looking up at a water wheel and its surrounding building, with the sky and clouds above.](https://docs-assets.developer.apple.com/published/9171798f66624fb18c9f216d85d85ad3/SwiftUI-FIIAS-Landscape_4-original.jpg)

The following example loads the image directly into an [`Image`](image.md) view, and then places it in a 300 x 400 point frame, with a blue border:

```swift
    Image("Landscape_4")
        .frame(width: 300, height: 400, alignment: .topLeading)
        .border(.blue)
```

As seen in the following screenshot, the image data loads at full size into the view, so only the clouds from the upper left of the original image are visible. Because the image renders at full size, and the blue frame is smaller than the original image, the image displays beyond the area bounded by the frame.

![An image that shows a frame with a blue border overlaid on an image of a water wheel. The image is so much larger than the available space that only a portion of the sky and clouds from the upper left of the original image is visible. The image goes beyond the borders of the outline.](https://docs-assets.developer.apple.com/published/3f9b1cd8d9d65f9ffba1dcba86eca2a7/SwiftUI-FIIAS-unscaled%402x.png)

To fix this, you need to apply two modifiers to the `Image`:

- [`resizable(capInsets:resizingMode:)`](image/resizable(capinsets:resizingmode:).md) tells the image view to adjust the image representation to match the size of the view. By default, this modifier scales the image by reducing the size of larger images and enlarges images smaller than the view. By itself, this modifier scales each axis of the image independently.
- [`aspectRatio(_:contentMode:)`](view/aspectratio(_:contentmode:).md) corrects the behavior where the image scaling is different for each axis. This preserves the image’s original aspect ratio, using one of two strategies defined by the [`ContentMode`](contentmode.md) enumeration. [`ContentMode.fit`](contentmode/fit.md) scales the image to fit the view size along one axis, possibly leaving empty space along the other axis. [`ContentMode.fill`](contentmode/fill.md) scales the image to fill the entire view. ```swift
  Image("Landscape_4")
      .resizable()
      .aspectRatio(contentMode: .fit)
      .frame(width: 300, height: 400, alignment: .topLeading)
      .border(.blue)
```

![An image that shows a frame with a blue border overlaid on an image of a water wheel. The water wheel image is scaled to fit the width of the containing rectangle. Empty space extends from the bottom of the image to the bottom of the rectangle.](https://docs-assets.developer.apple.com/published/366e823084f58a2b5a02ca34a6139afa/SwiftUI-FIIAS-resizeToFit%402x.png)

##### Keep Image Data Inside the Views Bounds Using Clipping

If you use [`ContentMode.fill`](contentmode/fill.md) when scaling an image, a portion of an image may extend beyond the view’s bounds, unless the view matches the image’s aspect ratio exactly. The following example illustrates this problem:

```swift
    Image("Landscape_4")
        .resizable()
        .aspectRatio(contentMode: .fill)
        .frame(width: 300, height: 400, alignment: .topLeading)
        .border(.blue)
```

![An image that shows a frame with a blue border overlaid on an image of a water wheel. The water wheel image fills its entire space vertically, and extends past the right edge of the frame horizontally.](https://docs-assets.developer.apple.com/published/ddb655ddd8af262670b93b990ec5226d/SwiftUI-FIIAS-resizeToFill-noClip%402x.png)

To prevent this problem, add the [`clipped(antialiased:)`](view/clipped(antialiased:).md) modifier. This modifier simply cuts off excess image rendering at the bounding frame of the view. Optionally, you can add an antialiasing behavior to apply smoothing to the edges of the clipping rectangle; this parameter defaults to `false`. The following example shows the effect of adding clipping to the previous fill-mode example:

```swift
    Image("Landscape_4")
        .resizable()
        .aspectRatio(contentMode: .fill)
        .frame(width: 300, height: 400, alignment: .topLeading)
        .border(.blue)
        .clipped()
```

![An image that shows a frame with a blue border overlaid on an image of a water wheel. The water wheel image fills the entire frame vertically and horizontally. The right side of the image is cut off at the right side of the rectangle.](https://docs-assets.developer.apple.com/published/677c185016ebecdd1c2a9aec138aa828/SwiftUI-FIIAS-resizeToFill-clipped%402x.png)

##### Use Interpolation Flags to Adjust Rendered Image Quality

Rendering an image at anything other than its original size requires : using the existing image data to approximate a representation at a different size. Different approaches to performing interpolation have different trade-offs between computational complexity and visual quality of the rendered image. You can use the [`interpolation(_:)`](image/interpolation(_:).md) modifier to provide a hint for SwiftUI rendering behavior.

It’s easier to see the effect of interpolation when scaling a smaller image into a larger space, because the rendered image requires more image data than is available. Consider the following example, which renders a 34 x 34 image named `dot_green` into the same 300 x 400 container frame as before:

```swift
    Image("dot_green")
        .resizable()
        .interpolation(.none)
        .aspectRatio(contentMode: .fit)
        .frame(width: 300, height: 400, alignment: .topLeading)
        .border(.blue)
```

Passing the [`Image.Interpolation.none`](image/interpolation/none.md) value to [`interpolation(_:)`](image/interpolation(_:).md) produces a highly pixelated image when rendered.

![A green dot with a darker green border, scaled to many times its original size and highly pixelated.](https://docs-assets.developer.apple.com/published/daad34a379a26fb3aa4a2727cd3530b9/SwiftUI-FIIAS-smallImage-interpolation-none%402x.png)

If you change the interpolation value to [`Image.Interpolation.medium`](image/interpolation/medium.md), SwiftUI smoothes out the pixel data to produce an image that isn’t as pixelated:

![A green dot with a darker green border, scaled to many times its original size, but with its edges smoothed.](https://docs-assets.developer.apple.com/published/0b5ba6711c01bc4324ee89397fb1798b/SwiftUI-FIIAS-smallImage-interpolation-medium%402x.png)

> 💡 **Tip**: You can also specify interpolation behavior when scaling images down, to ensure the highest quality image possible, fastest rendering time, or a behavior in between.

You can also specify interpolation behavior when scaling images down, to ensure the highest quality image possible, fastest rendering time, or a behavior in between.

##### Fill a Space with a Repeating Image Using Tiling

When you have an image that’s much smaller than the space you want to render it into, another option  to fill the space is : repeating the same image over and over again. To tile an image, pass the [`Image.ResizingMode.tile`](image/resizingmode/tile.md) parameter to the [`resizable(capInsets:resizingMode:)`](image/resizable(capinsets:resizingmode:).md) modifier:

```swift
    Image("dot_green")
        .resizable(resizingMode: .tile)
        .frame(width: 300, height: 400, alignment: .topLeading)
        .border(.blue)
```

![A rectangular blue outline, 300 by 400. The repeated green dot image fills its entire space horizontally and vertically.](https://docs-assets.developer.apple.com/published/eddc5cef6d4b0fd479272e0d25df8d7c/SwiftUI-FIIAS-smallImage-tile%402x.png)

Tiling can be particuarly useful when using an image that, when placed end-to-end with copies of itself, creates a larger pattern with no visual discontinuities.

## See Also

- [func imageScale(Image.Scale) -> some View](view/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [var imageScale: Image.Scale](environmentvalues/imagescale.md)
  The image scale for this environment.
- [Image.Scale](image/scale.md)
  A scale to apply to vector images relative to text.
- [Image.Orientation](image/orientation.md)
  The orientation of an image.
- [Image.ResizingMode](image/resizingmode.md)
  The modes that SwiftUI uses to resize an image to fit within its containing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fitting-images-into-available-space)*