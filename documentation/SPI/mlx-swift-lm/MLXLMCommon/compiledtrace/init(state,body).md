---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/compiledtrace/init(state:body:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(state:body:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(state: @escaping StateProvider = { [$0] }, body: @escaping Body)
```

## Parameters

- `state`: The modules whose weights the body reads; the owner by default, which covers a body that stays inside its own subtree
- `body`: The function to trace


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/compiledtrace/init(state:body:))*