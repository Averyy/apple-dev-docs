# Managing color space and gamut in plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Control the appearance of your rendering by using the color gamut API.

## Overview

Motion and Final Cut Pro use a color-managed pipeline for rendering. They keep track of the color spaces the source clips define, and convert images and colors from one color space to another as necessary in order to preserve their intended appearance.

When the host app calls your FxPlug plug-in to render, the host app passes input images and colors that the host app already converted to the *working color space*. The plug-in’s desired color space, which the plug-in controls, and the gamut that Motion and Final Cut Pro use, which the user controls, uniquely determine the working color space. You usually don’t need to convert from one color space to another. (The only exceptions are plug-ins that do specialized processing in specific color spaces.)

### Understand color values and color spaces

Both a color’s component values and its defining color space determine its appearance. For example, the RGB values (`0.5, 0.5, 0.5`) appear as middle gray in the sRGB color space, but in the Rec. 709 color space, the same values appear as a slightly brighter gray. To display the same middle gray in Rec. 709, the plug-in must change the color values so that the sRGB color (`0.5, 0.5, 0.5`) appears to the eye as the same shade of gray as Rec. 709 (`0.45, 0.45, 0.45`).

![Rec. 709 and sRGB Transfer Functions](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3655264@2x.png)

The fact that both the component values and the color space control the color appearance can have some surprising implications. For example, in general, two colors with identical components appear differently to the eye if those two colors use different color spaces. Similarly, two colors that appear the same have different color components if those two colors use different color spaces.

When you create a color channel using the [`FxParameterCreationAPI_v5`](../professional_video_applications/fxparametercreationapi_v5.md), the host app assumes that default RGB values you supply are to be in the sRGB color space. The host app also uses the sRGB color space when the inspector displays color component values. However, when [`FxParameterRetrievalAPI_v7`](../professional_video_applications/fxparameterretrievalapi_v7.md) gets the color components, it converts sRGB values to the working color space. For example, if the color channel shows the components (`0.2, 0.4, 0.6`) and the working color space is linear Rec. 709, your plug-in receives (`0.033, 0.133, 0.3189`) as the value of the color. These converted color components are correct; both color values display as the same identical dark blue color.

> **Note**:  The [`kFxParameterFlag_DONT_REMAP_COLORS`](../professional_video_applications/kfxparameterflag_dont_remap_colors.md) parameter flag on a color channel is an exception to this rule because it states that the channel isn’t logically a color and the host must not treat it as belonging to a color space. Instead, the host treats such a color channel as a simple triple of floating-point values, and the host app delivers these values to your plug-in without any conversion.

### Set the desired color space

Your plug-in can tell Motion and Final Cut Pro whether you prefer the working color space to be a gamma-corrected color space or a linear color space. Whether your plug-in requires gamma-corrected or linear pixels is the plug-in’s *desired color space*.

Your plug-in specifies the desired color space by setting the value of the [`kFxPropertyKey_DesiredProcessingColorInfo`](../professional_video_applications/kfxpropertykey_desiredprocessingcolorinfo.md) key in its properties dictionary to either [`kFxImageColorInfo_RGB_GAMMA_VIDEO`](../professional_video_applications/kfximagecolorinfo_rgb_gamma_video.md) or [`kFxImageColorInfo_RGB_LINEAR`](../professional_video_applications/kfximagecolorinfo_rgb_linear.md). If your plug-in doesn’t set the value of this key, the default is `kFxImageColorInfo_RGB_LINEAR`.

### Determine the color gamut in use for the working color space

All color spaces have a range of colors that the color space defines, called the color space’s *gamut*. This gamut usually corresponds to color components that are in the range `[0, 1]` (some color spaces support *extended range*, where components can be less than `0` or greater than `1`). When a color has components that are outside of the range for a color space, the color is *out of gamut*.

> **Note**:  Motion and Final Cut Pro allow out of gamut colors in their rendering pipelines. So your plug-in may receive images or colors with components that are less than `0` or greater than `1`. For example, if the working color space is the Rec. 709 color space, and your input image is from a wide gamut clip and contains pixels outside the Rec. 709 gamut, your plug-in receives colors that have components that are either less than `0` or greater than `1`. Additionally, the host apps explicitly allows users to create colors with components outside the `[0, 1]` range in the inspector.

Display devices also have a gamut. In the past, television, computer, and phone displays commonly had a gamut similar to the Rec. 709 color gamut. Now, however, many devices can display a wider range of colors, which allows the colors to have a brighter or more saturated appearance.

To get the `FxColorPrimaries` value for the project that uses your plug-in, use the [`colorPrimaries()`](../professional_video_applications/fxcolorgamutapi_v2/colorprimaries%28%29.md) method of the `FxColorGamutAPI` protocol:

**Swift**:

```swift
let colorApi = _apiManager!.api(for: FxColorGamutAPI.self) as! FxColorGamutAPI
let isHDR : Bool = colorApi.colorPrimaries() == UInt(kFxColorPrimaries_Rec2020)

if isHDR {
   // ...
}
```

**Objective-C**:

```objc
id<FxColorGamutAPI> colorApi = [_apiManager apiForProtocol: @protocol(FxColorGamutAPI)];
BOOL isHDR = ([colorApi colorPrimaries] == kFxColorPrimaries_Rec2020);
if (isHDR)
{
   // ...
}
```

The `FxColorPrimaries` enumerated type defines the two choices of color gamut:

