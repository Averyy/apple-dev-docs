# init(contentType:content:metadata:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a data attachment with the content type, content, and metadata you provide.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
init(contentType: UTType, content: Data, metadata: GeneratedContent = GeneratedContent(properties: [:]))
```

## Parameters

- `contentType`: A `UTType` identifying how to interpret `content`.
- `content`: A raw binary representation of the attachment.
- `metadata`: Metadata pertinent to this attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/dataattachment/init(contenttype:content:metadata:))*