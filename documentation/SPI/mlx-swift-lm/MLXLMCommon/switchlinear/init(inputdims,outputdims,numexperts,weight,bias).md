---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/switchlinear/init(inputdims:outputdims:numexperts:weight:bias:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(inputDims:outputDims:numExperts:weight:bias:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initializer meant for subclasses to provide weight and bias arrays directly.

## Declaration

```swift
init(inputDims: Int, outputDims: Int, numExperts: Int, weight: MLXArray, bias: MLXArray? = nil)
```

## Discussion

This is used e.g. by [`QuantizedSwitchLinear`](../quantizedswitchlinear.md) to provide quantized weights and biases rather than have [`SwitchLinear`](../switchlinear.md) compute them.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/switchlinear/init(inputdims:outputdims:numexperts:weight:bias:))*