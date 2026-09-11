# CMDroppedFrameReason.discontinuity

**Framework**: Core Media  
**Kind**: case

An unknown number of frames were dropped.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case discontinuity
```

#### Discussion

When the module providing sample buffers has experienced a discontinuity, and an unknown number of frames have been lost. This condition is typically caused by the system being too busy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmdroppedframereason/discontinuity)*