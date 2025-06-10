# JSONEncoder.OutputFormatting

**Framework**: Foundation  
**Kind**: struct

The output formatting options that determine the readability, size, and element order of an encoded JSON object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct OutputFormatting
```

## Topics

### Formatting Output
- [static let prettyPrinted: JSONEncoder.OutputFormatting](jsonencoder/outputformatting-swift.struct/prettyprinted.md)
  The output formatting option that uses ample white space and indentation to make output easy to read.
- [static let sortedKeys: JSONEncoder.OutputFormatting](jsonencoder/outputformatting-swift.struct/sortedkeys.md)
  The output formatting option that sorts keys in lexicographic order.
- [static let withoutEscapingSlashes: JSONEncoder.OutputFormatting](jsonencoder/outputformatting-swift.struct/withoutescapingslashes.md)
  The output formatting option specifies that the output doesn’t prefix slash characters with escape characters.
### Creating Options
- [init(rawValue: UInt)](jsonencoder/outputformatting-swift.struct/init(rawvalue:).md)
  Creates an OutputFormatting value with the given raw value.
- [let rawValue: UInt](jsonencoder/outputformatting-swift.struct/rawvalue.md)
  The format’s default value.
- [init()](jsonencoder/init.md)
  Creates a new, reusable JSON encoder with the default formatting settings and encoding strategies.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var outputFormatting: JSONEncoder.OutputFormatting](jsonencoder/outputformatting-swift.property.md)
  A value that determines the readability, size, and element order of the encoded JSON object.
- [var keyEncodingStrategy: JSONEncoder.KeyEncodingStrategy](jsonencoder/keyencodingstrategy-swift.property.md)
  A value that determines how to encode a  type’s coding keys as JSON keys.
- [JSONEncoder.KeyEncodingStrategy](jsonencoder/keyencodingstrategy-swift.enum.md)
  The values that determine how to encode a type’s coding keys as JSON keys.
- [var userInfo: [CodingUserInfoKey : any Sendable]](jsonencoder/userinfo.md)
  A dictionary you use to customize the encoding process by providing contextual information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/outputformatting-swift.struct)*