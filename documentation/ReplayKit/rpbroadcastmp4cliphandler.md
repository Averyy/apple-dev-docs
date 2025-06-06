# RPBroadcastMP4ClipHandler

**Framework**: ReplayKit  
**Kind**: class

An object that processes MP4 movie clips from ReplayKit.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class RPBroadcastMP4ClipHandler
```

#### Overview

Subclass this class to handle movie clips as ReplayKit records them during the broadcast. The system calls [`processMP4Clip(with:setupInfo:finished:)`](rpbroadcastmp4cliphandler/processmp4clip(with:setupinfo:finished:).md) when a movie clip is available for processing.

## Topics

### Processing MP4 Movie Clips
- [func finishedProcessingMP4Clip(withUpdatedBroadcastConfiguration: RPBroadcastConfiguration?, error: (any Error)?)](rpbroadcastmp4cliphandler/finishedprocessingmp4clip(withupdatedbroadcastconfiguration:error:).md)
  Applies configuration update changes to the next MP4 movie clip.
- [func processMP4Clip(with: URL?, setupInfo: [String : NSObject]?, finished: Bool)](rpbroadcastmp4cliphandler/processmp4clip(with:setupinfo:finished:).md)
  Processes MP4 movie clips for a live broadcast.

## Relationships

### Inherits From
- [RPBroadcastHandler](rpbroadcasthandler.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class RPBroadcastController](rpbroadcastcontroller.md)
  An object containing methods for starting and controlling a broadcast.
- [class RPBroadcastHandler](rpbroadcasthandler.md)
  An object that sends messages to the broadcasting app.
- [class RPBroadcastSampleHandler](rpbroadcastsamplehandler.md)
  An object that processes buffer objects as received from ReplayKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler)*