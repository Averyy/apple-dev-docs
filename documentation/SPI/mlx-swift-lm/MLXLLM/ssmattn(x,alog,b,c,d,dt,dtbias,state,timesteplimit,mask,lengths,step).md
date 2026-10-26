---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/ssmattn(x:alog:b:c:d:dt:dtbias:state:timesteplimit:mask:lengths:step:)"
framework: "mlx-swift-lm/MLXLLM"
---

# ssmAttn(x:ALog:B:C:D:dt:dtBias:state:timeStepLimit:mask:lengths:step:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func ssmAttn(x: MLXArray, ALog: MLXArray, B: MLXArray, C: MLXArray, D: MLXArray, dt: MLXArray, dtBias: MLXArray, state: MLXArray? = nil, timeStepLimit: (Float, Float) = (0.001, 100.0), mask: MLXArray? = nil, lengths: MLXArray? = nil, step: Int = 256) -> (MLXArray, MLXArray)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/ssmattn(x:alog:b:c:d:dt:dtbias:state:timesteplimit:mask:lengths:step:))*