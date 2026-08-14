# ArgumentValue

**Framework**: Evaluations  
**Kind**: enum

A primitive value type for argument specifications that is @Generable.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum ArgumentValue
```

#### Overview

```swift
let city: ArgumentValue = "San Francisco"
let count: ArgumentValue = 5
let score: ArgumentValue = 0.95
```

Unlike `StructuredValue`, this enum only contains primitive types (no recursive array/dictionary) which allows it to work with the @Generable macro.

## Topics

### Values
- [ArgumentValue.string(_:)](argumentvalue/string(_:).md)
  A string value.
- [ArgumentValue.int(_:)](argumentvalue/int(_:).md)
  An integer value.
- [ArgumentValue.double(_:)](argumentvalue/double(_:).md)
  A double-precision floating-point value.
- [ArgumentValue.bool(_:)](argumentvalue/bool(_:).md)
  A Boolean value.
### Converting values
- [var structuredValue: StructuredValue](argumentvalue/structuredvalue.md)
  The equivalent structured value representation of this argument value.
- [enum StructuredValue](structuredvalue.md)
  A type-safe representation of JSON values.

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](../foundationmodels/convertibletogeneratedcontent.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByBooleanLiteral](../swift/expressiblebybooleanliteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Generable](../foundationmodels/generable.md)
- [Hashable](../swift/hashable.md)
- [InstructionsRepresentable](../foundationmodels/instructionsrepresentable.md)
- [PromptRepresentable](../foundationmodels/promptrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum StructuredValue](structuredvalue.md)
  A type-safe representation of JSON values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentvalue)*