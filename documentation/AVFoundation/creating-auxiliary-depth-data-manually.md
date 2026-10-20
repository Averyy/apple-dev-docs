# Creating auxiliary depth data manually

**Framework**: AVFoundation  
**Role**: Article

Generate a depth image and attach it to your own image.

#### Overview

iOS Portrait Mode generates a depth map and attaches it to the image as auxiliary metadata, but for custom effects, you can generate your own auxiliary depth image, one not taken with iOS Portrait Mode or another depth-enabled capture device. This article shows you how to generate this map and attach it to your image.

##### Convert pixel values into a compatible floating-point format

The depth image is a single-component image that must be converted per-pixel from grayscale pixel values (`0` = black to `1` = white, zNear to zFar) to either depth (in meters) or disparity (in 1/meters). Then adjust these values to fit your desired floating-point format.

The supported pixel formats for disparity or depth images are:

- `kCVPixelFormatType_DisparityFloat16 = 'hdis'`: An IEEE754-2008 binary16 (half float), describing the normalized shift when comparing two images. Units are 1/meters: (pixelShift / (pixelFocalLength * baselineInMeters))
- `kCVPixelFormatType_DisparityFloat32 = 'fdis'`: An IEEE754-2008 binary32 float, describing the normalized shift when comparing two images. Units are 1/meters: (pixelShift / (pixelFocalLength * baselineInMeters))
- `kCVPixelFormatType_DepthFloat16 = 'hdep'`: An IEEE754-2008 binary16 (half float), describing the depth (distance to an object) in meters
- `kCVPixelFormatType_DepthFloat32 = 'fdep'`: An IEEE754-2008 binary32 float, describing the depth (distance to an object) in meters

Load the grayscale image into a [CVPixelBuffer](../CoreVideo/cvpixelbuffer-q2e.md). Load its base address, attained via [`CVPixelBufferLockBaseAddress(_:_:)`](../CoreVideo/cvpixelbufferlockbaseaddress%28_,_%29.md), as data ([`CFData`](../CoreFoundation/cfdata.md)) and pass it as the [`kCGImageAuxiliaryDataInfoData`](../ImageIO/kcgimageauxiliarydatainfodata.md) value into a dictionary ([`CFDictionary`](../CoreFoundation/cfdictionary.md)).

##### Parse metadata dictionaries

The format of the dictionary is documented in `CGImageSource.h`. Access this dictionary with [`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](../ImageIO/cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md). The dictionary supports JPEG, HEIF, and DNG images. The [`CFDictionary`](../CoreFoundation/cfdictionary.md) contains auxiliary data in the following format:

- [`kCGImageAuxiliaryDataInfoData`](../ImageIO/kcgimageauxiliarydatainfodata.md) → Depth data ([`CFData`](../CoreFoundation/cfdata.md))
- [`kCGImageAuxiliaryDataInfoDataDescription`](../ImageIO/kcgimageauxiliarydatainfodatadescription.md) → Depth data description ([`CFDictionary`](../CoreFoundation/cfdictionary.md): See below for more details.)
- [`kCGImageAuxiliaryDataInfoMetadata`](../ImageIO/kcgimageauxiliarydatainfometadata.md) → Optional metadata ([`CGImageMetadata`](../ImageIO/cgimagemetadata.md))

[`CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)`](../ImageIO/cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md) returns `nil` if the image doesn’t contain `auxiliaryImageDataType` data.

The value for key [`kCGImageAuxiliaryDataInfoDataDescription`](../ImageIO/kcgimageauxiliarydatainfodatadescription.md) is a [`CFDictionary`](../CoreFoundation/cfdictionary.md) that you populate to tell the image system how to interpret the depth map. It can contain the following depth data parameters:

- [`kCGImagePropertyPixelFormat`](../ImageIO/kcgimagepropertypixelformat.md) → One of the Core Video `CVPixelBuffer.h` depth or disparity formats
- [`kCGImagePropertyWidth`](../ImageIO/kcgimagepropertywidth.md) and [`kCGImagePropertyHeight`](../ImageIO/kcgimagepropertyheight.md) → Pixel dimensions
- [`kCGImagePropertyBytesPerRow`](../ImageIO/kcgimagepropertybytesperrow.md) → The number of bytes per row in the depth map

##### Attach your custom depth map to an image

Attach the depth or disparity dictionary to an image as follows:

1. Create [`AVDepthData`](./avdepthdata.md) with [`init(fromDictionaryRepresentation:)`](./avdepthdata/init%28fromdictionaryrepresentation%29.md), passing in the depth or disparity dictionary.
2. Create the image destination.
3. Create the image, using helper methods from [Image I/O](../ImageIO/ImageIO.md).

```swift
// Add an image to the destination.
CGImageDestinationAddImage(cgImageDestination, renderedCGImage, attachments)  

// Use AVDepthData to get the auxiliary data dictionary.         
var auxDataType :NSString? 
let auxData = depthData.dictionaryRepresentation(forAuxiliaryDataType: &auxDataType)  

// Add auxiliary data to the image destination. 
CGImageDestinationAddAuxiliaryDataInfo(cgImageDestination, auxDataType!, auxData! as CFDictionary)  

if CGImageDestinationFinalize(cgImageDestination) {  
	return data as Data
}  
```

## See Also

### Depth data capture
- [Capturing photos with depth](./capturing-photos-with-depth.md)
  Get a depth map with a photo to create effects like the system camera’s Portrait mode (on compatible devices).
- [Capturing depth using the LiDAR camera](./capturing-depth-using-the-lidar-camera.md)
  Access the LiDAR camera on supporting devices to capture precise depth data.
- [AVCamFilter: Applying filters to a capture stream](./avcamfilter-applying-filters-to-a-capture-stream.md)
  Render a capture stream with rose-colored filtering and depth effects.
- [Streaming depth data from the TrueDepth camera](./streaming-depth-data-from-the-truedepth-camera.md)
  Visualize depth data in 2D and 3D from the TrueDepth camera.
- [Enhancing live video by leveraging TrueDepth camera data](./enhancing-live-video-by-leveraging-truedepth-camera-data.md)
  Apply your own background to a live capture feed streamed from the front-facing TrueDepth camera.
- [class AVCaptureDepthDataOutput](./avcapturedepthdataoutput.md)
  A capture output that records scene depth information on compatible camera devices.
- [class AVDepthData](./avdepthdata.md)
  A container for per-pixel distance or disparity information captured by compatible camera devices.
- [class AVCameraCalibrationData](./avcameracalibrationdata.md)
  Information about the camera characteristics used to capture images and depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/creating-auxiliary-depth-data-manually)*