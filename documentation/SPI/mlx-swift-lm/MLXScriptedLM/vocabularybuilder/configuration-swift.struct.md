---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/vocabularybuilder/configuration-swift.struct"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# VocabularyBuilder.Configuration

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(maxPieceLength: Int?, reservedSpecialCount: Int, multibyteCharacters: MultibyteCharacters)](./configuration-swift.struct/init%28maxpiecelength,reservedspecialcount,multibytecharacters%29.md)
### Instance Properties
- [var maxPieceLength: Int?](./configuration-swift.struct/maxpiecelength.md)
  Maximum piece length in bytes. `nil` keeps whole words.
- [var multibyteCharacters: MultibyteCharacters](./configuration-swift.struct/multibytecharacters-swift.property.md)
- [var reservedSpecialCount: Int](./configuration-swift.struct/reservedspecialcount.md)
  Ids reserved for atomic specials, below all other tokens.
### Enumerations
- [VocabularyBuilder.Configuration.MultibyteCharacters](./configuration-swift.struct/multibytecharacters-swift.enum.md)
### Default Implementations
- [Equatable Implementations](./configuration-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/vocabularybuilder/configuration-swift.struct)*