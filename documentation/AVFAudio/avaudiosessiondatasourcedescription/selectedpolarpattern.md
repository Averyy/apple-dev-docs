# selectedPolarPattern

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) AVAudioSessionPolarPattern selectedPolarPattern;
```

## Discussion

If this value is [`nil`](../../ObjectiveC/nil-227m0.md), the data source doesn’t support directivity configuration.

## See Also

### Configuring microphone directivity
- [var supportedPolarPatterns: [AVAudioSession.PolarPattern]?](./supportedpolarpatterns.md)
  The set of directivity configurations supported by the data source.
- [var preferredPolarPattern: AVAudioSession.PolarPattern?](./preferredpolarpattern.md)
  The preferred directivity configuration for the data source.
- [func setPreferredPolarPattern(AVAudioSession.PolarPattern?) throws](./setpreferredpolarpattern%28_%29.md)
  Selects the preferred directivity configuration for the data source.
- [AVAudioSession.PolarPattern](../avaudiosession/polarpattern.md)
  Constants that describe the possible polar patterns of the data source on an iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription/selectedpolarpattern)*