# Applying Apple HDR effect to your photos

**Framework**: AppKit

You can decode and apply Apple’s HDR gain map to your own images.

#### Overview

You can apply Apple high dynamic range (HDR) effect to digital photography images without using Apple SDKs. You compute the Apple HDR gain map from the image’s auxiliary data and then apply it to the image. The  is an 8-bit, single-channel luminance map that’s stored with an image.

##### Extract the Existing Hdr Gain Map From the Image

Get the existing HDR gain map from the image’s auxiliary data using the `urn:com:apple:photo:2020:aux:hdrgainmap` image data type. The gain map is untagged and formatted as linear data. It’s encoded using the Rec.709 transfer function and is 1/4 the resolution of the original image.

For example, using Apple APIs, you can extract the gain map from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) object by passing [`kCGImageAuxiliaryDataTypeHDRGainMap`](https://developer.apple.com/documentation/ImageIO/kCGImageAuxiliaryDataTypeHDRGainMap) to the [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](https://developer.apple.com/documentation/ImageIO/CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)) function.

##### Calculate the Headroom From the Image Metadata

Write code that computes the headroom you need to change the dynamic range image. The headroom is the ratio of the luminance of the image’s brightest white to the luminance of standard dynamic range (SDR) white, in the image’s native color space.

Before you begin, check whether the image’s metadata contains the `HDRGainMapVersion` key. If this key exists in the metadata, the gain map is valid and you can continue calculating the headroom.

Next, extract the `MakerNote` dictionary from the image’s metadata. If the `MakerNote` dictionary contains the `33` and `48` keys and they’re set to 32-bit float values, the HDR gain map is valid and you can use it to calculate the headroom.

To compute the headroom, use the following Swift code snippet or rewrite this code in your preferred language:

```swift
// Extract the metadata keys from the image.
let (maker33, maker48) = getMetadataFromImage()
let stops: Float

// Convert the metadata to the number of stops
// (factors of 2) that the gain map should apply
// to the image.
if maker33 < 1.0 {
    if maker48 <= 0.01 {
        stops = -20.0 * maker48 + 1.8
    } else {
        stops = -0.101 * maker48 + 1.601
    }
} else {
    if maker48 <= 0.01 {
        stops = -70.0*maker48 + 3.0
    } else {
        stops = -0.303*maker48 + 2.303
    }
}

// Convert the stops to linear headroom.
let headroom = pow(2.0, max(stops, 0.0))
```

##### Apply the Hdr Gain Map to the Image

Before you apply the HDR gain map to the image, perform the following steps:

1. Resize the gain map by scaling it so it matches the size of the original image.
2. Linearize the gain map by inverting the gain map gamma using the Rec.709 transfer function.
3. Linearize the SDR RGB image by inverting the gamma of the image according to the colorspace.

Then use the headroom value you calculated previously to scale the gain map to the correct level and multiply it into each channel of the image as follows:

```swift
let sdr_rgb = ... // A pixel of the SDR image.
let gainmap = ... // A pixel of the gain map.

let hdr_rgb = sdr_rgb * (1.0 + (headroom - 1.0) * gainmap)
```

The result of applying the gain map is a linear HDR image with a scale where `1.0` is the reference white and the peak value is no greater than the headroom value.

> **Note**:  The technique described in this document has been proposed for standardization at the International Organization for Standardization (ISO) as part of ISO/NP 21496-1. Apple is prepared to commit to license essential patents in this technique with respect to a standard resulting from ISO/NP 21496-1 in accordance with the Common Patent Policy for ITU-T/ITU-R/ISO/IEC (as of April 2023).

## See Also

- [Providing images for different appearances](../UIKit/providing-images-for-different-appearances.md)
  Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Supporting Continuity Camera in Your Mac App](supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [Supporting HDR images in your app](../UIKit/supporting-hdr-images-in-your-app.md)
  ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [class NSImage](nsimage.md)
  A high-level interface for manipulating image data.
- [protocol NSImageDelegate](nsimagedelegate.md)
  A set of optional methods that you can use to respond to drawing failures and manage incremental loads.
- [class NSImageRep](nsimagerep.md)
  A semiabstract superclass that provides subclasses that you use to draw an image from a particular type of source data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/applying-apple-hdr-effect-to-your-photos)*