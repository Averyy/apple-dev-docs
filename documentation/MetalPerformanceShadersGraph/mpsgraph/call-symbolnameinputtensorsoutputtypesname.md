# call(symbolName:inputTensors:outputTypes:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates an operation which invokes another executable.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func call(symbolName: String, inputTensors: [MPSGraphTensor], outputTypes: [MPSGraphType], name: String?) -> [MPSGraphTensor]
```

#### Return Value

An array of valid [`MPSGraphTensor`](mpsgraphtensor.md) objects representing the return tensors of the invoked executable.

## Parameters

- `symbolName`: The unique identifier used to find the executable in the   directory.
- `inputTensors`: The tensors which are passed as inputs to the executable being invoked.
- `outputTypes`: The expected return types of the executable being invoked.
- `name`: Name of operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/call(symbolname:inputtensors:outputtypes:name:))*