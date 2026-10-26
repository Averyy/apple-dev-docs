---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rejectedtoolcall/reason-swift.enum"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RejectedToolCall.Reason

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Why the model output could not become an executable [`ToolCall`](../toolcall.md).

## Declaration

```swift
enum Reason
```

## Topics

### Enumeration Cases
- [RejectedToolCall.Reason.incompleteOutput](./reason-swift.enum/incompleteoutput.md)
  Generation ended after a recognizable tool-call prefix but before a complete call was available.
- [RejectedToolCall.Reason.invalidArguments](./reason-swift.enum/invalidarguments.md)
  The function arguments could not be represented as a tool input or definitively violated the tool’s declared schema.
- [RejectedToolCall.Reason.malformedSyntax](./reason-swift.enum/malformedsyntax.md)
  A complete tool protocol payload could not be parsed.
- [RejectedToolCall.Reason.missingToolName](./reason-swift.enum/missingtoolname.md)
  The payload looked like a tool call but omitted its function name.
- [RejectedToolCall.Reason.resourceLimitExceeded](./reason-swift.enum/resourcelimitexceeded.md)
  The candidate exceeded the bounded parser budget and was discarded without execution.
- [RejectedToolCall.Reason.undeclaredTool](./reason-swift.enum/undeclaredtool.md)
  The call named a function that was not present in the supplied tools.
### Initializers
- [init?(rawValue: String)](./reason-swift.enum/init%28rawvalue%29.md)
### Default Implementations
- [Encodable Implementations](./reason-swift.enum/encodable-implementations.md)
- [Equatable Implementations](./reason-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](./reason-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.CaseIterable
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rejectedtoolcall/reason-swift.enum)*