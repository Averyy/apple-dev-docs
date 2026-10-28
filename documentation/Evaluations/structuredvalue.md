# StructuredValue

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

A type-safe representation of JSON values.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
enum StructuredValue
```

## Overview

```swift
let name: StructuredValue = "Alice"
let score: StructuredValue = 4.5
let tags: StructuredValue = ["swift", "evaluation"]
```

This type is not `@Generable` due to its recursive array or dictionary structure. For generable argument specifications, use `ArgumentValue` instead.

## Topics

### Primitive values
- [StructuredValue.string(_:)](./structuredvalue/string%28_%29.md)
  A string value.
- [StructuredValue.int(_:)](./structuredvalue/int%28_%29.md)
  An integer value.
- [StructuredValue.double(_:)](./structuredvalue/double%28_%29.md)
  A double-precision floating-point value.
- [StructuredValue.bool(_:)](./structuredvalue/bool%28_%29.md)
  A Boolean value.
- [StructuredValue.null](./structuredvalue/null.md)
  A null value.
### Collection values
- [case array([StructuredValue])](./structuredvalue/array%28_%29.md)
  An array of `StructuredValue` instances.
- [case dictionary([String : StructuredValue])](./structuredvalue/dictionary%28_%29.md)
  A dictionary with string keys and `StructuredValue` instances as values.
### Accessing the underlying value
- [var value: Any](./structuredvalue/value.md)
  The underlying value.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [ExpressibleByBooleanLiteral](../Swift/expressiblebybooleanliteral.md)
- [ExpressibleByDictionaryLiteral](../Swift/expressiblebydictionaryliteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [enum ArgumentValue](./argumentvalue.md)
  A primitive, generable value type for argument specifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/structuredvalue)*