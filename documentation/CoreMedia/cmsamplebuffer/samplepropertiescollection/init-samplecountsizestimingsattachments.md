# init(sampleCount:sizes:timings:attachments:)

**Framework**: Core Media  
**Kind**: init

Create a collection with specified sample information.

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
init(sampleCount: Int, sizes: CMSampleBuffer.SizePerSample?, timings: CMSampleBuffer.TimingPerSample?, attachments: [CMSampleBuffer.SampleAttachments]? = nil)
```

## Parameters

- `sampleCount`: Number of samples. Must be greater than 0.
- `sizes`: Size information of each sample.
- `timings`: Timing information of each sample.
- `attachments`: Attachments for each sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/samplepropertiescollection/init(samplecount:sizes:timings:attachments:))*