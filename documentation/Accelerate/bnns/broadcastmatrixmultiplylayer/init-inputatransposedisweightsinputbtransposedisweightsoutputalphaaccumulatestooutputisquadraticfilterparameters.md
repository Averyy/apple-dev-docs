# init(inputA:transposed:isWeights:inputB:transposed:isWeights:output:alpha:accumulatesToOutput:isQuadratic:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new broadcast matrix multiply layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
convenience init?(inputA: BNNSNDArrayDescriptor, transposed transposeA: Bool, isWeights aIsWeights: Bool, inputB: BNNSNDArrayDescriptor, transposed transposeB: Bool, isWeights bIsWeights: Bool, output: BNNSNDArrayDescriptor, alpha: Float, accumulatesToOutput: Bool, isQuadratic: Bool, filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `inputA`: The descriptor of matrix *A*.
- `transposeA`: A Boolean value that transposes the last two dimensions of matrix *A*.
- `aIsWeights`: A Boolean value that determines whether to treat matrix *A* as weights.
- `inputB`: The descriptor of matrix *B*.
- `transposeB`: A Boolean value that transposes the last two dimensions of matrix *B*.
- `bIsWeights`: A Boolean value that determines whether to treat matrix *B* as weights.
- `output`: The descriptor of the output.
- `alpha`: A value to scale the result.
- `accumulatesToOutput`: A Boolean value that specifies whether to add the result to the existing output.
- `isQuadratic`: A Boolean value that determines whether the operation multiplies matrix *A* by itself.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/broadcastmatrixmultiplylayer/init(inputa:transposed:isweights:inputb:transposed:isweights:output:alpha:accumulatestooutput:isquadratic:filterparameters:))*