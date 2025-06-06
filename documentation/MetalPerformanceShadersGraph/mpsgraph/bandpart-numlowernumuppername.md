# bandPart(_:numLower:numUpper:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the band part of an input tensor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func bandPart(_ inputTensor: MPSGraphTensor, numLower: Int, numUpper: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

This operation copies a diagonal band of values from input tensor to a result tensor of the same size. A coordinate `[..., i, j]` is in the band if

```md
(numLower < 0 || (i-j) <= numLower) && (numUpper < 0 || (j-i) <= numUpper) 
```

The values outside of the band are set to 0.

## Parameters

- `inputTensor`: Input tensor
- `numLower`: The number of diagonals in the lower triangle to keep. If -1, the framework returns all sub diagnols.
- `numUpper`: The number of diagonals in the upper triangle to keep. If -1,  the framework returns all super diagnols.
- `name`: Name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/bandpart(_:numlower:numupper:name:))*