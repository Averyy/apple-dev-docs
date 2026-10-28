# ArgumentValue

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

A primitive, generable value type for argument specifications.

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
enum ArgumentValue
```

## Overview

```swift
let city: ArgumentValue = "San Francisco"
let count: ArgumentValue = 5
let score: ArgumentValue = 0.95
```

Unlike `StructuredValue`, this enum only contains primitive types (no recursive array or dictionary) that allows it to work with the `@Generable` macro.

## Topics

### Values
- [ArgumentValue.string(_:)](./argumentvalue/string%28_%29.md)
  A string value.
- [ArgumentValue.int(_:)](./argumentvalue/int%28_%29.md)
  An integer value.
- [ArgumentValue.double(_:)](./argumentvalue/double%28_%29.md)
  A double-precision floating-point value.
- [ArgumentValue.bool(_:)](./argumentvalue/bool%28_%29.md)
  A Boolean value.
### Converting values
- [var structuredValue: StructuredValue](./argumentvalue/structuredvalue.md)
  The equivalent structured value representation of this argument value.
- [enum StructuredValue](./structuredvalue.md)
  A type-safe representation of JSON values.

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../FoundationModels/convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](../FoundationModels/convertibletogeneratedcontent.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByBooleanLiteral](../Swift/expressiblebybooleanliteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Generable](../FoundationModels/generable.md)
- [Hashable](../Swift/hashable.md)
- [InstructionsRepresentable](../FoundationModels/instructionsrepresentable.md)
- [PromptRepresentable](../FoundationModels/promptrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [enum StructuredValue](./structuredvalue.md)
  A type-safe representation of JSON values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentvalue)*