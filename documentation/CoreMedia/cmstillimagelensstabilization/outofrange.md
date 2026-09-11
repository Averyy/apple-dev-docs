# CMStillImageLensStabilization.outOfRange

**Framework**: Core Media  
**Kind**: case

The motion of the device or duration of the capture was outside of what the stabilization mechanism could support.

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
case outOfRange
```

#### Discussion

The value of kCMSampleBufferAttachmentKey_StillImageLensStabilizationInfo if the module stabilizing the lens was unable to compensate for the movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmstillimagelensstabilization/outofrange)*