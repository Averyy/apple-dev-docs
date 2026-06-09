# init(rawContent:underlyingError:debugDescription:)

**Framework**: Foundation Models  
**Kind**: init

Creates a parsing failure value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(rawContent: String, underlyingError: (any Error)? = nil, debugDescription: String)
```

## Parameters

- `rawContent`: The raw content that could not be parsed.
- `underlyingError`: The underlying error that caused the parsing failure, if any.
- `debugDescription`: A debug description of what failed to parse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generatedcontent/parsingerror/init(rawcontent:underlyingerror:debugdescription:))*