# CMDroppedFrameReason.Info.cameraModeSwitch

**Framework**: Core Media  
**Kind**: case

A discontinuity was caused by a camera mode switch.

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
case cameraModeSwitch
```

#### Discussion

When the module providing sample buffers has experienced a discontinuity due to a camera mode switch. Short discontinuities of this type can occur when the session is configured for still image capture on some devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmdroppedframereason/info/cameramodeswitch)*