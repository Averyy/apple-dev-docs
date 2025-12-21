# BNNSDataLayoutGetRank(_:)

**Framework**: Accelerate  
**Kind**: func

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func BNNSDataLayoutGetRank(_ layout: BNNSDataLayout) -> Int
```

#### Return Value

The number of dimensions represented by `layout`, or `SIZE_T_MAX` if unable to determine

#### Discussion

Determine the rank of the given layout

## See Also

- [struct BNNSLayerData](bnnslayerdata.md)
  A structure containing common layer parameters.
- [BNNS.Shape](bnns/shape.md)
  Constants that describe the size and data layout of an n-dimensional array descriptor.
- [struct BNNSDataLayout](bnnsdatalayout.md)
  Constants that describe the data type of an n-dimensional array.
- [struct BNNSDataType](bnnsdatatype.md)
  BNNS Data Types.
- [struct BNNSNDArrayDescriptor](bnnsndarraydescriptor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayoutgetrank(_:))*