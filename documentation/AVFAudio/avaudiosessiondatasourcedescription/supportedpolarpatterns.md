# supportedPolarPatterns

**Framework**: AVFAudio  
**Kind**: property

The set of directivity configurations supported by the data source.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var supportedPolarPatterns: [AVAudioSession.PolarPattern]? { get }
```

#### Discussion

This property returns an array of one or more polar patterns, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if the data source doesn’t support directivity configuration. This feature is available only on the built-in microphone port for certain devices.

## See Also

- [var selectedPolarPattern: AVAudioSession.PolarPattern?](avaudiosessiondatasourcedescription/selectedpolarpattern.md)
  The data source’s active polar pattern.
- [var preferredPolarPattern: AVAudioSession.PolarPattern?](avaudiosessiondatasourcedescription/preferredpolarpattern.md)
  The preferred directivity configuration for the data source.
- [func setPreferredPolarPattern(AVAudioSession.PolarPattern?) throws](avaudiosessiondatasourcedescription/setpreferredpolarpattern(_:).md)
  Selects the preferred directivity configuration for the data source.
- [AVAudioSession.PolarPattern](avaudiosession/polarpattern.md)
  Constants that describe the possible polar patterns of the data source on an iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription/supportedpolarpatterns)*