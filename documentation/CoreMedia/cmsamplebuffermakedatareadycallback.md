# CMSampleBufferMakeDataReadyCallback

**Framework**: Core Media  
**Kind**: typealias

Client callback called by [`CMSampleBufferMakeDataReady(_:)`](cmsamplebuffermakedataready(_:).md).

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMSampleBufferMakeDataReadyCallback = (CMSampleBuffer, UnsafeMutableRawPointer?) -> OSStatus
```

#### Discussion

This callback must make the data ready (e.g. force a scheduled read to finish). If this callback succeeds and returns 0, the sample buffer will then be marked as “data ready”.

## Parameters

- `sbuf`: The sample buffer to make ready.
- `makeDataReadyRefcon`: For example, it could point at info about the scheduled read that needs to be forced to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffermakedatareadycallback)*