---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processeosoutputs()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# processEOSOutputs()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Finishes processing and removes residual output in source order.

## Declaration

```swift
func processEOSOutputs() -> [Output]
```

## Discussion

This preserves non-tool text following EOS-delimited calls. Do not mix this API with the legacy processing and draining APIs.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processeosoutputs())*