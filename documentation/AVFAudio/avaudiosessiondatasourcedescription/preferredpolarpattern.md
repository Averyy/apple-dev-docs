# preferredPolarPattern

**Framework**: AVFAudio  
**Kind**: property

The preferred directivity configuration for the data source.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredPolarPattern: AVAudioSession.PolarPattern? { get }
```

#### Discussion

If this value is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0), the data source doesn’t support directivity configuration, or you haven’t selected a preferred polar pattern.

## See Also

- [var selectedPolarPattern: AVAudioSession.PolarPattern?](avaudiosessiondatasourcedescription/selectedpolarpattern.md)
  The data source’s active polar pattern.
- [var supportedPolarPatterns: [AVAudioSession.PolarPattern]?](avaudiosessiondatasourcedescription/supportedpolarpatterns.md)
  The set of directivity configurations supported by the data source.
- [func setPreferredPolarPattern(AVAudioSession.PolarPattern?) throws](avaudiosessiondatasourcedescription/setpreferredpolarpattern(_:).md)
  Selects the preferred directivity configuration for the data source.
- [AVAudioSession.PolarPattern](avaudiosession/polarpattern.md)
  Constants that describe the possible polar patterns of the data source on an iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription/preferredpolarpattern)*