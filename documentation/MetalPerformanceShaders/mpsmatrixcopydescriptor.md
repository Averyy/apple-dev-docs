# MPSMatrixCopyDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A description of multiple matrix copy operations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixCopyDescriptor
```

```objc
@interface MPSMatrixCopyDescriptor : NSObject
```

## Topics

### Initializers
- [init(device: any MTLDevice, count: Int)](./mpsmatrixcopydescriptor/init%28device,count%29.md)
- [init(sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], offsetVector: MPSVector?, offset: Int)](./mpsmatrixcopydescriptor/init%28sourcematrices,destinationmatrices,offsetvector,offset%29.md)
- [convenience init(sourceMatrix: MPSMatrix, destinationMatrix: MPSMatrix, offsets: MPSMatrixCopyOffsets)](./mpsmatrixcopydescriptor/init%28sourcematrix,destinationmatrix,offsets%29.md)
### Instance Methods
- [func setCopyOperationAt(Int, sourceMatrix: MPSMatrix, destinationMatrix: MPSMatrix, offsets: MPSMatrixCopyOffsets)](./mpsmatrixcopydescriptor/setcopyoperationat%28_,sourcematrix,destinationmatrix,offsets%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Matrix Copying Operations
- [class MPSMatrixCopy](./mpsmatrixcopy.md)
  A class that can perform multiple matrix copy operations.
- [class MPSMatrixCopyToImage](./mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSImageCopyToMatrix](./mpsimagecopytomatrix.md)
  A class that copies image data to a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopydescriptor)*