---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/turnscripts/blockedunscriptedtokens"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# blockedUnscriptedTokens

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: property  
**Role**: Instance Property

Tokens the model must not emit inside a turn where the script has no token: the stop tokens and the first marker token. Either one would end the turn early or start the next one. Stop strings are not covered.

## Declaration

```swift
var blockedUnscriptedTokens: Set<Int> { get }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/turnscripts/blockedunscriptedtokens)*