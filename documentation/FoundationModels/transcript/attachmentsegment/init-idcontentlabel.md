# init(id:content:label:)

**Framework**: Foundation Models  
**Kind**: init

Creates an attachment segment that wraps the content you provide.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String = UUID().uuidString, content: Transcript.Attachment, label: String? = nil)
```

## Parameters

- `id`: A unique identifier for the segment.
- `content`: The attached file or image.
- `label`: An optional label that identifies the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/attachmentsegment/init(id:content:label:))*