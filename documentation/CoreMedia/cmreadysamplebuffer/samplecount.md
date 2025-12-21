# sampleCount

**Framework**: Core Media  
**Kind**: property

Number of samples in the sample buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var sampleCount: Int { get }
```

#### Discussion

This value is always equal to `sampleProperties.count`. This value is 0 when `Content` is [`CMSampleBuffer.DynamicContent`](cmsamplebuffer/dynamiccontent.md) and [`contentType`](cmreadysamplebuffer/contenttype.md) is [`CMSampleBuffer.ContentType.markerOnly`](cmsamplebuffer/contenttype-swift.enum/markeronly.md). For all other sample buffer content, this value is greater than 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/samplecount)*