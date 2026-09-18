# init(contentType:content:metadata:)

**Framework**: Foundation Models  
**Kind**: init

Creates a data attachment with the content type, content, and metadata you provide.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

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