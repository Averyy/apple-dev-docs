# MPSMatrixCopy

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A class that can perform multiple matrix copy operations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixCopy
```

```objc
@interface MPSMatrixCopy : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsmatrixcopy/init%28coder,device%29.md)
- [init(device: any MTLDevice, copyRows: Int, copyColumns: Int, sourcesAreTransposed: Bool, destinationsAreTransposed: Bool)](./mpsmatrixcopy/init%28device,copyrows,copycolumns,sourcesaretransposed,destinationsaretransposed%29.md)
### Instance Properties
- [var copyColumns: Int](./mpsmatrixcopy/copycolumns.md)
- [var copyRows: Int](./mpsmatrixcopy/copyrows.md)
- [var destinationsAreTransposed: Bool](./mpsmatrixcopy/destinationsaretransposed.md)
- [var sourcesAreTransposed: Bool](./mpsmatrixcopy/sourcesaretransposed.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, copyDescriptor: MPSMatrixCopyDescriptor)](./mpsmatrixcopy/encode%28commandbuffer,copydescriptor%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, copyDescriptor: MPSMatrixCopyDescriptor, rowPermuteIndices: MPSVector?, rowPermuteOffset: Int, columnPermuteIndices: MPSVector?, columnPermuteOffset: Int)](./mpsmatrixcopy/encode%28commandbuffer,copydescriptor,rowpermuteindices,rowpermuteoffset,columnpermuteindices,columnpermuteoffset%29.md)

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
- [class MPSMatrixCopyToImage](./mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSMatrixCopyDescriptor](./mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.
- [class MPSImageCopyToMatrix](./mpsimagecopytomatrix.md)
  A class that copies image data to a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopy)*