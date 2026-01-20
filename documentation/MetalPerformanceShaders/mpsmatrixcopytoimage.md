# MPSMatrixCopyToImage

**Framework**: Metal Performance Shaders  
**Kind**: class

A kernel that copies matrix data to a Metal Performance Shaders image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixCopyToImage
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixcopytoimage/init(coder:device:).md)
- [init(device: any MTLDevice, dataLayout: MPSDataLayout)](mpsmatrixcopytoimage/init(device:datalayout:).md)
### Instance Properties
- [var dataLayout: MPSDataLayout](mpsmatrixcopytoimage/datalayout.md)
- [var sourceMatrixBatchIndex: Int](mpsmatrixcopytoimage/sourcematrixbatchindex.md)
- [var sourceMatrixOrigin: MTLOrigin](mpsmatrixcopytoimage/sourcematrixorigin.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, destinationImage: MPSImage)](mpsmatrixcopytoimage/encode(commandbuffer:sourcematrix:destinationimage:).md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, destinationImages: [MPSImage])](mpsmatrixcopytoimage/encodebatch(commandbuffer:sourcematrix:destinationimages:).md)

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
- [class MPSMatrixCopyDescriptor](mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.
- [class MPSImageCopyToMatrix](mpsimagecopytomatrix.md)
  A class that copies image data to a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopytoimage)*