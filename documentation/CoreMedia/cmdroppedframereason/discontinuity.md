# CMDroppedFrameReason.discontinuity

**Framework**: Core Media  
**Kind**: case

An unknown number of frames were dropped.

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
case discontinuity
```

#### Discussion

When the module providing sample buffers has experienced a discontinuity, and an unknown number of frames have been lost. This condition is typically caused by the system being too busy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmdroppedframereason/discontinuity)*