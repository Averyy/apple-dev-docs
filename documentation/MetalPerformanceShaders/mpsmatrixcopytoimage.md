# MPSMatrixCopyToImage

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSMatrixCopyToImage : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixcopytoimage/init%28coder,device%29.md)
- [init(device: any MTLDevice, dataLayout: MPSDataLayout)](./mpsmatrixcopytoimage/init%28device,datalayout%29.md)
### Instance Properties
- [var dataLayout: MPSDataLayout](./mpsmatrixcopytoimage/datalayout.md)
- [var sourceMatrixBatchIndex: Int](./mpsmatrixcopytoimage/sourcematrixbatchindex.md)
- [var sourceMatrixOrigin: MTLOrigin](./mpsmatrixcopytoimage/sourcematrixorigin.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, destinationImage: MPSImage)](./mpsmatrixcopytoimage/encode%28commandbuffer,sourcematrix,destinationimage%29.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, destinationImages: [MPSImage])](./mpsmatrixcopytoimage/encodebatch%28commandbuffer,sourcematrix,destinationimages%29.md)

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

### Matrix Copying Operations
- [class MPSMatrixCopy](./mpsmatrixcopy.md)
  A class that can perform multiple matrix copy operations.
- [class MPSMatrixCopyDescriptor](./mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.
- [class MPSImageCopyToMatrix](./mpsimagecopytomatrix.md)
  A class that copies image data to a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopytoimage)*