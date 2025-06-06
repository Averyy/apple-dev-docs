# bandPart(_:numLowerTensor:numUpperTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates the band part operation and returns the result.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func bandPart(_ inputTensor: MPSGraphTensor, numLowerTensor: MPSGraphTensor, numUpperTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

See above discussion of bandPartWithTensor: numLower: numUpper: name:

## Parameters

- `inputTensor`: The source tensor to copy.
- `numLowerTensor`: Scalar Int32 tensor. The number of diagonals in the lower triangle to keep. If -1, keep all.
- `numUpperTensor`: Scalar Int32 tensor. The number of diagonals in the upper triangle to keep. If -1, keep all.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/bandpart(_:numlowertensor:numuppertensor:name:))*