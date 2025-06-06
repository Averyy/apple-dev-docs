# CMSampleBufferMakeDataReadyHandler

**Framework**: Core Media  
**Kind**: typealias

A block the system calls to make the sample buffer ready for use.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMSampleBufferMakeDataReadyHandler = (CMSampleBuffer) -> OSStatus
```

## Parameters

- `sbuf`: The sample buffer to make ready.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffermakedatareadyhandler)*