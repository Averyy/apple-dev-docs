---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/audios"
framework: "mlx-swift-lm/MLXLMCommon"
---

# audios

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

The audios associated with the `UserInput`.

## Declaration

```swift
var audios: [UserInput.Audio]
```

## Discussion

If the [`prompt`](./prompt-swift.property.md) is a [`UserInput.Prompt.chat(_:)`](./prompt-swift.enum/chat%28_%29.md) this will collect the audios from the chat messages, otherwise these are the stored audios with the [`UserInput`](../userinput.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/audios)*