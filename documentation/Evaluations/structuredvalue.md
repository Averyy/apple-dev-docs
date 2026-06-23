# StructuredValue

**Framework**: Evaluations  
**Kind**: enum

A type-safe representation of JSON values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum StructuredValue
```

#### Overview

```swift
let name: StructuredValue = "Alice"
let score: StructuredValue = 4.5
let tags: StructuredValue = ["swift", "evaluation"]
```

This type is not `@Generable` due to its recursive array/dictionary structure. For generable argument specifications, use `ArgumentValue` instead.

## Topics

### Primitive values
- [StructuredValue.string(_:)](structuredvalue/string(_:).md)
  A string value.
- [StructuredValue.int(_:)](structuredvalue/int(_:).md)
  An integer value.
- [StructuredValue.double(_:)](structuredvalue/double(_:).md)
  A double-precision floating-point value.
- [StructuredValue.bool(_:)](structuredvalue/bool(_:).md)
  A Boolean value.
- [StructuredValue.null](structuredvalue/null.md)
  A null value.
### Collection values
- [case array([StructuredValue])](structuredvalue/array(_:).md)
  An array of `StructuredValue` instances.
- [case dictionary([String : StructuredValue])](structuredvalue/dictionary(_:).md)
  A dictionary with string keys and `StructuredValue` instances as values.
### Accessing the underlying value
- [var value: Any](structuredvalue/value.md)
  The underlying value.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [ExpressibleByBooleanLiteral](../Swift/ExpressibleByBooleanLiteral.md)
- [ExpressibleByDictionaryLiteral](../Swift/ExpressibleByDictionaryLiteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ArgumentValue](argumentvalue.md)
  A primitive value type for argument specifications that is @Generable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/structuredvalue)*