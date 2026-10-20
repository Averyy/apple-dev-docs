# AVPlaybackSpeed

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVPlaybackSpeed : NSObject
```

## Topics

### Retrieving default speeds
- [class var systemDefaultSpeeds: [AVPlaybackSpeed]](./avplaybackspeed/systemdefaultspeeds.md)
  A list of playback speeds the system uses by default.
### Creating a playback speed
- [init(rate: Float, localizedName: String)](./avplaybackspeed/init%28rate,localizedname%29.md)
  Creates a playback speed with a rate and localized name.
### Inspecting speed details
- [var rate: Float](./avplaybackspeed/rate.md)
  The playback rate to use when you select this speed.
- [var localizedName: String](./avplaybackspeed/localizedname.md)
  A localized name for a speed that’s suitable for display in a user interface.
- [var localizedNumericName: String](./avplaybackspeed/localizednumericname.md)
  A localized numeric name for a speed that’s suitable for display in a user interface.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring the playback speed
- [var speeds: [AVPlaybackSpeed]](./avplayerview/speeds.md)
  A list of user-selectable playback speeds to show in the playback speed control.
- [var selectedSpeed: AVPlaybackSpeed?](./avplayerview/selectedspeed.md)
  The currently selected playback speed.
- [func selectSpeed(AVPlaybackSpeed)](./avplayerview/selectspeed%28_%29.md)
  Selects a specified playback speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackspeed)*