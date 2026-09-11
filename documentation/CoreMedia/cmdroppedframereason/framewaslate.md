# CMDroppedFrameReason.frameWasLate

**Framework**: Core Media  
**Kind**: case

The frame was dropped because it was late.

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
case frameWasLate
```

#### Discussion

When a video capture client has indicated that late video frames should be dropped and the current frame is late. This condition is typically caused by the client’s processing taking too long.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmdroppedframereason/framewaslate)*