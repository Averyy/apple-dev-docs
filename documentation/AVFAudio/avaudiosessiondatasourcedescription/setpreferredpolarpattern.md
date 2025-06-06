# setPreferredPolarPattern(_:)

**Framework**: AVFAudio  
**Kind**: method

Selects the preferred directivity configuration for the data source.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredPolarPattern(_ pattern: AVAudioSession.PolarPattern?) throws
```

#### Discussion

Calling this method requests a change to the selected polar pattern. To determine whether the change has taken effect, inspect the [`selectedPolarPattern`](avaudiosessiondatasourcedescription/selectedpolarpattern.md) property.

If the data source and its owning port are in use, using this method to change the directivity configuration is likely to result in a route reconfiguration.

Set a preferred polar pattern only after setting the audio session’s category and mode, and activating the session.

## Parameters

- `pattern`: The directivity configuration to use.

## See Also

- [var selectedPolarPattern: AVAudioSession.PolarPattern?](avaudiosessiondatasourcedescription/selectedpolarpattern.md)
  The data source’s active polar pattern.
- [var supportedPolarPatterns: [AVAudioSession.PolarPattern]?](avaudiosessiondatasourcedescription/supportedpolarpatterns.md)
  The set of directivity configurations supported by the data source.
- [var preferredPolarPattern: AVAudioSession.PolarPattern?](avaudiosessiondatasourcedescription/preferredpolarpattern.md)
  The preferred directivity configuration for the data source.
- [AVAudioSession.PolarPattern](avaudiosession/polarpattern.md)
  Constants that describe the possible polar patterns of the data source on an iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription/setpreferredpolarpattern(_:))*