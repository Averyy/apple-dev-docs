# AVPortraitEffectsMatte

**Framework**: AVFoundation  
**Kind**: class

An auxiliary image used to separate foreground from background with high resolution.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class AVPortraitEffectsMatte
```

## Mentions

- [Extracting Portrait Effects matte image data from a photo](extracting-portrait-effects-matte-image-data-from-a-photo.md)

#### Overview

Before iOS 11, the iPhone camera software used depth maps to render a shallow depth of field (the  effect) into still images taken in Portrait Mode before discarding the maps. Because the effect was part of the photo, you couldn’t access the maps separately, as metadata, for photos taken by devices running iOS 10 or earlier.

Starting in iOS 11, apps accessing the photo library can use images containing embedded auxiliary depth maps to render creative depth effects, such as forced perspective, or image projection from 2D to 3D space. These depth maps are low-resolution compared to the full-resolution RGB image. As such, the depth effects you can render are limited by the resolution and accuracy of the maps. Fine detail, such as hair, is challenging to preserve faithfully at the resolution of these depth maps.

Starting in iOS 12, the portrait effects matte helps achieve this fine-grain level of detail.

![Zoomed in photo showing the fine detail in a portrait effects matte image](https://docs-assets.developer.apple.com/published/c69e91511a8754659f6683c83569e86d/media-3030223%402x.png)

|  |  |  |  |
| --- | --- | --- | --- |
| Rear dual camera | 4032 x 3024 | 768 x 576 | 2016 x 1512 |
| TrueDepth camera | 3088 x 2320 | 640 x 480 | 1544 x 1160 |

Using the auxiliary matte image, you can improve the quality of rendered portrait effects, such as Natural Light, Studio Light, Contour Light, Stage Light, and Stage Light Mono.

Unlike the depth map, the portrait effects matte isn’t intended to faithfully preserve all gradations of depth in the scene. It’s a depth-guided, people-focused segmentation mask generated from a proprietary Apple neural network trained to detect people. It separates an individual in the foreground from whatever is in the background, with greater detail and clarity than with the depth map alone. It achieves this clarity in part because the matte image has higher resolution than the depth map.

For information about capturing the portrait effects matte, see [`Configuring camera capture to collect a Portrait Effects matte`](configuring-camera-capture-to-collect-a-portrait-effects-matte.md). To learn how to extract a portrait effects matte from photos previously captured in portrait mode on a device running iOS 12, see [`Extracting Portrait Effects matte image data from a photo`](extracting-portrait-effects-matte-image-data-from-a-photo.md).

## Topics

### Creating a Portrait Effects matte
- [Configuring camera capture to collect a Portrait Effects matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
  Prepare your app to capture a portrait effects matte when taking photos.
- [convenience init(fromDictionaryRepresentation: [AnyHashable : Any]) throws](avportraiteffectsmatte/init(fromdictionaryrepresentation:).md)
  Initializes a portrait effects matte instance from auxiliary image information in an image file.
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](avportraiteffectsmatte/applyingexiforientation(_:).md)
  Returns a derivative portrait effects matte after applying the specified EXIF orientation.
- [func replacingPortraitEffectsMatte(with: CVPixelBuffer) throws -> Self](avportraiteffectsmatte/replacingportraiteffectsmatte(with:).md)
  Returns a portrait effects matte by wrapping the replacement pixel buffer.
### Examining a Portrait Effects matte
- [Extracting Portrait Effects matte image data from a photo](extracting-portrait-effects-matte-image-data-from-a-photo.md)
  Check for portrait effects matte metadata in existing images.
- [var mattingImage: CVPixelBuffer](avportraiteffectsmatte/mattingimage.md)
  The portrait effects matte’s internal image, formatted as a pixel buffer.
- [var pixelFormatType: OSType](avportraiteffectsmatte/pixelformattype.md)
  The pixel format type of this portrait effects matte’s internal image.
- [func dictionaryRepresentation(forAuxiliaryDataType: AutoreleasingUnsafeMutablePointer<NSString?>?) -> [AnyHashable : Any]?](avportraiteffectsmatte/dictionaryrepresentation(forauxiliarydatatype:).md)
  A dictionary of primitive map information used for writing an image file with a portrait effects matte.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVSemanticSegmentationMatte](avsemanticsegmentationmatte.md)
  An object that wraps a matting image for a particular semantic segmentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte)*