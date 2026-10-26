---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/jsonvalue"
framework: "mlx-swift-lm/MLXLMCommon"
---

# JSONValue

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Type-safe representation of JSON values

## Declaration

```swift
enum JSONValue
```

## Topics

### Enumeration Cases
- [case array([JSONValue])](./jsonvalue/array%28_%29.md)
- [JSONValue.bool(_:)](./jsonvalue/bool%28_%29.md)
- [JSONValue.double(_:)](./jsonvalue/double%28_%29.md)
- [JSONValue.int(_:)](./jsonvalue/int%28_%29.md)
- [JSONValue.null](./jsonvalue/null.md)
- [case object([String : JSONValue])](./jsonvalue/object%28_%29.md)
- [JSONValue.string(_:)](./jsonvalue/string%28_%29.md)
### Initializers
- [init(from: Decoder) throws](./jsonvalue/init%28from%29.md)
### Instance Properties
- [var anyValue: Any](./jsonvalue/anyvalue.md)
- [var asSchema: [String : any Sendable]](./jsonvalue/asschema.md)
  Convert to JSON Schema representation
### Instance Methods
- [func encode(to: Encoder) throws](./jsonvalue/encode%28to%29.md)
### Type Methods
- [static func from(Any) -> JSONValue](./jsonvalue/from%28_%29.md)
### Default Implementations
- [Encodable Implementations](./jsonvalue/encodable-implementations.md)
- [Equatable Implementations](./jsonvalue/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/jsonvalue)*