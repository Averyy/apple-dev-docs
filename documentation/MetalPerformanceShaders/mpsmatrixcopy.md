# MPSMatrixCopy

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixcopy/init(coder:device:).md)
- [init(device: any MTLDevice, copyRows: Int, copyColumns: Int, sourcesAreTransposed: Bool, destinationsAreTransposed: Bool)](mpsmatrixcopy/init(device:copyrows:copycolumns:sourcesaretransposed:destinationsaretransposed:).md)
### Instance Properties
- [var copyColumns: Int](mpsmatrixcopy/copycolumns.md)
- [var copyRows: Int](mpsmatrixcopy/copyrows.md)
- [var destinationsAreTransposed: Bool](mpsmatrixcopy/destinationsaretransposed.md)
- [var sourcesAreTransposed: Bool](mpsmatrixcopy/sourcesaretransposed.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, copyDescriptor: MPSMatrixCopyDescriptor)](mpsmatrixcopy/encode(commandbuffer:copydescriptor:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, copyDescriptor: MPSMatrixCopyDescriptor, rowPermuteIndices: MPSVector?, rowPermuteOffset: Int, columnPermuteIndices: MPSVector?, columnPermuteOffset: Int)](mpsmatrixcopy/encode(commandbuffer:copydescriptor:rowpermuteindices:rowpermuteoffset:columnpermuteindices:columnpermuteoffset:).md)

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

- [class MPSMatrixCopyToImage](mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSMatrixCopyDescriptor](mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.
- [class MPSImageCopyToMatrix](mpsimagecopytomatrix.md)
  A class that copies image data to a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopy)*