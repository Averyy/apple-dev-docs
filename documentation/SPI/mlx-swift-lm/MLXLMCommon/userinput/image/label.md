---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/image/label"
framework: "mlx-swift-lm/MLXLMCommon"
---

# label

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Text that a vision message generator writes into the prompt as `[label]`, immediately before this image. The generator leaves out and logs a label that contains `<`, `>`, `|`, `[` or `]`. A vision processor also leaves out a label whose `[label]` form contains a special token, such as `IMG` on Mistral3.

## Declaration

```swift
var label: String?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/image/label)*