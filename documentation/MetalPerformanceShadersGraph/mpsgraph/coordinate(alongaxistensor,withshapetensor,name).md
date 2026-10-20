# coordinate(alongAxisTensor:withShapeTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Creates a get-coordindate operation and returns the result tensor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func coordinate(alongAxisTensor axisTensor: MPSGraphTensor, withShapeTensor shapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) coordinateAlongAxisTensor:(MPSGraphTensor *) axisTensor withShapeTensor:(MPSGraphTensor *) shapeTensor name:(NSString *) name;
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

See [`coordinate(alongAxis:withShape:name:)`](./coordinate%28alongaxis,withshape,name%29.md).

## Parameters

- `axisTensor`: A Scalar tensor of type `MPSDataTypeInt32`, that specifies the coordinate axis an element’s value is set to. Negative values wrap around.
- `shapeTensor`: A rank-1 tensor of type `MPSDataTypeInt32` or `MPSDataTypeInt64` that defines the shape of the result tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/coordinate(alongaxistensor:withshapetensor:name:))*