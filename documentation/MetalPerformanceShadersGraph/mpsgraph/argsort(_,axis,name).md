# argSort(_:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Computes the indices that sort the elements of the input tensor along the specified axis.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+

## Declaration

```swift
func argSort(_ tensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) argSortWithTensor:(MPSGraphTensor *) tensor axis:(NSInteger) axis name:(NSString *) name;
```

#### Return Value

A valid MPSGraphTensor object with 32-bit integer data type

## Parameters

- `tensor`: The input tensor
- `axis`: The tensor dimension over which you sort the tensor
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/argsort(_:axis:name:))*