- **[`kFxColorPrimaries_Rec709`](../professional_video_applications/kfxcolorprimaries_rec709.md)**: Standard Rec. 709 gamut.
- **[`kFxColorPrimaries_Rec2020`](../professional_video_applications/kfxcolorprimaries_rec2020.md)**: Rec. 2020 Wide Gamut HDR.

These values correspond to the color processing settings in Motion or Final Cut Pro. For more information, see [Use wide-gamut HDR color processing in Motion](https://support.apple.com/en-ca/guide/motion/motnb8712fa5/mac) and [Use wide-gamut HDR color processing in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/use-wide-gamut-hdr-color-processing-ver1cd9629a5).

![Rec. 709/sRGB color space vs. Rec 2020](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3655257@2x.png)

### Determine the working color space

Between the plug-in’s desired color space and the gamut the [`FxColorGamutAPI_v2`](../professional_video_applications/fxcolorgamutapi_v2.md) protocol returns to your plug-in, you can determine what the actual working color space is when the host app calls your plug-in. This table describes the working color space for each combination of desired color space and color gamut value. The rows of this table are desired color space values, while the columns are gamut values.

|  | [`kFxColorPrimaries_Rec709`](../professional_video_applications/kfxcolorprimaries_rec709.md) | [`kFxColorPrimaries_Rec2020`](../professional_video_applications/kfxcolorprimaries_rec2020.md) |
| --- | --- | --- |
| [`kFxImageColorInfo_RGB_LINEAR`](../professional_video_applications/kfximagecolorinfo_rgb_linear.md) | The linear Rec. 709 color space | The linear Rec. 2020 color space |
| [`kFxImageColorInfo_RGB_GAMMA_VIDEO`](../professional_video_applications/kfximagecolorinfo_rgb_gamma_video.md) | The Rec. 709 color space | The Rec. 2020 color space |

When the host app calls your plug-in to render, Motion and Final Cut Pro provide input images in the working color space. If you retrieve the values of color parameters, the host app provides the values in the working color space (unless your color parameter uses [`kFxParameterFlag_DONT_REMAP_COLORS`](../professional_video_applications/kfxparameterflag_dont_remap_colors.md), in which case, the host app retrieves the components without conversion). Similarly, Motion and Final Cut Pro assume that the output image your plug-in renders is in the working color space.

As mentioned earlier, your plug-in must be able to accept colors outside the `[0, 1]` range. Values above `1.0` generally behave in an intuitive way: the higher the value, the brighter the color. Thus, (`1.5, 0, 0`) is a brighter red than (`1, 0, 0`). However, negative values don’t correspond to dimmer colors, as one might expect; instead, they correspond to higher saturation. For example, (`1, 1, 0`) is a fully (in-gamut) saturated yellow. But (`1, 1, -0.2`) is an even more saturated yellow that is out of gamut for the color space.

Negative color components can produce unexpected results in certain calculations. For example, the host app computes luminance as a weighted sum of the RGB components. If one or more of the components is negative, it artificially skews the luminance lower and can lead to unexpected rendering results. Nontrivial blending operations can also produce surprising results with component values outside of `[0, 1]`.

You must determine the best way for your plug-in to deal with such values. Simple options include clamping or taking the absolute value of the components; more sophisticated methods try to map out-of-gamut colors to in-gamut colors. The best solution depends on what your plug-in does and what results your users expect. There is no universally correct answer.

### Convert pixels between RGB and YCbCr

[`FxColorGamutAPI_v2`](../professional_video_applications/fxcolorgamutapi_v2.md) has two methods for obtaining matrices to convert pixels between RGB and YCbCr color spaces. Plug-ins commonly convert pixels between RGB and YCbCr color spaces using a single matrix multiply of the pixel and the desired conversion matrix. These two methods retrieve the appropriate matrices:

**Swift**:

```swift
func colorMatrixFromDesiredRGBToYCbCr() -> FxMatrix44!
func colorMatrixFromYCbCrToDesiredRGB() -> FxMatrix44!
```

**Objective-C**:

```objc
- (FxMatrix44*)colorMatrixFromDesiredRGBToYCbCr;
- (FxMatrix44*)colorMatrixFromYCbCrToDesiredRGB;
```

You can use the matrix that [`colorMatrixFromDesiredRGBToYCbCr()`](../professional_video_applications/fxcolorgamutapi_v2/colormatrixfromdesiredrgbtoycbcr%28%29.md) returns to convert from RGB pixels the host provides to your plug-in in the working space to the equivalent YCbCr pixels. Conversely, you can use the matrix that [`colorMatrixFromYCbCrToDesiredRGB()`](../professional_video_applications/fxcolorgamutapi_v2/colormatrixfromycbcrtodesiredrgb%28%29.md) returns to convert YCbCr pixels back to the RGB working color space.

If you need to convert from RGB to luminance only, you can use the matrix the [`colorMatrixFromDesiredRGBToYCbCr()`](../professional_video_applications/fxcolorgamutapi_v2/colormatrixfromdesiredrgbtoycbcr%28%29.md) method returns. Computing the dot product of the first row of the matrix with the RGB color obtains the luminance.

## See Also

### Color
- [protocol FxColorGamutAPI_v2](../professional_video_applications/fxcolorgamutapi_v2.md)
  A protocol that handles plug-in queries to the host for the project’s color gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/managing-color-space-and-gamut-in-plug-ins)*