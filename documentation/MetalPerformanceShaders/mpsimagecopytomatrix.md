# MPSImageCopyToMatrix

**Framework**: Metal Performance Shaders  
**Kind**: class

A class that copies image data to a matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageCopyToMatrix
```

#### Overview

This kernel copies image data to a [`MPSMatrix`](mpsmatrix.md) object. The image data is stored in a row of a matrix.  The [`dataLayout`](mpsimagecopytomatrix/datalayout.md) specifies the order in which the feature channels in the image get stored in the matrix.  If the [`MPSImage`](mpsimage.md) stores a batch of images, the images are copied into multiple rows, one row per image.

The number of elements in a row in the matrix must be greater than the image width multiplied its height multiplied by the number of [`featureChannels`](mpsimage/featurechannels.md) in the image.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagecopytomatrix/init(coder:device:).md)
- [init(device: any MTLDevice, dataLayout: MPSDataLayout)](mpsimagecopytomatrix/init(device:datalayout:).md)
### Instance Properties
- [var dataLayout: MPSDataLayout](mpsimagecopytomatrix/datalayout.md)
- [var destinationMatrixBatchIndex: Int](mpsimagecopytomatrix/destinationmatrixbatchindex.md)
- [var destinationMatrixOrigin: MTLOrigin](mpsimagecopytomatrix/destinationmatrixorigin.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationMatrix: MPSMatrix)](mpsimagecopytomatrix/encode(commandbuffer:sourceimage:destinationmatrix:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationMatrix: MPSMatrix)](mpsimagecopytomatrix/encodebatch(commandbuffer:sourceimages:destinationmatrix:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSMatrixCopy](mpsmatrixcopy.md)
  A class that can perform multiple matrix copy operations.
- [class MPSMatrixCopyToImage](mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSMatrixCopyDescriptor](mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagecopytomatrix)*