# init(id:metadata:segments:)

**Framework**: Foundation Models  
**Kind**: init

Creates a response that contains the metadata and segments you provide.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String = UUID().uuidString, metadata: [String : any ConvertibleToGeneratedContent] = [:], segments: [Transcript.Segment])
```

## Parameters

- `id`: A unique identifier for the response.
- `metadata`: Additional information to associate with the response, keyed by name.
- `segments`: The segments of the response, in order.

## See Also

- [init(id: String, assetIDs: [String], segments: [Transcript.Segment])](transcript/response/init(id:assetids:segments:).md)
  Creates a response that contains the segments you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/response/init(id:metadata:segments:))*