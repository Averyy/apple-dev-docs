---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/images"
framework: "mlx-swift-lm/MLXLMCommon"
---

# images

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

The images associated with the `UserInput`.

## Declaration

```swift
var images: [UserInput.Image]
```

## Discussion

If the [`prompt`](./prompt-swift.property.md) is a [`UserInput.Prompt.chat(_:)`](./prompt-swift.enum/chat%28_%29.md) this will collect the images from the chat messages, otherwise these are the stored images with the [`UserInput`](../userinput.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/images)*