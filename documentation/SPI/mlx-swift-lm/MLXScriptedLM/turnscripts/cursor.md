---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/turnscripts/cursor"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# TurnScripts.Cursor

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

Where the next token comes from: `scripts[turn][index]`. An `index` equal to the script’s length means the script is used up.

## Declaration

```swift
struct Cursor
```

## Topics

### Initializers
- [init(turn: Int, index: Int)](./cursor/init%28turn,index%29.md)
### Instance Properties
- [let index: Int](./cursor/index.md)
- [let turn: Int](./cursor/turn.md)
### Default Implementations
- [Equatable Implementations](./cursor/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/turnscripts/cursor)*