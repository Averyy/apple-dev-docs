# maxPooling4D(_:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Creates a 4D max-pooling operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func maxPooling4D(_ source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) maxPooling4DWithSourceTensor:(MPSGraphTensor *) source descriptor:(MPSGraphPooling4DOpDescriptor *) descriptor name:(NSString *) name;
```

## Return Value

A valid MPSGraphTensor object

## Parameters

- `source`: A source tensor.
- `descriptor`: A pooling operation descriptor that specifies pooling window sizes, strides, dilation rates and paddings.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/maxpooling4d(_:descriptor:name:))*