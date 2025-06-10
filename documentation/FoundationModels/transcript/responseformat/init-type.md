# init(type:)

**Framework**: Foundation Models  
**Kind**: init

Creates a response format with type you specify.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init<Content>(type: Content.Type) where Content : Generable
```

## Parameters

- `type`: A   type to use as the response format.

## See Also

- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(schema: GenerationSchema)](transcript/responseformat/init(schema:).md)
  Creates a response format with a schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/responseformat/init(type:))*