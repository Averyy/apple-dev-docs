# cumulativeMinimum(_:axis:exclusive:reverse:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Computes the cumulative minimum of the input tensor along the specified axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func cumulativeMinimum(_ tensor: MPSGraphTensor, axis: Int, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) cumulativeMinimumWithTensor:(MPSGraphTensor *) tensor axis:(NSInteger) axis exclusive:(BOOL) exclusive reverse:(BOOL) reverse name:(NSString *) name;
```

## Return Value

A valid MPSGraphTensor object

## Parameters

- `tensor`: The input tensor
- `axis`: The tensor dimension where you compute the cumulative operation
- `exclusive`: If true, perform the exclusive cumulative operation, and the first element will be equal to the largest value of the tensor data type
- `reverse`: If true, reverse the direction of the cumulative operation along the specified axis
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/cumulativeminimum(_:axis:exclusive:reverse:name:))*