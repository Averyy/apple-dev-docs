# init(pixelBuffer:formatDescription:presentationTimeStamp:duration:)

**Framework**: Core Media  
**Kind**: init

Creates a sample buffer carrying image buffer.

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
init(pixelBuffer content: Content, formatDescription: CMVideoFormatDescription? = nil, presentationTimeStamp: CMTime, duration: CMTime = .invalid)
```

## Parameters

- `formatDescription`: Format description of the content. If provided, the format must be have video   media type. If not provided, one will be created using  .
- `presentationTimeStamp`: The time at which sample will be presented. Must be valid numeric time.
- `duration`: Duration of the sample. Set to   if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/init(pixelbuffer:formatdescription:presentationtimestamp:duration:))*