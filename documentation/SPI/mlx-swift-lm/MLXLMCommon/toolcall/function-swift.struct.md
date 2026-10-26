---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcall/function-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCall.Function

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Represents the function details for a tool call

## Declaration

```swift
struct Function
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./function-swift.struct/init%28from%29.md)
- [init(name: String, arguments: [String : JSONValue])](./function-swift.struct/init%28name,arguments%29-17z8x.md)
- [init(name: String, arguments: [String : any Sendable])](./function-swift.struct/init%28name,arguments%29-96420.md)
### Instance Properties
- [let arguments: [String : JSONValue]](./function-swift.struct/arguments.md)
  The arguments passed to the function
- [let name: String](./function-swift.struct/name.md)
  The name of the function
### Default Implementations
- [Encodable Implementations](./function-swift.struct/encodable-implementations.md)
- [Equatable Implementations](./function-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcall/function-swift.struct)*