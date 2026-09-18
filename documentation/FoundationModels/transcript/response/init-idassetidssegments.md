# init(id:assetIDs:segments:)

**Framework**: Foundation Models  
**Kind**: init

Creates a response that contains the segments you provide.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String = UUID().uuidString, assetIDs: [String], segments: [Transcript.Segment])
```

## Parameters

- `id`: A unique identifier for the response.
- `assetIDs`: A list of identifiers for the assets used to generate the response.
- `segments`: The segments of the response, in order.

## See Also

- [init(id: String, metadata: [String : any ConvertibleToGeneratedContent], segments: [Transcript.Segment])](transcript/response/init(id:metadata:segments:).md)
  Creates a response that contains the metadata and segments you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/response/init(id:assetids:segments:))*