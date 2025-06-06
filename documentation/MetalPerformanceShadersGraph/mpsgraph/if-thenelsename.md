# if(_:then:else:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Adds an if-then-else operation to the graph.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func `if`(_ predicateTensor: MPSGraphTensor, then thenBlock: @escaping MPSGraphIfThenElseBlock, else elseBlock: MPSGraphIfThenElseBlock?, name: String?) -> [MPSGraphTensor]
```

#### Return Value

Results If no error, the tensors returned by user. If not empty, user must define both then/else block, both should have same number of arguments and each corresponding argument should have same elementTypes.

## Parameters

- `predicateTensor`: Tensor must have a single scalar value, used to decide between then/else branches
- `thenBlock`: If predicate is true operations in this block are executed
- `elseBlock`: If predicate is false operations in this block are executed
- `name`: Name of operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/if(_:then:else:name:))*