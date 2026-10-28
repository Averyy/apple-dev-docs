# coordinate(alongAxisTensor:withShape:name:)

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
func coordinate(alongAxisTensor axisTensor: MPSGraphTensor, withShape shape: [NSNumber], name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) coordinateAlongAxisTensor:(MPSGraphTensor *) axisTensor withShape:(MPSShape *) shape name:(NSString *) name;
```

## Return Value

A valid MPSGraphTensor object.

## Discussion

See [`coordinate(alongAxis:withShape:name:)`](./coordinate%28alongaxis,withshape,name%29.md).

## Parameters

- `axisTensor`: A Scalar tensor of type `MPSDataTypeInt32`, that specifies the coordinate axis an element’s value is set to. Negative values wrap around.
- `shape`: The shape of the result tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/coordinate(alongaxistensor:withshape:name:))*