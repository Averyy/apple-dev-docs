# videoFrameRateRangeForBackgroundReplacement

**Framework**: AVFoundation  
**Kind**: property

The minimum and maximum frame rates available when Background Replacement is active.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var videoFrameRateRangeForBackgroundReplacement: AVFrameRateRange? { get }
```

#### Discussion

Devices may support a limited frame rate range when Background Replacement is active. If this device format doesn’t support this feature, the value of this property is `nil`.

## See Also

- [var isBackgroundReplacementSupported: Bool](avcapturedevice/format/isbackgroundreplacementsupported.md)
  A Boolean value that indicates whether the format supports background replacement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforbackgroundreplacement)*