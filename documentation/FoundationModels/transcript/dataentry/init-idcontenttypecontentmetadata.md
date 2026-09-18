# init(id:contentType:content:metadata:)

**Framework**: Foundation Models  
**Kind**: init

Creates a data entry with the content type, content, and metadata you provide.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
init(id: String = UUID().uuidString, contentType: UTType, content: Data, metadata: GeneratedContent = GeneratedContent(properties: [:]))
```

## Parameters

- `id`: A unique identifier for the entry.
- `contentType`: A `UTType` identifying how to interpret `content`.
- `content`: A raw binary representation of the entry.
- `metadata`: Metadata pertinent to this entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/dataentry/init(id:contenttype:content:metadata:))*