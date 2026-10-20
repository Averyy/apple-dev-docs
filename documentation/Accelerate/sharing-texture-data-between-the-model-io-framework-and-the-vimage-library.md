# Sharing texture data between the Model I/O framework and the vImage library

**Framework**: Accelerate  
**Role**: Sample Code  
**Download**: [SharingTextureDataBetweenTheModelIOFrameworkAndTheVImageLibrary.zip](https://docs-assets.developer.apple.com/published/95d06baaab82/SharingTextureDataBetweenTheModelIOFrameworkAndTheVImageLibrary.zip)

Use Model I/O and vImage to composite a photograph over a computer-generated sky.

**Availability**:
- macOS 14.0+
- Xcode 15.0+

#### Overview

The [Model I/O](../ModelIO/ModelIO.md) framework provides the [`MDLTexture`](../ModelIO/mdltexture.md) class and its subclasses to generate procedural textures such as noise, normal maps, and realistic sky boxes.  This sample code project uses an [`MDLSkyCubeTexture`](../ModelIO/mdlskycubetexture.md) instance to generate a physically realistic simulation of a sunlit sky. The code uses the generated sky image as the background and a photograph of a building as the foreground.

The image below shows the final composition:

![A photograph of a skyscraper composited over a computer-generated](https://developer.apple.com/tutorials/images/com.apple.accelerate/img.png)

Using the UI, someone can define the parameters that control the sky simulation such as upper atmosphere scattering and sun elevation. Before exploring the code, try building and running the app to get familiar with the effect of the different parameters on the image.

##### Create the sky texture generator

The `ImageProvider` class declares constants for the source image’s dimensions and the [`MDLSkyCubeTexture`](../ModelIO/mdlskycubetexture.md) instance named `skyGenerator`:

```swift
let width: Int
var height: Int

let skyGenerator: MDLSkyCubeTexture
```

The initializer creates the sky generator instance that’s the same size as the top layer image of the skyscraper:

```swift
width = foregroundImage.width
height = foregroundImage.height

skyGenerator = MDLSkyCubeTexture(name: nil,
                                 channelEncoding: .uInt8,
                                 textureDimensions: .init(x: Int32(width),
                                                          y: Int32(height)),
                                 turbidity: 0,
                                 sunElevation: 0,
                                 upperAtmosphereScattering: 0,
                                 groundAlbedo: 0)
```

##### Update the sky texture generator parameters

With each change to the SwiftUI [`Picker`](../SwiftUI/picker.md) controls that define the sky generator parameters, the app calls the `renderSky()` function. The function sets the sky generator parameters and calls [`update()`](../ModelIO/mdlskycubetexture/update%28%29.md) to generate new texel data:

```swift
skyGenerator.turbidity = turbidity
skyGenerator.sunElevation = sunElevation
skyGenerator.upperAtmosphereScattering = upperAtmosphereScattering
skyGenerator.groundAlbedo = groundAlbedo

skyGenerator.update()
```

##### Create the composite image

The [`texelDataWithTopLeftOrigin()`](../ModelIO/mdltexture/texeldatawithtopleftorigin%28%29.md) method returns the sky generator’s image data organized such that its first pixel represents the top-left corner of the image. This layout matches the [`vImage.PixelBuffer`](./vimage/pixelbuffer.md) layout. The code passes the texel data to the [`withUnsafeBytes(_:)`](../Foundation/data/withunsafebytes%28_%29.md) function to work with the underlying bytes of the data’s contiguous storage.

```swift
let img = skyGenerator.texelDataWithTopLeftOrigin()?.withUnsafeBytes { skyData in
```

The [`MDLSkyCubeTexture`](../ModelIO/mdlskycubetexture.md) instance generates a cube texture that’s represented as six sides, vertically stacked.

![A vertically stacked series of six images that represent the six sides of the sky texture cube.](https://developer.apple.com/tutorials/images/com.apple.accelerate/cube.png)

The code below calculates the range texels that correspond to the selected side (one of `["+X", "-X", "+Y", "-Y", "+Z", "-Z"]`) and binds those to [`Pixel_8`](./pixel_8.md) values:

```swift
let imageIndex = ImageProvider.views.firstIndex(of: view) ?? 0
let imagePixelCount = width * height * format.componentCount

let range = imageIndex * imagePixelCount ..< (imageIndex + 1) * imagePixelCount

let values = skyData.bindMemory(to: Pixel_8.self)[ range ]
```

The code below creates a [`vImage.PixelBuffer`](./vimage/pixelbuffer.md) structure from the values and, because the [`alphaComposite(_:topLayer:destination:)`](./vimage/pixelbuffer/alphacomposite%28_,toplayer,destination%29-fybo.md) method expects ARGB data, permutes the channel order so that alpha channel is first:

```swift
let buffer = vImage.PixelBuffer(pixelValues: values,
                                size: .init(width: width, height: height),
                                pixelFormat: vImage.Interleaved8x4.self)

buffer.permuteChannels(to: (3, 0, 1, 2), destination: buffer)
```

Finally, the sample code project composites the skyscraper image, represented by `foregroundBuffer`, over the sky image and returns a [`CGImage`](../CoreGraphics/cgimage.md) instance that contains the result:

```swift
    buffer.alphaComposite(.nonpremultiplied,
                          topLayer: foregroundBuffer,
                          destination: buffer)
    
    return buffer.makeCGImage(cgImageFormat: format)
} // Ends `skyGenerator.texelDataWithTopLeftOrigin()?.withUnsafeBytes`.
```

## See Also

### vImage Pixel Buffers
- [Using vImage pixel buffers to generate video effects](./using-vimage-pixel-buffers-to-generate-video-effects.md)
  Render real-time video effects with the vImage Pixel Buffer.
- [Applying tone curve adjustments to images](./applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [Adjusting the brightness and contrast of an image](./adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [Adjusting the hue of an image](./adjusting-the-hue-of-an-image.md)
  Convert an image to L*a*b* color space and apply hue adjustment.
- [Calculating the dominant colors in an image](./calculating-the-dominant-colors-in-an-image.md)
  Find the main colors in an image by implementing k-means clustering using the Accelerate framework.
- [vImage.PixelBuffer](./vimage/pixelbuffer.md)
  An image buffer that stores an image’s pixel data, dimensions, bit depth, and number of channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sharing-texture-data-between-the-model-io-framework-and-the-vimage-library)*