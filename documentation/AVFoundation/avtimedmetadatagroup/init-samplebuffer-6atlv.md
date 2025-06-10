# init(sampleBuffer:)

**Framework**: AVFoundation  
**Kind**: init

Initializes an instance of AVTimedMetadataGroup with a ready sample buffer.

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
convenience init?(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)
```

#### Return Value

An instance of AVTimedMetadataGroup.

## Parameters

- `sampleBuffer`: A CMReadySampleBuffer with media type kCMMediaType_Metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/init(samplebuffer:)-6atlv)*