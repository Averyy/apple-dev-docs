---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/stringornumber"
framework: "mlx-swift-lm/MLXLMCommon"
---

# StringOrNumber

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Representation of a heterogenous type in a JSON configuration file.

## Declaration

```swift
enum StringOrNumber
```

#### Overview

This can be: a string, a numeric value or an array of numeric values. There are methods to do unwrapping, see e.g. [`asFloat()`](./stringornumber/asfloat%28%29.md) and [`asFloats()`](./stringornumber/asfloats%28%29.md) or callers can switch on the enum.

## Topics

### Enumeration Cases
- [StringOrNumber.bool(_:)](./stringornumber/bool%28_%29.md)
- [StringOrNumber.float(_:)](./stringornumber/float%28_%29.md)
- [StringOrNumber.floats(_:)](./stringornumber/floats%28_%29.md)
- [StringOrNumber.int(_:)](./stringornumber/int%28_%29.md)
- [StringOrNumber.ints(_:)](./stringornumber/ints%28_%29.md)
- [StringOrNumber.string(_:)](./stringornumber/string%28_%29.md)
### Initializers
- [init(from: Decoder) throws](./stringornumber/init%28from%29.md)
### Instance Methods
- [func asFloat() -> Float?](./stringornumber/asfloat%28%29.md)
  Return the value as an optional float.
- [func asFloats() -> [Float]?](./stringornumber/asfloats%28%29.md)
  Return the value as an optional array of floats.
- [func asInt() -> Int?](./stringornumber/asint%28%29.md)
  Return the value as an optional integer.
- [func asInts() -> [Int]?](./stringornumber/asints%28%29.md)
  Return the value as an optional array of integers.
- [func encode(to: Encoder) throws](./stringornumber/encode%28to%29.md)
### Default Implementations
- [Encodable Implementations](./stringornumber/encodable-implementations.md)
- [Equatable Implementations](./stringornumber/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/stringornumber)*