# identity(with:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Copies the input tensor values into the output, behaving as an identity operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func identity(with tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) identityWithTensor:(MPSGraphTensor *) tensor name:(NSString *) name;
```

## Return Value

A valid `MPSGraphTensor` object which is a copy of the input.

## Parameters

- `tensor`: The input tensor.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/identity(with:name:))*