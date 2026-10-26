---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/transcript/terminator/none"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# Transcript.Terminator.none

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: case  
**Role**: Case

Nothing: generation runs until `maxTokens`, emitting unscripted tokens after the script. Those are never a stop token or the turn marker, so the turn cannot end early. Stop strings can still match the decoded text.

## Declaration

```swift
case none
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/transcript/terminator/none)*