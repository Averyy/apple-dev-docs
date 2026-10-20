# AVCaptureDevice.Format.AutoFocusSystem.phaseDetection

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

A faster autofoscus system based on differences in light phase.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
case phaseDetection
```

```c
AVCaptureAutoFocusSystemPhaseDetection
```

#### Discussion

Phase detection has the ability to achieve focus in many cases without a focus scan. Phase detection autofocus is typically less visually intrusive than contrast detection autofocus.

## See Also

### Systems
- [AVCaptureDevice.Format.AutoFocusSystem.none](./none.md)
  Autofocus isn’t available.
- [AVCaptureDevice.Format.AutoFocusSystem.contrastDetection](./contrastdetection.md)
  A slower autofocus system based on differences in contrast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/autofocussystem-swift.enum/phasedetection)*