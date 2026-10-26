---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/transcript/terminator"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# Transcript.Terminator

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: enum  
**Role**: Enumeration

What ends an assistant turn’s script.

## Declaration

```swift
enum Terminator
```

## Topics

### Enumeration Cases
- [Transcript.Terminator.endOfSequence](./terminator/endofsequence.md)
  The tokenizer’s EOS token, so generation stops on its own.
- [Transcript.Terminator.none](./terminator/none.md)
  Nothing: generation runs until `maxTokens`, emitting unscripted tokens after the script. Those are never a stop token or the turn marker, so the turn cannot end early. Stop strings can still match the decoded text.
### Initializers
- [init?(rawValue: String)](./terminator/init%28rawvalue%29.md)
### Default Implementations
- [Encodable Implementations](./terminator/encodable-implementations.md)
- [Equatable Implementations](./terminator/equatable-implementations.md)
- [RawRepresentable Implementations](./terminator/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/transcript/terminator)*