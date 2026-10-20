# AVAudioSession.Location

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

Constants that describe the location of the data source on device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct Location
```

```c
typedef NSString * AVAudioSessionLocation;
```

## Topics

### Creating a location
- [init(rawValue: String)](./location/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
### Getting standard locations
- [static let lower: AVAudioSession.Location](./location/lower.md)
  A value that indicates that the data source is located near the bottom end of the device.
- [static let upper: AVAudioSession.Location](./location/upper.md)
  A value that indicates that the data source is located near the top end of the device.
### Deprecated
- [Deprecated symbols](../location-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving the data source location
- [var location: AVAudioSession.Location?](../avaudiosessiondatasourcedescription/location.md)
  The location of the data source on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/location)*