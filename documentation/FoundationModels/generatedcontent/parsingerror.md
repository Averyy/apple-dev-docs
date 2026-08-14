# GeneratedContent.ParsingError

**Framework**: Foundation Models  
**Kind**: struct

A failure that occurs when a string cannot be parsed into GeneratedContent.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ParsingError
```

## Topics

### Creating an instance
- [init(rawContent: String, underlyingError: (any Error)?, debugDescription: String)](generatedcontent/parsingerror/init(rawcontent:underlyingerror:debugdescription:).md)
  Creates a parsing failure value.
### Inspecting the instance
- [var rawContent: String](generatedcontent/parsingerror/rawcontent.md)
  The raw content that could not be parsed.
- [var underlyingError: (any Error)?](generatedcontent/parsingerror/underlyingerror.md)
  The underlying error that caused the parsing failure, if any.
- [var debugDescription: String](generatedcontent/parsingerror/debugdescription.md)
  A debug description of what failed to parse.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Error](../swift/error.md)
- [Escapable](../swift/escapable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(_:)](generatedcontent/init(_:).md)
  Creates generated content from another value.
- [init(some ConvertibleToGeneratedContent, id: GenerationID)](generatedcontent/init(_:id:).md)
  Creates content that contains a single value with a custom generation identifier.
- [init<S>(elements: S, id: GenerationID?)](generatedcontent/init(elements:id:).md)
  Creates content representing an array of elements you specify.
- [init(properties: KeyValuePairs<String, any ConvertibleToGeneratedContent>, id: GenerationID?)](generatedcontent/init(properties:id:).md)
  Creates generated content representing a structure with the properties you specify.
- [init<S>(properties: S, id: GenerationID?, uniquingKeysWith: (GeneratedContent, GeneratedContent) throws -> some ConvertibleToGeneratedContent) rethrows](generatedcontent/init(properties:id:uniquingkeyswith:).md)
  Creates generated content from key-value pairs, resolving duplicate keys with a combining closure.
- [init(json: String) throws](generatedcontent/init(json:).md)
  Creates equivalent content from a JSON string.
- [init(kind: GeneratedContent.Kind, id: GenerationID?)](generatedcontent/init(kind:id:).md)
  Creates content with the specified kind and generation identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/parsingerror)*