# init(taggedBuffers:formatDescription:presentationTimeStamp:duration:)

**Framework**: Core Media  
**Kind**: init

Creates a sample buffer carrying tagged buffers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(taggedBuffers content: Content, formatDescription: CMTaggedBufferGroupFormatDescription? = nil, presentationTimeStamp: CMTime, duration: CMTime = .invalid)
```

## Parameters

- `formatDescription`: Format description of the content. The format must be have tagged buffer group   media type.
- `presentationTimeStamp`: The time at which sample will be presented. Must be valid numeric time.
- `duration`: Duration of the sample. Set to   if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/init(taggedbuffers:formatdescription:presentationtimestamp:duration:))*