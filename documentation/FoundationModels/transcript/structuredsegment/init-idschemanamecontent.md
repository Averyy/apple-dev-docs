# init(id:schemaName:content:)

**Framework**: Foundation Models  
**Kind**: init

Creates a structured segment that contains the generated content you provide.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String = UUID().uuidString, schemaName: String, content: GeneratedContent)
```

## Parameters

- `id`: A unique identifier for the segment.
- `schemaName`: A name that describes which type the content represents.
- `content`: The structured content of the segment.

## See Also

- [init(id: String, source: String, content: GeneratedContent)](transcript/structuredsegment/init(id:source:content:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/structuredsegment/init(id:schemaname:content:))*