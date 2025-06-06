# selectedPolarPattern

**Framework**: AVFAudio  
**Kind**: property

The data source’s active polar pattern.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var selectedPolarPattern: AVAudioSession.PolarPattern? { get }
```

#### Discussion

If this value is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0), the data source doesn’t support directivity configuration.

## See Also

- [var supportedPolarPatterns: [AVAudioSession.PolarPattern]?](avaudiosessiondatasourcedescription/supportedpolarpatterns.md)
  The set of directivity configurations supported by the data source.
- [var preferredPolarPattern: AVAudioSession.PolarPattern?](avaudiosessiondatasourcedescription/preferredpolarpattern.md)
  The preferred directivity configuration for the data source.
- [func setPreferredPolarPattern(AVAudioSession.PolarPattern?) throws](avaudiosessiondatasourcedescription/setpreferredpolarpattern(_:).md)
  Selects the preferred directivity configuration for the data source.
- [AVAudioSession.PolarPattern](avaudiosession/polarpattern.md)
  Constants that describe the possible polar patterns of the data source on an iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription/selectedpolarpattern)*