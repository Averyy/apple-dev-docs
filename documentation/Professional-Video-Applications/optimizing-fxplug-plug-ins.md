# Optimizing FxPlug plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Maintain consistent rendering at all resolutions and aspect ratios by using pixel transforms.

#### Overview

FxPlug plug-ins provide users a real-time rendering experience that’s measured in frames produced per second. Plug-ins that work with large inputs can optimize their performance by rendering only a subset of pixels as determined using *pixel transforms*.

Pixel transforms are 4x4 matrices that are created by the host app to contain *transformation* information about the media the plug-in has been applied to. Transformations include translation, rotation, scale, and foreshortening (skewing the image to make closer objects appear larger).

##### Understand pixel transforms

The host application creates the 4x4 matrices used in pixel transforms. These matrices contain information that must be taken into account in order to render correctly and efficiently.

For example, if the host application asks your plug-in to render a small thumbnail preview, the scaling information for that request is contained in the pixel transform matrices. Likewise, when a user selects Dynamic Resolution from the viewer options in Motion, or Better Performance in Final Cut Pro, that information is also included in the pixel transform matrices. A pixel transform contains either full or partial information on how the input or output image will be distorted before being composited into the scene. Take a look at this example:

![A checkerboard layer parallel to the film-back of the virtual camera](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3906065@2x.png)

When a layer is parallel to the film-back of the virtual camera that’s recording a scene, you might see all of its pixels as shown above.

The most efficient texture for a generator to produce is one that corresponds exactly to the pixels needed in the final composition. Assuming that your plug-in supports pixel transforms, a good one to use is the one that projects from the layer’s object space to the scene’s output space. When the user rotates the layer around the y-axis and translates it back on the z-axis, it becomes shorter along its width, as shown below. Rotating the layer in this way lets your plug-in process fewer pixels, because fewer pixels are needed to render the final composition.

![The checkerboard layer rotated around the y axis](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3906063@2x.png)

> **Note**:  A pixel transform doesn’t contain the same information as a full transformation matrix, which also shows a layer’s position in the scene. To get complete information about the 3D environment, including camera and object transforms, use the `Fx3DAPI_v4` object that the host application provides.****

##### Support pixel transforms in your plug-in

Each plug-in chooses what information it needs to know about the image through pixel transforms, and lets the host know which types of transforms it will deal with. It does this by including the associated key-value pair in the dictionary it returns from its properties method. The key is [`kFxPropertyKey_PixelTransformSupport`](../professional_video_applications/kfxpropertykey_pixeltransformsupport.md), and the value tells the host application what types of transformations a plug-in is capable of working with. (If your plug-in doesn’t include this key, the host application assumes that your plug-in supports scale transforms).

- **[`kFxPixelTransform_Scale`](../professional_video_applications/kfxpixeltransform_scale.md)**: This plug-in supports non-uniform scaling only.
- **[`kFxPixelTransform_ScaleTranslate`](../professional_video_applications/kfxpixeltransform_scaletranslate.md)**: This plug-in supports both non-uniform scaling and translation.
- **[`kFxPixelTransform_Full`](../professional_video_applications/kfxpixeltransform_full.md)**: This plug-in supports any affine or full-perspective transform.

Your properties method can also set a Boolean on another key, `kFxPropertyKey_PixelIndependent`. If a plug-in is pixel independent, each output pixel relies only on a single input pixel, and the location of each input pixel doesn’t matter. An example of this would be a color filter, which applies an adjustment at every pixel, regardless of position.

The following code shows a typical entry in the dictionary returned by the [`properties(_:)`](../professional_video_applications/fxtileableeffect/properties%28_%29.md) method:

**Swift**:

```swift
func properties(_ properties: AutoreleasingUnsafeMutablePointer<NSDictionary>?) throws {
        let swiftProps = [
            kFxPropertyKey_MayRemapTime : NSNumber(booleanLiteral: false),
            kFxPropertyKey_PixelTransformSupport : NSNumber(value: kFxPixelTransform_ScaleTranslate),
            kFxPropertyKey_VariesWhenParamsAreStatic: NSNumber(booleanLiteral: false)
        ]
        let props = NSDictionary(dictionary: swiftProps)
        properties?.pointee = props
    }
```

