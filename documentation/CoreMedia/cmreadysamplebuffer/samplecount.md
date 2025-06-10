# sampleCount

**Framework**: Core Media  
**Kind**: property

Number of samples in the sample buffer.

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
var sampleCount: Int { get }
```

#### Discussion

This value is always equal to `sampleProperties.count`. This value is 0 when `Content` is [`CMSampleBuffer.DynamicContent`](cmsamplebuffer/dynamiccontent.md) and [`contentType`](cmreadysamplebuffer/contenttype.md) is [`CMSampleBuffer.ContentType.markerOnly`](cmsamplebuffer/contenttype-swift.enum/markeronly.md). For all other sample buffer content, this value is greater than 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/samplecount)*