# MPSImageFindKeypoints

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A kernel that is used to find a list of keypoints.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageFindKeypoints
```

```objc
@interface MPSImageFindKeypoints : MPSKernel
```

#### Overview

This kernel is used to find a list of keypoints whose values are greater than the [`minimumThresholdValue`](./mpsimagekeypointrangeinfo/minimumthresholdvalue.md) in [`MPSImageKeypointRangeInfo`](./mpsimagekeypointrangeinfo.md). The keypoints are generated for a specified region in the image. The pixel format of the source image must be [`MTLPixelFormat.r8Unorm`](../Metal/mtlpixelformat/r8unorm.md).

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsimagefindkeypoints/init%28coder,device%29.md)
- [init(device: any MTLDevice, info: UnsafePointer<MPSImageKeypointRangeInfo>)](./mpsimagefindkeypoints/init%28device,info%29.md)
### Instance Properties
- [var keypointRangeInfo: MPSImageKeypointRangeInfo](./mpsimagefindkeypoints/keypointrangeinfo.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, regions: UnsafePointer<MTLRegion>, numberOfRegions: Int, keypointCount: any MTLBuffer, keypointCountBufferOffset: Int, keypointDataBuffer: any MTLBuffer, keypointDataBufferOffset: Int)](./mpsimagefindkeypoints/encode%28to,sourcetexture,regions,numberofregions,keypointcount,keypointcountbufferoffset,keypointdatabuffer,keypointdatabufferoffset%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Keypoints
- [struct MPSImageKeypointData](./mpsimagekeypointdata.md)
  A structure that specifies keypoint information.
- [struct MPSImageKeypointRangeInfo](./mpsimagekeypointrangeinfo.md)
  A structure that specifies information to find the keypoints in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefindkeypoints)*