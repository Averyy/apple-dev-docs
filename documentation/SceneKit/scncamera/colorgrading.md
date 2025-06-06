# colorGrading

**Framework**: SceneKit  
**Kind**: property

A texture for applying color grading effects to the entire rendered scene.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var colorGrading: SCNMaterialProperty { get }
```

#### Discussion

The [`contents`](scnmaterialproperty/contents.md) value for this material property must be a 3D color lookup table, or a 2D texture image that represents such a table arranged in a horizontal strip.

A lookup table is a cube of color values: the red, green, and blue components of an input color map to the x, y, and z coordinates of a location in that cube, and at that location in the cube is a corresponding output color. You can provide data in this cubic format as a Metal texture with the [`MTLTextureType.type3D`](https://developer.apple.com/documentation/Metal/MTLTextureType/type3D) texture type.

The 2D representation of a 3D color cube is an arrangement of slices: for example, a 16 x 16 x 16 color cube becomes a horizontal strip of 16 squares, each 16 x 16 pixels (that is, a 256 x 16 image). Each square contains a gradation of red and green components, and together the 16 squares form a gradation for the blue component. To provide a 2D representation of a color cube, set this material property’s [`contents`](scnmaterialproperty/contents.md) value to an image.

By using a color table, you can easily create custom color effects that apply to an entire rendered scene:

1. Create a basic color table image such as [`Figure 1`](scncamera/1644114-colorgrading#1965935.md), where the color value for each R, G, and B coordinate in the cube is the corresponding RGB color.

![None](https://docs-assets.developer.apple.com/published/ecb529f74d64281e39ed2ba259de707a/media-1965935.png) 2. Use an image editor to create the color effect you want using some other image—such as a screenshot of your game. Apply only effects that affect pixel colors without modifying pixel positions. (For example, you can use hue/saturation, color curves, or color matrix filters, but not blur or distort filters.)

![None](https://docs-assets.developer.apple.com/published/144a43cee37c0db36c5b5659739e0ce8/media-1965936%402x.png) 3. Apply the same color effect you created in step 2 to your basic color table image. You can even perform these steps together: paste the basic color table into your game screenshot, apply an effect to the combined picture, then crop the picture to just the modified color table. [`Figure 2`](scncamera/1644114-colorgrading#1965936.md) shows an example effect. 4. Assign your customized color table image (such as the example in [`Figure 3`](scncamera/1644114-colorgrading#1965937.md)) to this property. When rendering, SceneKit looks up the RGB values for each pixel in the rendered scene, and displays the corresponding color values from the color table.

![None](https://docs-assets.developer.apple.com/published/ecb529f74d64281e39ed2ba259de707a/media-1965937.png)

To enable this behavior, you must first enable the [`wantsHDR`](scncamera/wantshdr.md) setting.

## See Also

- [var contrast: CGFloat](scncamera/contrast.md)
  An adjustment factor to apply to the overall visual contrast of the rendered scene.
- [var saturation: CGFloat](scncamera/saturation.md)
  An adjustment factor to apply to the overall color saturation of the rendered scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/colorgrading)*