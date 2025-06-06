# AVAudioSession.PolarPattern

**Framework**: AVFAudio  
**Kind**: struct

Constants that describe the possible polar patterns of the data source on an iOS device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct PolarPattern
```

#### Overview

The direction of a polar pattern is relative to the orientation of the data source. For example, you can use the cardioid pattern with a back-facing data source to more clearly record sound from behind the device, or with a front-facing data source to more clearly record sound from in front of the device (such as the user’s voice).

## Topics

### Creating a Polar Pattern
- [init(rawValue: String)](avaudiosession/polarpattern/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.
### Getting Standard Polar Patterns
- [static let stereo: AVAudioSession.PolarPattern](avaudiosession/polarpattern/stereo.md)
  A polar pattern that captures a stereo image of an audio source.
- [static let cardioid: AVAudioSession.PolarPattern](avaudiosession/polarpattern/cardioid.md)
  A data source that’s most sensitive to sound from the direction of the data source and is nearly insensitive to sound from the opposite direction.
- [static let subcardioid: AVAudioSession.PolarPattern](avaudiosession/polarpattern/subcardioid.md)
  A data source that’s most sensitive to sound from the direction of the data source and is less sensitive to sound from the opposite direction.
- [static let omnidirectional: AVAudioSession.PolarPattern](avaudiosession/polarpattern/omnidirectional.md)
  A data source that’s equally sensitive to sound from any direction.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var selectedPolarPattern: AVAudioSession.PolarPattern?](avaudiosessiondatasourcedescription/selectedpolarpattern.md)
  The data source’s active polar pattern.
- [var supportedPolarPatterns: [AVAudioSession.PolarPattern]?](avaudiosessiondatasourcedescription/supportedpolarpatterns.md)
  The set of directivity configurations supported by the data source.
- [var preferredPolarPattern: AVAudioSession.PolarPattern?](avaudiosessiondatasourcedescription/preferredpolarpattern.md)
  The preferred directivity configuration for the data source.
- [func setPreferredPolarPattern(AVAudioSession.PolarPattern?) throws](avaudiosessiondatasourcedescription/setpreferredpolarpattern(_:).md)
  Selects the preferred directivity configuration for the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/polarpattern)*