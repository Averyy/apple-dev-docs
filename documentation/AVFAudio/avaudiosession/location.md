# AVAudioSession.Location

**Framework**: AVFAudio  
**Kind**: struct

Constants that describe the location of the data source on device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct Location
```

## Topics

### Creating a Location
- [init(rawValue: String)](avaudiosession/location/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.
### Getting Standard Locations
- [static let lower: AVAudioSession.Location](avaudiosession/location/lower.md)
  A value that indicates that the data source is located near the bottom end of the device.
- [static let upper: AVAudioSession.Location](avaudiosession/location/upper.md)
  A value that indicates that the data source is located near the top end of the device.
### Deprecated
- [Deprecated Symbols](location-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Type Properties
- [static var orientationBack: AVAudioSession.Location](avaudiosession/location/orientationback.md)
- [static var orientationBottom: AVAudioSession.Location](avaudiosession/location/orientationbottom.md)
- [static var orientationFront: AVAudioSession.Location](avaudiosession/location/orientationfront.md)
- [static var orientationLeft: AVAudioSession.Location](avaudiosession/location/orientationleft.md)
- [static var orientationRight: AVAudioSession.Location](avaudiosession/location/orientationright.md)
- [static var orientationTop: AVAudioSession.Location](avaudiosession/location/orientationtop.md)
- [static var polarPatternCardioid: AVAudioSession.Location](avaudiosession/location/polarpatterncardioid.md)
- [static var polarPatternOmnidirectional: AVAudioSession.Location](avaudiosession/location/polarpatternomnidirectional.md)
- [static var polarPatternSubcardioid: AVAudioSession.Location](avaudiosession/location/polarpatternsubcardioid.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var location: AVAudioSession.Location?](avaudiosessiondatasourcedescription/location.md)
  The location of the data source on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/location)*