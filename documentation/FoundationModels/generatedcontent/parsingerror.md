# GeneratedContent.ParsingError

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A failure that occurs when a string cannot be parsed into generated content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ParsingError
```

## Topics

### Creating an instance
- [init(rawContent: String, underlyingError: (any Error)?, debugDescription: String)](./parsingerror/init%28rawcontent,underlyingerror,debugdescription%29.md)
  Creates a parsing failure value.
### Inspecting the instance
- [var rawContent: String](./parsingerror/rawcontent.md)
  The raw content that could not be parsed.
- [var underlyingError: (any Error)?](./parsingerror/underlyingerror.md)
  The underlying error that caused the parsing failure, if any.
- [var debugDescription: String](./parsingerror/debugdescription.md)
  A debug description of what failed to parse.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating generated content
- [init(_:)](./init%28_%29.md)
  Creates generated content from another value.
- [init(some ConvertibleToGeneratedContent, id: GenerationID)](./init%28_,id%29.md)
  Creates content that contains a single value with a custom generation identifier.
- [init<S>(elements: S, id: GenerationID?)](./init%28elements,id%29.md)
  Creates content representing an array of elements you specify.
- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID?)](./init%28properties,id%29.md)
  Creates generated content representing a structure with the properties you specify.
- [init<S>(properties: S, id: GenerationID?, uniquingKeysWith: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows](./init%28properties,id,uniquingkeyswith%29.md)
  Creates generated content from key-value pairs, resolving duplicate keys with a combining closure.
- [init(json: String) throws](./init%28json%29.md)
  Creates equivalent content from a JSON string.
- [init(kind: GeneratedContent.Kind, id: GenerationID?)](./init%28kind,id%29.md)
  Creates content with the specified kind and generation identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/parsingerror)*