# AVCoordinatedPlaybackSuspension

**Framework**: AVFoundation  
**Kind**: class

An object that represents a temporary suspension of coordinated playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class AVCoordinatedPlaybackSuspension
```

#### Overview

See the playback coordinator’s [`beginSuspension(for:)`](avplaybackcoordinator/beginsuspension(for:).md) method for details about suspending playback.

## Topics

### Inspecting a Suspension
- [var beginDate: Date](avcoordinatedplaybacksuspension/begindate.md)
  The time the suspension begins.
- [var reason: AVCoordinatedPlaybackSuspension.Reason](avcoordinatedplaybacksuspension/reason-swift.property.md)
  The reason for the suspension.
- [AVCoordinatedPlaybackSuspension.Reason](avcoordinatedplaybacksuspension/reason-swift.struct.md)
  Constants that identify playback suspension reasons.
### Ending a Suspension
- [func end()](avcoordinatedplaybacksuspension/end.md)
  Ends a suspension.
- [func end(proposingNewTime: CMTime)](avcoordinatedplaybacksuspension/end(proposingnewtime:).md)
  Ends a suspension and proposes a new playback time to the group.
### Initializers
- [init(String)](avcoordinatedplaybacksuspension/reason-swift.struct/init(_:).md)
  Creates a suspension with a string.
- [init(rawValue: String)](avcoordinatedplaybacksuspension/reason-swift.struct/init(rawvalue:).md)
  Creates a suspension with a raw string value.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [func beginSuspension(for: AVCoordinatedPlaybackSuspension.Reason) -> AVCoordinatedPlaybackSuspension](avplaybackcoordinator/beginsuspension(for:).md)
  Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.
- [func expectedItemTime(atHostTime: CMTime) -> CMTime](avplaybackcoordinator/expecteditemtime(athosttime:).md)
  Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension)*