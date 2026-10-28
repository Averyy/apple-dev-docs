# variableFromTensor(_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Creates a variable from an input tensor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func variableFromTensor(_ tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) variableFromTensorWithTensor:(MPSGraphTensor *) tensor name:(NSString *) name;
```

## Return Value

A valid MPSGraphTensor object.

## Parameters

- `tensor`: The tensor from which to form the variable.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/variablefromtensor(_:name:))*