# MPSNDArray

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNDArray
```

## Topics

### Initializers
- [convenience init(buffer: any MTLBuffer, offset: Int, descriptor: MPSNDArrayDescriptor)](mpsndarray/init(buffer:offset:descriptor:).md)
- [init(device: any MTLDevice, descriptor: MPSNDArrayDescriptor)](mpsndarray/init(device:descriptor:).md)
- [convenience init(device: any MTLDevice, scalar: Double)](mpsndarray/init(device:scalar:).md)
### Instance Properties
- [var dataType: MPSDataType](mpsndarray/datatype.md)
- [var dataTypeSize: Int](mpsndarray/datatypesize.md)
- [var device: any MTLDevice](mpsndarray/device.md)
- [var label: String?](mpsndarray/label.md)
- [var numberOfDimensions: Int](mpsndarray/numberofdimensions.md)
- [var parent: MPSNDArray?](mpsndarray/parent.md)
### Instance Methods
- [func arrayView(with: MPSNDArrayDescriptor) -> MPSNDArray?](mpsndarray/arrayview(with:).md)
- [func arrayView(with: any MTLCommandBuffer, descriptor: MPSNDArrayDescriptor, aliasing: MPSAliasingStrategy) -> MPSNDArray?](mpsndarray/arrayview(with:descriptor:aliasing:).md)
- [func arrayView(withDimensionCount: Int, dimensionSizes: UnsafePointer<Int>, strides: UnsafePointer<Int>) -> MPSNDArray?](mpsndarray/arrayview(withdimensioncount:dimensionsizes:strides:).md)
- [func arrayView(withShape: [NSNumber]?, strides: [NSNumber]) -> MPSNDArray?](mpsndarray/arrayview(withshape:strides:).md)
- [func descriptor() -> MPSNDArrayDescriptor](mpsndarray/descriptor.md)
- [func exportData(with: any MTLCommandBuffer, to: any MTLBuffer, destinationDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)](mpsndarray/exportdata(with:to:destinationdatatype:offset:rowstrides:).md)
- [func exportData(with: any MTLCommandBuffer, to: [MPSImage], offset: MPSImageCoordinate)](mpsndarray/exportdata(with:to:offset:).md)
- [func importData(with: any MTLCommandBuffer, from: [MPSImage], offset: MPSImageCoordinate)](mpsndarray/importdata(with:from:offset:).md)
- [func importData(with: any MTLCommandBuffer, from: any MTLBuffer, sourceDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)](mpsndarray/importdata(with:from:sourcedatatype:offset:rowstrides:).md)
- [func length(ofDimension: Int) -> Int](mpsndarray/length(ofdimension:).md)
- [func readBytes(UnsafeMutableRawPointer, strideBytes: UnsafeMutablePointer<Int>?)](mpsndarray/readbytes(_:stridebytes:).md)
- [func resourceSize() -> Int](mpsndarray/resourcesize.md)
- [func synchronize(on: any MTLCommandBuffer)](mpsndarray/synchronize(on:).md)
- [func userBuffer() -> (any MTLBuffer)?](mpsndarray/userbuffer.md)
- [func writeBytes(UnsafeMutableRawPointer, strideBytes: UnsafeMutablePointer<Int>?)](mpsndarray/writebytes(_:stridebytes:).md)
### Type Methods
- [class func defaultAllocator() -> any MPSNDArrayAllocator](mpsndarray/defaultallocator.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSTemporaryNDArray](mpstemporaryndarray.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray)*