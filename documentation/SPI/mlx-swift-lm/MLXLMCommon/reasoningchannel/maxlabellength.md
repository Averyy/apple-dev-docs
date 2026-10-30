---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningchannel/maxlabellength"
framework: "mlx-swift-lm/MLXLMCommon"
---

# maxLabelLength

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

How far past the start delimiter a label may run before the opener counts as malformed and its text is shown as reasoning instead of consumed as metadata.

## Declaration

```swift
var maxLabelLength: Int
```

## Discussion

Without a bound, a label that never terminates either buffers the whole generation or swallows everything up to a distant end delimiter.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningchannel/maxlabellength)*