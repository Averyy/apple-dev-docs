# AVCoordinatedPlaybackSuspension

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCoordinatedPlaybackSuspension : NSObject
```

## Overview

See the playback coordinator’s [`beginSuspension(for:)`](./avplaybackcoordinator/beginsuspension%28for%29.md) method for details about suspending playback.

## Topics

### Inspecting a suspension
- [var beginDate: Date](./avcoordinatedplaybacksuspension/begindate.md)
  The time the suspension begins.
- [var reason: AVCoordinatedPlaybackSuspension.Reason](./avcoordinatedplaybacksuspension/reason-swift.property.md)
  The reason for the suspension.
- [AVCoordinatedPlaybackSuspension.Reason](./avcoordinatedplaybacksuspension/reason-swift.struct.md)
  Constants that identify playback suspension reasons.
### Ending a suspension
- [func end()](./avcoordinatedplaybacksuspension/end%28%29.md)
  Ends a suspension.
- [func end(proposingNewTime: CMTime)](./avcoordinatedplaybacksuspension/end%28proposingnewtime%29.md)
  Ends a suspension and proposes a new playback time to the group.
### Initializers
- [init(String)](./avcoordinatedplaybacksuspension/reason-swift.struct/init%28_%29.md)
  Creates a suspension with a string.
- [init(rawValue: String)](./avcoordinatedplaybacksuspension/reason-swift.struct/init%28rawvalue%29.md)
  Creates a suspension with a raw string value.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Suspending state coordination
- [func beginSuspension(for: AVCoordinatedPlaybackSuspension.Reason) -> AVCoordinatedPlaybackSuspension](./avplaybackcoordinator/beginsuspension%28for%29.md)
  Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.
- [func expectedItemTime(atHostTime: CMTime) -> CMTime](./avplaybackcoordinator/expecteditemtime%28athosttime%29.md)
  Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension)*