# preferredPolarPattern

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) AVAudioSessionPolarPattern preferredPolarPattern;
```

#### Discussion

If this value is [`nil`](../../ObjectiveC/nil-227m0.md), the data source doesn’t support directivity configuration, or you haven’t selected a preferred polar pattern.

## See Also

### Configuring microphone directivity
- [var selectedPolarPattern: AVAudioSession.PolarPattern?](./selectedpolarpattern.md)
  The data source’s active polar pattern.
- [var supportedPolarPatterns: [AVAudioSession.PolarPattern]?](./supportedpolarpatterns.md)
  The set of directivity configurations supported by the data source.
- [func setPreferredPolarPattern(AVAudioSession.PolarPattern?) throws](./setpreferredpolarpattern%28_%29.md)
  Selects the preferred directivity configuration for the data source.
- [AVAudioSession.PolarPattern](../avaudiosession/polarpattern.md)
  Constants that describe the possible polar patterns of the data source on an iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription/preferredpolarpattern)*