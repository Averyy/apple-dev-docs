---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatecompletioninfo/passthroughreason"
framework: "mlx-swift-lm/MLXLMCommon"
---

# passthroughReason

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Non-nil when the MTP iterator transitioned into sticky-passthrough mode for the remainder of the stream; carries the reason string captured at the moment of engagement. Nil if the iterator stayed speculative for the full stream or for non-MTP streams.

## Declaration

```swift
let passthroughReason: String?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatecompletioninfo/passthroughreason)*