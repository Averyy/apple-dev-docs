# MPSNDArrayDescriptor

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
class MPSNDArrayDescriptor
```

```objc
@interface MPSNDArrayDescriptor : NSObject
```

## Topics

### Initializers
- [convenience init(dataType: MPSDataType, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>)](./mpsndarraydescriptor/init%28datatype,dimensioncount,dimensionsizes%29.md)
- [convenience init(dataType: MPSDataType, shape: [NSNumber])](./mpsndarraydescriptor/init%28datatype,shape%29.md)
### Instance Properties
- [var dataType: MPSDataType](./mpsndarraydescriptor/datatype.md)
- [var numberOfDimensions: Int](./mpsndarraydescriptor/numberofdimensions.md)
- [var preferPackedRows: Bool](./mpsndarraydescriptor/preferpackedrows.md)
### Instance Methods
- [func dimensionOrder() -> vector_uchar16](./mpsndarraydescriptor/dimensionorder%28%29.md)
- [func getShape() -> [NSNumber]](./mpsndarraydescriptor/getshape%28%29.md)
- [func length(ofDimension: Int) -> Int](./mpsndarraydescriptor/length%28ofdimension%29.md)
- [func permute(withDimensionOrder: UnsafeMutablePointer<Int>)](./mpsndarraydescriptor/permute%28withdimensionorder%29.md)
- [func reshape(withDimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>)](./mpsndarraydescriptor/reshape%28withdimensioncount,dimensionsizes%29.md)
- [func reshape(withShape: [NSNumber])](./mpsndarraydescriptor/reshape%28withshape%29.md)
- [func sliceDimension(Int, withSubrange: MPSDimensionSlice)](./mpsndarraydescriptor/slicedimension%28_,withsubrange%29.md)
- [func sliceRange(forDimension: Int) -> MPSDimensionSlice](./mpsndarraydescriptor/slicerange%28fordimension%29.md)
- [func transposeDimension(Int, withDimension: Int)](./mpsndarraydescriptor/transposedimension%28_,withdimension%29.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraydescriptor)*