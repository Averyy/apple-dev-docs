# Enhancing high dynamic range image rendering

**Framework**: Core Graphics

Improve your app’s High Dynamic Range (HDR) image support with metadata.

#### Overview

HDR images support a wider range of brightness levels than traditional, standard dynamic range images, and provide significant visual improvements. Despite the visual benefits of HDR images, rendering them in full fidelity isn’t always the best option for your app. You may need to reduce HDR fidelity to lower your app’s power consumption, avoid causing eye strain, or improve mixed media or multiwindow experiences by matching the range of brightness between your images and the rest of the system UI.

You can precisely configure how the system presents HDR images with API support across photos and videos by setting a preferred dynamic range and adding hints for the system with metadata API. Additional information for rendering HDR images can be found in [`Supporting HDR images in your app`](https://developer.apple.com/documentation/uikit/supporting-hdr-images-in-your-app).

> **Note**: For additional information on rendering HDR images, see WWDC24 session 10177: [`Use HDR for dynamic image experiences in your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10177), and WWDC23 session 10181: [`Support HDR images in your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10181) WWDC sessions.

##### Set the Dynamic Range You Prefer

You can indicate the HDR fidelity you desire with the multiple content-rendering frameworks that include the [`preferredDynamicRange`](cgcontenttonemappinginfo-swift.enum/defaultoptions/preferreddynamicrange.md) and its sibling properties. For graphics and images, [`Core Graphics`](CoreGraphics.md) and [`Core Animation`](https://developer.apple.com/documentation/quartzcore) offer the functionality in [`CGImage`](cgimage.md) and [`CALayer`](https://developer.apple.com/documentation/quartzcore/calayer). You can also find `preferredDynamicRange` in AVKit and UIKit frameworks: the [`AVPlayerViewController`](https://developer.apple.com/documentation/avkit/avplayerviewcontroller), [`Color`](https://developer.apple.com/documentation/swiftui/color), [`UIImageView`](https://developer.apple.com/documentation/uikit/uiimageview), and [`NSImageView`](https://developer.apple.com/documentation/appkit/nsimageview) classes, offer a consistent API.

Each API supports three rendering styles:

- Standard dynamic range
- Constrained HDR rendering, which applies to mixed media and multiwindow applications
- Full HDR, when an app renders content that maximizes the a display’s capabilities

**Core Graphics**:

```swift
let url = URL(fileURLWithFileSystemRepresentation: "HDR.heic", isDirectory: true, relativeTo: nil)
let hdrOptions = [kCGImageSourceDecodeRequest: kCGImageSourceDecodeToHDR]
let bitmapInfo = CGBitmapInfo(alpha: .premultipliedLast,
                              byteOrder: .order16Little,
                              pixelFormat: .packed)
if let imageSource = CGImageSourceCreateWithURL(url as CFURL, nil),
   let hdrHEIC = CGImageSourceCreateImageAtIndex(imageSource, 0, hdrOptions as CFDictionary),
    let context = CGContext(data: nil,
                            width: hdrHEIC.width,
                            height: hdrHEIC.height,
                            bitsPerComponent: 16,
                            bytesPerRow: 0,
                            space: CGColorSpace(name: CGColorSpace.extendedLinearDisplayP3),
                            bitmapInfo: bitmapInfo) {
    let targetHeadroom: Float = 2.0

    context.setEDRTargetHeadroom(targetHeadroom)

    let averageLightLevel = hdrHEIC.calculatedContentAverageLightLevel
    let options = CGContentToneMappingInfo.DefaultOptions(contentAverageLightLevel: .nits(Int(averageLightLevel)), preferredDynamicRange: .constrained)
    let toneMappingInfo = CGContentToneMappingInfo.referenceWhiteBased(options)
    
    context.contentToneMappingInfo = toneMappingInfo

    context.draw(hdrHEIC, in: CGRect(x: 0, y: 0, width: hdrHEIC.width, height: hdrHEIC.height))

    let result = context.makeImage()
}
```

**Core Image**:

```swift
let image = CIImage.empty()
let currentDisplayHeadroom:Float = 4.92
let filter = CIFilter.systemToneMap()

filter.inputImage = image
filter.displayHeadroom = currentDisplayHeadroom
filter.preferredDynamicRange = .constrainedHigh

let toneMappedImage = filter.outputImage
```

**Core Animation**:

```swift
let layer = CALayer()

// The default is automatic.
layer.preferredDynamicRange = .automatic

// Set standard dynamic range rendering.
layer.preferredDynamicRange = .standard

// The constrained-high option helps HDR content co-exist with SDR content and media.
layer.preferredDynamicRange = .constrainedHigh

// When the full HDR experience is appropriate, such as fullscreen images or editing, set a high dynamic range.
layer.preferredDynamicRange = .high
```

> **Note**: Only Core Animation layers support animating across [`preferredDynamicRange`](https://developer.apple.com/documentation/quartzcore/calayer/preferreddynamicrange) values.

##### Manage Hdr Metadata

HDR images capture a wide range of light values. You can take advantage of metadata on an HDR image to improve rendering by declaring how the system presents those light value ranges in context.

*Headroom*, for instance, is the ratio between the maximum HDR light level and the maximum SDR light level, and can be an attribute of either an image or a display. Image headroom identifies when an HDR image has a higher dynamic range than a display’s HDR capabilities informing you the image might not render as you expect. [`Core Graphics`](CoreGraphics.md) supports automatic bitmap context management, choosing appropriate bit depth, color space, and context target headroom based on the content. The system can make reasonable choices on behalf of your app even if the system doesn’t explicitly support HDR metadata.

[`contentAverageLightLevel`](cgimage/contentaveragelightlevel.md) establishes the average light level across all image pixels. Use [`CGContentToneMappingInfo.DynamicRange.constrained`](cgcontenttonemappinginfo-swift.enum/dynamicrange/constrained.md) dynamic range to optimize rendering for multimedia and multiwindow usage. And `.constrained` rendering relies on `contentAverageLightLevel` metadata to adapt each HDR image according to its overall brightness, avoiding the possibility of bright HDR media overpowering other media, UI elements, or text.

##### Calculate Hdr Metadata

The system interprets headroom and average content light level from standard HDR metadata often present in HDR images and videos. When the information is available in the file, the system loads the metadata into memory automatically, along with the image data. When there’s no metadata, you can compute the information it might contain at load time. [`NSImage`](https://developer.apple.com/documentation/appkit/nsimage) and [`UIImage`](https://developer.apple.com/documentation/uikit/uiimage) always compute HDR metadata. [`Image I/O`](https://developer.apple.com/documentation/imageio) and [`Core Image`](https://developer.apple.com/documentation/coreimage) only compute HDR metadata when the [`kCGComputeHDRStats`](https://developer.apple.com/documentation/imageio/kcgcomputehdrstats) option is set.

**ImageIO**:

```swift
let sourceData = Data()
let options: [CFString: Any] = [
    kCGImageSourceDecodeRequest: kCGImageSourceDecodeToHDR,
    kCGImageSourceDecodeRequestOptions: [kCGComputeHDRStats: true]];

if let src = CGImageSourceCreateWithData(sourceData as CFData, nil) {
    let img = CGImageSourceCreateImageAtIndex(src, 0, options as CFDictionary)
}
```

**Core Image**:

```swift
if let ciImage = CIImage(contentsOf: url) {
    let hdrStatCIImage = ciContext.calculateHDRStats(for: ciImage)
}
```

Images loaded without metadata receive default values for [`contentHeadroom`](cgcolor/contentheadroom.md) (`4.926`) and  [`contentAverageLightLevel`](cgimage/contentaveragelightlevel.md) (`0.0`).

HDR metadata may be calculated at any time with the [`copyWithCalculatedHDRStats()`](cgimage/copywithcalculatedhdrstats().md) API. The system adds the calculated HDR statistics to the copied image, and doesn’t set the values on the original image.

```swift
CGImageRef image = originalCIImage.copyWithCalculatedHDRStats()
```

> **Note**: Computing HDR metadata at load time requires extra computation and may impact performance.

Once the system calculates [`contentHeadroom`](cgimage/contentheadroom.md) and [`contentAverageLightLevel`](cgimage/contentaveragelightlevel.md) at load time or loads them along with the image data, you can access the values with `get` functions in [`Image I/O`](https://developer.apple.com/documentation/imageio) and [`Core Image`](https://developer.apple.com/documentation/coreimage) to ensure you use the images in the appropriate contexts.

**ImageIO**:

```swift
let contentAverageLightLevel = cgImage.contentAverageLightLevel
let headroom = cgImage.contentHeadroom
let computedContentAverageLightLevel = cgImage.calculatedContentAverageLightLevel
```

**Core Image**:

```swift
let contentAverageLightLevel = ciImage.contentAverageLightLevel
let headroom = ciImage.contentHeadroom
```

## See Also

- [var contentHeadroom: Float](cgimage/contentheadroom.md)
- [var calculatedContentHeadroom: Float](cgimage/calculatedcontentheadroom.md)
- [var contentAverageLightLevel: Float](cgimage/contentaveragelightlevel.md)
- [var calculatedContentAverageLightLevel: Float](cgimage/calculatedcontentaveragelightlevel.md)
- [func copy(contentAverageLightLevel: Float) -> CGImage?](cgimage/copy(contentaveragelightlevel:).md)
- [func copyWithCalculatedHDRStats() -> CGImage?](cgimage/copywithcalculatedhdrstats.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/adopting-advancements-in-hdr-image-rendering)*