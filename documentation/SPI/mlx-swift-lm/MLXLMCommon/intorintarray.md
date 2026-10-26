---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/intorintarray"
framework: "mlx-swift-lm/MLXLMCommon"
---

# IntOrIntArray

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Decodes a JSON value that can be either a single Int or an array of Ints. Used for fields like `eos_token_id` which may appear as `128001` or `[128001, 128008]`.

## Declaration

```swift
struct IntOrIntArray
```

## Topics

### Initializers
- [init([Int])](./intorintarray/init%28_%29-131pz.md)
- [init(Int)](./intorintarray/init%28_%29-3pinf.md)
- [init(from: Decoder) throws](./intorintarray/init%28from%29.md)
### Instance Properties
- [let values: [Int]](./intorintarray/values.md)
### Instance Methods
- [func encode(to: Encoder) throws](./intorintarray/encode%28to%29.md)
### Subscripts
- [subscript(Int) -> Int](./intorintarray/subscript%28_%29.md)
  Get the intermediate size for a specific layer
### Default Implementations
- [Encodable Implementations](./intorintarray/encodable-implementations.md)
- [Equatable Implementations](./intorintarray/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/intorintarray)*