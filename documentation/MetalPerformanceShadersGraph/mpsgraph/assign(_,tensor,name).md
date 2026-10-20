# assign(_:tensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Creates an assign operation which writes at this point of execution of the graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func assign(_ variable: MPSGraphTensor, tensor: MPSGraphTensor, name: String?) -> MPSGraphOperation
```

```objc
- (MPSGraphOperation *) assignVariable:(MPSGraphTensor *) variable withValueOfTensor:(MPSGraphTensor *) tensor name:(NSString *) name;
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `variable`: The variable resource tensor to assign to.
- `tensor`: The tensor to assign to the variable.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/assign(_:tensor:name:))*