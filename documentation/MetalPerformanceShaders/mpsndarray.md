# MPSNDArray

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSNDArray : NSObject
```

## Topics

### Initializers
- [convenience init(buffer: any MTLBuffer, offset: Int, descriptor: MPSNDArrayDescriptor)](./mpsndarray/init%28buffer,offset,descriptor%29.md)
- [init(device: any MTLDevice, descriptor: MPSNDArrayDescriptor)](./mpsndarray/init%28device,descriptor%29.md)
- [convenience init(device: any MTLDevice, scalar: Double)](./mpsndarray/init%28device,scalar%29.md)
### Instance Properties
- [var dataType: MPSDataType](./mpsndarray/datatype.md)
- [var dataTypeSize: Int](./mpsndarray/datatypesize.md)
- [var device: any MTLDevice](./mpsndarray/device.md)
- [var label: String?](./mpsndarray/label.md)
- [var numberOfDimensions: Int](./mpsndarray/numberofdimensions.md)
- [var parent: MPSNDArray?](./mpsndarray/parent.md)
### Instance Methods
- [func arrayView(with: MPSNDArrayDescriptor) -> MPSNDArray?](./mpsndarray/arrayview%28with%29.md)
- [func arrayView(with: any MTLCommandBuffer, descriptor: MPSNDArrayDescriptor, aliasing: MPSAliasingStrategy) -> MPSNDArray?](./mpsndarray/arrayview%28with,descriptor,aliasing%29.md)
- [func arrayView(withDimensionCount: Int, dimensionSizes: UnsafePointer<Int>, strides: UnsafePointer<Int>) -> MPSNDArray?](./mpsndarray/arrayview%28withdimensioncount,dimensionsizes,strides%29.md)
- [func arrayView(withShape: [NSNumber]?, strides: [NSNumber]) -> MPSNDArray?](./mpsndarray/arrayview%28withshape,strides%29.md)
- [func descriptor() -> MPSNDArrayDescriptor](./mpsndarray/descriptor%28%29.md)
- [func exportData(with: any MTLCommandBuffer, to: any MTLBuffer, destinationDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)](./mpsndarray/exportdata%28with,to,destinationdatatype,offset,rowstrides%29.md)
- [func exportData(with: any MTLCommandBuffer, to: [MPSImage], offset: MPSImageCoordinate)](./mpsndarray/exportdata%28with,to,offset%29.md)
- [func importData(with: any MTLCommandBuffer, from: [MPSImage], offset: MPSImageCoordinate)](./mpsndarray/importdata%28with,from,offset%29.md)
- [func importData(with: any MTLCommandBuffer, from: any MTLBuffer, sourceDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)](./mpsndarray/importdata%28with,from,sourcedatatype,offset,rowstrides%29.md)
- [func length(ofDimension: Int) -> Int](./mpsndarray/length%28ofdimension%29.md)
- [func readBytes(UnsafeMutableRawPointer, strideBytes: UnsafeMutablePointer<Int>?)](./mpsndarray/readbytes%28_,stridebytes%29.md)
- [func resourceSize() -> Int](./mpsndarray/resourcesize%28%29.md)
- [func synchronize(on: any MTLCommandBuffer)](./mpsndarray/synchronize%28on%29.md)
- [func userBuffer() -> (any MTLBuffer)?](./mpsndarray/userbuffer%28%29.md)
- [func writeBytes(UnsafeMutableRawPointer, strideBytes: UnsafeMutablePointer<Int>?)](./mpsndarray/writebytes%28_,stridebytes%29.md)
### Type Methods
- [class func defaultAllocator() -> any MPSNDArrayAllocator](./mpsndarray/defaultallocator%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPSTemporaryNDArray](./mpstemporaryndarray.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray)*