---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processchunkoutputs(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# processChunkOutputs(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Processes a generated chunk and removes its output in source order.

## Declaration

```swift
func processChunkOutputs(_ chunk: String) -> [Output]
```

#### Discussion

Tool protocol syntax that does not parse as a call is not emitted as a response. Use this streaming operation when tool calls and response text must retain their relative order. Do not mix this API with `processChunk`, `processEOS`, or `drainToolCalls()` on the same processor instance.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processchunkoutputs(_:))*