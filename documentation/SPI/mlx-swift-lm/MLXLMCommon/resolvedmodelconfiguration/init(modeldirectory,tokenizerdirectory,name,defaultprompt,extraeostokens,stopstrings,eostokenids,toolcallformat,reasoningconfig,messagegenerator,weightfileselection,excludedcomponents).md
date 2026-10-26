---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolvedmodelconfiguration/init(modeldirectory:tokenizerdirectory:name:defaultprompt:extraeostokens:stopstrings:eostokenids:toolcallformat:reasoningconfig:messagegenerator:weightfileselection:excludedcomponents:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(modelDirectory:tokenizerDirectory:name:defaultPrompt:extraEOSTokens:stopStrings:eosTokenIds:toolCallFormat:reasoningConfig:messageGenerator:weightFileSelection:excludedComponents:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(modelDirectory: URL, tokenizerDirectory: URL, name: String, defaultPrompt: String, extraEOSTokens: Set<String>, stopStrings: Set<String>? = nil, eosTokenIds: Set<Int>, toolCallFormat: ToolCallFormat?, reasoningConfig: ReasoningConfig? = nil, messageGenerator: (any MessageGenerator)? = nil, weightFileSelection: WeightFileSelection = .automatic, excludedComponents: Set<ModelComponent> = [])
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolvedmodelconfiguration/init(modeldirectory:tokenizerdirectory:name:defaultprompt:extraeostokens:stopstrings:eostokenids:toolcallformat:reasoningconfig:messagegenerator:weightfileselection:excludedcomponents:))*