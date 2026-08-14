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

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var location: AVAudioSession.Location?](avaudiosessiondatasourcedescription/location.md)
  The location of the data source on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/location)*