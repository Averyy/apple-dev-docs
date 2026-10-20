# clamp(_:min:max:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Clamps the values in the first tensor between the corresponding values in the minimum and maximum value tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func clamp(_ tensor: MPSGraphTensor, min minValueTensor: MPSGraphTensor, max maxValueTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) clampWithTensor:(MPSGraphTensor *) tensor minValueTensor:(MPSGraphTensor *) minValueTensor maxValueTensor:(MPSGraphTensor *) maxValueTensor name:(NSString *) name;
```

#### Return Value

A valid `MPSGraphTensor` object containing the elementwise result of the applied operation.

#### Discussion

This operation creates a clamp operation and returns the result tensor. It supports broadcasting as well.

```md
resultTensor = clamp(tensor, minValueTensor, maxValueTensor)
```

## Parameters

- `tensor`: The tensor to be clamped.
- `minValueTensor`: The tensor with min values to clamp to.
- `name`: An optional string which serves as an identifier for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/clamp(_:min:max:name:))*