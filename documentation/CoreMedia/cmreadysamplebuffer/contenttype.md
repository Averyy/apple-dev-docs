# contentType

**Framework**: Core Media  
**Kind**: property

Type of the content carried by this sample buffer

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
var contentType: CMSampleBuffer.ContentType { get }
```

#### Discussion

The content type of the sample buffer can not be changed by assigning a different content, even if content is Dynamic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/contenttype)*