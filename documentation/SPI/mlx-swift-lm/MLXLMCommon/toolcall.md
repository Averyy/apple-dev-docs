---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcall"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCall

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct ToolCall
```

## Topics

### Structures
- [ToolCall.Function](./toolcall/function-swift.struct.md)
  Represents the function details for a tool call
### Initializers
- [init(from: any Decoder) throws](./toolcall/init%28from%29.md)
- [init(function: Function, id: String?)](./toolcall/init%28function,id%29.md)
### Instance Properties
- [let function: Function](./toolcall/function-swift.property.md)
  The function to be called
- [let id: String?](./toolcall/id.md)
  Optional id used to correlate a tool call with its tool result.
### Instance Methods
- [func execute<Input, Output>(with: Tool<Input, Output>) async throws -> Output](./toolcall/execute%28with%29.md)
### Default Implementations
- [Encodable Implementations](./toolcall/encodable-implementations.md)
- [Equatable Implementations](./toolcall/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcall)*