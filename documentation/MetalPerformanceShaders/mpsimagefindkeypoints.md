# MPSImageFindKeypoints

**Framework**: Metal Performance Shaders  
**Kind**: class

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

#### Overview

This kernel is used to find a list of keypoints whose values are greater than the [`minimumThresholdValue`](mpsimagekeypointrangeinfo/minimumthresholdvalue.md) in [`MPSImageKeypointRangeInfo`](mpsimagekeypointrangeinfo.md). The keypoints are generated for a specified region in the image. The pixel format of the source image must be [`MTLPixelFormat.r8Unorm`](https://developer.apple.com/documentation/metal/mtlpixelformat/r8unorm).

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagefindkeypoints/init(coder:device:).md)
- [init(device: any MTLDevice, info: UnsafePointer<MPSImageKeypointRangeInfo>)](mpsimagefindkeypoints/init(device:info:).md)
### Instance Properties
- [var keypointRangeInfo: MPSImageKeypointRangeInfo](mpsimagefindkeypoints/keypointrangeinfo.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, regions: UnsafePointer<MTLRegion>, numberOfRegions: Int, keypointCount: any MTLBuffer, keypointCountBufferOffset: Int, keypointDataBuffer: any MTLBuffer, keypointDataBufferOffset: Int)](mpsimagefindkeypoints/encode(to:sourcetexture:regions:numberofregions:keypointcount:keypointcountbufferoffset:keypointdatabuffer:keypointdatabufferoffset:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [struct MPSImageKeypointData](mpsimagekeypointdata.md)
  A structure that specifies keypoint information.
- [struct MPSImageKeypointRangeInfo](mpsimagekeypointrangeinfo.md)
  A structure that specifies information to find the keypoints in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefindkeypoints)*