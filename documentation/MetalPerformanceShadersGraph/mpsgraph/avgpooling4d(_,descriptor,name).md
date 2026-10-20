# avgPooling4D(_:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Creates a 4D average pooling operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func avgPooling4D(_ source: MPSGraphTensor, descriptor: MPSGraphPooling4DOpDescriptor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) avgPooling4DWithSourceTensor:(MPSGraphTensor *) source descriptor:(MPSGraphPooling4DOpDescriptor *) descriptor name:(NSString *) name;
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `source`: A source tensor.
- `descriptor`: A pooling operation descriptor that specifies pooling window sizes, strides, dilation rates and paddings.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/avgpooling4d(_:descriptor:name:))*