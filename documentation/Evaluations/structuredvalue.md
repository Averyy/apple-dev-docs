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
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

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

This type is not `@Generable` due to its recursive array or dictionary structure. For generable argument specifications, use `ArgumentValue` instead.

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
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [ExpressibleByBooleanLiteral](../swift/expressiblebybooleanliteral.md)
- [ExpressibleByDictionaryLiteral](../swift/expressiblebydictionaryliteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum ArgumentValue](argumentvalue.md)
  A primitive, generable value type for argument specifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/structuredvalue)*