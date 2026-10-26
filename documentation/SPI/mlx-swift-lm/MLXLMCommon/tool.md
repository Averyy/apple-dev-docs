---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tool"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Tool

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Tool<Input, Output> where Input : Decodable, Input : Encodable, Output : Decodable, Output : Encodable
```

## Topics

### Initializers
- [init(name: String, description: String, parameters: [ToolParameter], handler: @Sendable (Input) async throws -> Output)](./tool/init%28name,description,parameters,handler%29.md)
- [init(schema: ToolSpec, handler: @Sendable (Input) async throws -> Output)](./tool/init%28schema,handler%29.md)
### Instance Properties
- [let handler: @Sendable (Input) async throws -> Output](./tool/handler.md)
  The handler for the tool.
- [var name: String](./tool/name.md)
  The name of the tool extracted from the schema
- [let schema: ToolSpec](./tool/schema.md)
  The JSON Schema describing the tool’s interface.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolProtocol](./toolprotocol.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tool)*