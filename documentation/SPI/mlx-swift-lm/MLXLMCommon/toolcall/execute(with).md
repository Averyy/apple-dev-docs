---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcall/execute(with:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# execute(with:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func execute<Input, Output>(with tool: Tool<Input, Output>) async throws -> Output where Input : Decodable, Input : Encodable, Output : Decodable, Output : Encodable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcall/execute(with:))*