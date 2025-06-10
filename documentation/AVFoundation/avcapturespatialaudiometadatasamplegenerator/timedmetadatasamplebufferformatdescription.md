# timedMetadataSampleBufferFormatDescription

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var timedMetadataSampleBufferFormatDescription: CMFormatDescription { get }
```

#### Discussion

Returns the CMFormatDescription that will be specified by the buffer returned from the createTimedMetadataSampleBuffer method.

Clients can use this format description when creating their AVAssetWriter track that will contain the metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription)*