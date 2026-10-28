---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat/gptoss"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallFormat.gptOSS

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

GPT-OSS full Harmony response protocol.

## Declaration

```swift
case gptOSS
```

## Discussion

Not a tool-call JSON dialect: selects the Harmony frame parser + router (channels, recipients, terminators). Tool calls appear only as `commentary to=functions.<name>` frames within that protocol. Example: `<|channel|>commentary to=functions.get_weather<|message|>{"location": "Tokyo"}<|call|>`


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat/gptoss)*