# CMDroppedFrameReason.outOfBuffers

**Framework**: Core Media  
**Kind**: case

The frame was dropped because the module providing frames is out of buffers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case outOfBuffers
```

#### Discussion

When the module providing sample buffers has run out of source buffers. This condition is typically caused by the client holding onto buffers for too long and can be alleviated by returning buffers to the provider by releasing the buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmdroppedframereason/outofbuffers)*