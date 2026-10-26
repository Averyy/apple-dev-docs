---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinputprocessor"
framework: "mlx-swift-lm/MLXLMCommon"
---

# UserInputProcessor

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for a type that can convert [`UserInput`](./userinput.md) to [`LMInput`](./lminput.md).

## Declaration

```swift
protocol UserInputProcessor : Sendable
```

#### Overview

See also [`ModelContext`](./modelcontext.md).

## Topics

### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./userinputprocessor/prepare%28input%29.md)

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [MessageGeneratorUserInputProcessor](./messagegeneratoruserinputprocessor.md)
- [StandInUserInputProcessor](./standinuserinputprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinputprocessor)*