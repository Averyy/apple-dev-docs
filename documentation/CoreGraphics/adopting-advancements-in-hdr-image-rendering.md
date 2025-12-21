# Enhancing high dynamic range image rendering

**Framework**: Core Graphics

Improve your app’s High Dynamic Range (HDR) image support with metadata.

#### Overview

HDR images support a wider range of brightness levels than traditional, standard dynamic range images, and provide significant visual improvements. Despite the visual benefits of HDR images, rendering them in full fidelity isn’t always the best option for your app. You may need to reduce HDR fidelity to lower your app’s power consumption, avoid causing eye strain, or improve mixed media or multiwindow experiences by matching the range of brightness between your images and the rest of the system UI.

You can precisely configure how the system presents HDR images with API support across photos and videos by setting a preferred dynamic range and adding hints for the system with metadata API. Additional information for rendering HDR images can be found in [`Supporting HDR images in your app`](https://developer.apple.com/documentation/UIKit/supporting-hdr-images-in-your-app).

> **Note**: For additional information on rendering HDR images, see WWDC24 session 10177: [`Use HDR for dynamic image experiences in your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10177), and WWDC23 session 10181: [`Support HDR images in your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10181) WWDC sessions.

##### Set the Dynamic Range You Prefer

You can indicate the HDR fidelity you desire with the multiple content-rendering frameworks that include the [`preferredDynamicRange`](CGContentToneMappingInfo-swift.enum/DefaultOptions/preferredDynamicRange.md) and its sibling properties. For graphics and images, [`Core Graphics`](CoreGraphics.md) and [`Core Animation`](https://developer.apple.com/documentation/QuartzCore) offer the functionality in [`CGImage`](CGImage.md) and [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer). You can also find `preferredDynamicRange` in AVKit and UIKit frameworks: the [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController), [`Color`](https://developer.apple.com/documentation/SwiftUI/Color), [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView), and [`NSImageView`](https://developer.apple.com/documentation/AppKit/NSImageView) classes, offer a consistent API.

Each API supports three rendering styles:

- Standard dynamic range
- Constrained HDR rendering, which applies to mixed media and multiwindow applications
- Full HDR, when an app renders content that maximizes the a display’s capabilities

> **Note**: Only Core Animation layers support animating across [`preferredDynamicRange`](https://developer.apple.com/documentation/QuartzCore/CALayer/preferredDynamicRange) values.

##### Manage Hdr Metadata

HDR images capture a wide range of light values. You can take advantage of metadata on an HDR image to improve rendering by declaring how the system presents those light value ranges in context.

, for instance, is the ratio between the maximum HDR light level and the maximum SDR light level, and can be an attribute of either an image or a display. Image headroom identifies when an HDR image has a higher dynamic range than a display’s HDR capabilities informing you the image might not render as you expect. [`Core Graphics`](CoreGraphics.md) supports automatic bitmap context management, choosing appropriate bit depth, color space, and context target headroom based on the content. The system can make reasonable choices on behalf of your app even if the system doesn’t explicitly support HDR metadata.

[`contentAverageLightLevel`](CGImage/contentAverageLightLevel.md) establishes the average light level across all image pixels. Use [`CGContentToneMappingInfo.DynamicRange.constrained`](CGContentToneMappingInfo-swift.enum/DynamicRange/constrained.md) dynamic range to optimize rendering for multimedia and multiwindow usage. And `.constrained` rendering relies on `contentAverageLightLevel` metadata to adapt each HDR image according to its overall brightness, avoiding the possibility of bright HDR media overpowering other media, UI elements, or text.

##### Calculate Hdr Metadata

The system interprets headroom and average content light level from standard HDR metadata often present in HDR images and videos. When the information is available in the file, the system loads the metadata into memory automatically, along with the image data. When there’s no metadata, you can compute the information it might contain at load time. [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) and [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) always compute HDR metadata. [`Image I/O`](https://developer.apple.com/documentation/ImageIO) and [`Core Image`](https://developer.apple.com/documentation/CoreImage) only compute HDR metadata when the [`kCGComputeHDRStats`](https://developer.apple.com/documentation/ImageIO/kCGComputeHDRStats) option is set.

Images loaded without metadata receive default values for [`contentHeadroom`](CGColor/contentHeadroom.md) (`4.926`) and  [`contentAverageLightLevel`](CGImage/contentAverageLightLevel.md) (`0.0`).

HDR metadata may be calculated at any time with the [`copyWithCalculatedHDRStats()`](cgimage/copywithcalculatedhdrstats().md) API. The system adds the calculated HDR statistics to the copied image, and doesn’t set the values on the original image.

```swift
CGImageRef image = originalCIImage.copyWithCalculatedHDRStats()
```

> **Note**: Computing HDR metadata at load time requires extra computation and may impact performance.

Once the system calculates [`contentHeadroom`](CGImage/contentHeadroom.md) and [`contentAverageLightLevel`](CGImage/contentAverageLightLevel.md) at load time or loads them along with the image data, you can access the values with `get` functions in [`Image I/O`](https://developer.apple.com/documentation/ImageIO) and [`Core Image`](https://developer.apple.com/documentation/CoreImage) to ensure you use the images in the appropriate contexts.

## See Also

- [var contentHeadroom: Float](cgimage/contentheadroom.md)
- [var calculatedContentHeadroom: Float](cgimage/calculatedcontentheadroom.md)
- [var contentAverageLightLevel: Float](cgimage/contentaveragelightlevel.md)
- [var calculatedContentAverageLightLevel: Float](cgimage/calculatedcontentaveragelightlevel.md)
- [func copy(contentAverageLightLevel: Float) -> CGImage?](cgimage/copy(contentaveragelightlevel:).md)
- [func copyWithCalculatedHDRStats() -> CGImage?](cgimage/copywithcalculatedhdrstats.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/adopting-advancements-in-hdr-image-rendering)*