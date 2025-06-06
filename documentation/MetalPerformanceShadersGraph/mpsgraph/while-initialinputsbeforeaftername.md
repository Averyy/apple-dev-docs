# while(initialInputs:before:after:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Adds a while loop operation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func `while`(initialInputs: [MPSGraphTensor], before: @escaping MPSGraphWhileBeforeBlock, after: @escaping MPSGraphWhileAfterBlock, name: String?) -> [MPSGraphTensor]
```

#### Return Value

A valid MPSGraphTensor array with results returned from the conditionBlock depending on the predicate tensor.

## Parameters

- `initialInputs`: inputTensors to the  , for the 1st iteration will be same as initialInputs passed to the while loop.
- `before`:  , this will be run first and then call the   with results or return results from the loop.
- `after`:  , this will execute after the condition evaluation.
- `name`: Name of operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/while(initialinputs:before:after:name:))*