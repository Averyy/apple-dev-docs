# reverseSquareRoot(with:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Applies the reverse square root operation to the input tensor elements.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func reverseSquareRoot(with tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) reverseSquareRootWithTensor:(MPSGraphTensor *) tensor name:(NSString *) name;
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

The reverse square root operation is the reciprocal of the square root.

## Parameters

- `tensor`: The input tensor.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reversesquareroot(with:name:))*