# AVPlaybackSpeed

**Framework**: AVKit  
**Kind**: class

An object that represents a user-selectable playback speed in a playback user interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class AVPlaybackSpeed
```

## Topics

### Retrieving Default Speeds
- [class var systemDefaultSpeeds: [AVPlaybackSpeed]](avplaybackspeed/systemdefaultspeeds.md)
  A list of playback speeds the system uses by default.
### Creating a Playback Speed
- [init(rate: Float, localizedName: String)](avplaybackspeed/init(rate:localizedname:).md)
  Creates a playback speed with a rate and localized name.
### Inspecting Speed Details
- [var rate: Float](avplaybackspeed/rate.md)
  The playback rate to use when you select this speed.
- [var localizedName: String](avplaybackspeed/localizedname.md)
  A localized name for a speed that’s suitable for display in a user interface.
- [var localizedNumericName: String](avplaybackspeed/localizednumericname.md)
  A localized numeric name for a speed that’s suitable for display in a user interface.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var speeds: [AVPlaybackSpeed]](avplayerview/speeds.md)
  A list of user-selectable playback speeds to show in the playback speed control.
- [var selectedSpeed: AVPlaybackSpeed?](avplayerview/selectedspeed.md)
  The currently selected playback speed.
- [func selectSpeed(AVPlaybackSpeed)](avplayerview/selectspeed(_:).md)
  Selects a specified playback speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackspeed)*