**Objective-C**:

```objc
- (BOOL)properties:(NSDictionary * _Nonnull * _Nullable)properties
             error:(NSError * _Nullable * _Nullable)error
{
    *properties = @{
                    kFxPropertyKey_MayRemapTime : @NO,
                    kFxPropertyKey_PixelTransformSupport :
                    [NSNumber numberWithInt:kFxPixelTransform_ScaleTranslate]
                    }; 
    return YES;
}
```

##### Apply pixel transforms

After informing the host application which types of transforms your plug-in supports, apply the appropriate pixel transforms using these steps:

1. Ask the input image for its pixel transform or its inverse pixel transform matrices (or both). Use the [`FxImageTile`](../professional_video_applications/fximagetile.md) class methods [`pixelTransform`](../professional_video_applications/fximagetile/pixeltransform.md) and [`inversePixelTransform`](../professional_video_applications/fximagetile/inversepixeltransform.md) to convert coordinate systems. If you want to convert coordinates into full-sized, square pixel coordinates, use `inversePixelTransform`. If you want to convert from full-sized, square pixel coordinates to actual image pixels, use `pixelTransform`.
2. Use the specified transformation matrices in your plug-in’s fragment shader.
3. Pass the current coordinate for the input texture through the inverse pixel transform. The result is a coordinate that represents the current pixel if the image were in square pixels, not transformed, at its full resolution, with the origin in the center of the image. This coordinate system is sometimes referred to as *document space*.
4. Calculate for distortions, convolution kernels, and so on using the coordinate derived in the previous step. To distort pixels along a sine wave or push pixels away from a particular point in the image, work in square pixels at full resolution to get correct results for all types of footage in all viewing conditions. Likewise, to sample multiple places in the input image to produce a blur or other convolution kernel, space the samples appropriately, regardless of the pixel aspect ratio, use of fields, or viewing resolution.
5. Convert the values back into the space that the image’s pixels are actually in. If your plug-in is a generator, you have no input image, so skip this step. Pass the coordinates through the forward pixel transform to get the coordinate from which you sampled the input image. This space is usually referred to as *pixel space*.

You can now safely sample from the image and know that you’ll get the required result.

##### Compare pixel transform examples

If you make proper use of pixel transforms in your rendering code, you don’t need special-case code for thumbnails or proxy resolution, and you don’t need to scale any of your parameters: your rendering will work for all of these situations. The illustrations below show common pixel transforms.

If a user creates a square-pixel project and applies project-sized footage to the canvas (a typical case) the pixel transform is the identity matrix, as is the inverse pixel transform, as shown in the following illustration.

![Matrix Example 1: 1:1 pixel transform and inverse pixel transform matrices](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3906064@2x.png)

If a user then sets the canvas viewing resolution to half-resolution, that change is reflected in the pixel transform, as shown in the following illustration:

![Matrix Example 2: Half-size pixel transform and inverse pixel transform matrices](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3906062@2x.png)

If the user applies a filter to footage that has a pixel aspect ratio of 1.33, that change is reflected in the pixel transform, as shown in the final illustration.

![Matrix Example 3: Pixel aspect of 1.33 transform and inverse pixel transform matrices](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3906061@2x.png)

## See Also

### Rendering
- [Rendering in FxPlug](./rendering-in-fxplug.md)
  Use Metal or other frameworks to render images with your FxPlug plug-in.
- [Communicating with the plug-in state](./communicating-with-the-plug-in-state.md)
  Prepare the necessary information, such as parameter values, for your FxPlug plug-in to render.
- [Working with tiled images](./working-with-tiled-images.md)
  Render only the necessary tiles of an image in your FxPlug plug-in to improve efficiency.
- [protocol FxTileableEffect](../professional_video_applications/fxtileableeffect.md)
  The designated initializer for your plug-in for rendering only certain portions of the plug-in’s output, referred to as tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/optimizing-fxplug-plug-ins)*