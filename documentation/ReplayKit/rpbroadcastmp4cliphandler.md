# RPBroadcastMP4ClipHandler

**Framework**: ReplayKit  
**Kind**: class  
**Role**: Class

An object that processes MP4 movie clips from ReplayKit.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`RPBroadcastSampleHandler`](./rpbroadcastsamplehandler.md) instead.

## Declaration

```swift
class RPBroadcastMP4ClipHandler
```

```objc
@interface RPBroadcastMP4ClipHandler : RPBroadcastHandler
```

#### Overview

Subclass this class to handle movie clips as ReplayKit records them during the broadcast. The system calls [`processMP4Clip(with:setupInfo:finished:)`](./rpbroadcastmp4cliphandler/processmp4clip%28with,setupinfo,finished%29.md) when a movie clip is available for processing.

## Topics

### Processing MP4 Movie Clips
- [func finishedProcessingMP4Clip(withUpdatedBroadcastConfiguration: RPBroadcastConfiguration?, error: (any Error)?)](./rpbroadcastmp4cliphandler/finishedprocessingmp4clip%28withupdatedbroadcastconfiguration,error%29.md)
  Applies configuration update changes to the next MP4 movie clip.
- [func processMP4Clip(with: URL?, setupInfo: [String : NSObject]?, finished: Bool)](./rpbroadcastmp4cliphandler/processmp4clip%28with,setupinfo,finished%29.md)
  Processes MP4 movie clips for a live broadcast.

## Relationships

### Inherits From
- [RPBroadcastHandler](./rpbroadcasthandler.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Media Clip Processing
- [class RPBroadcastController](./rpbroadcastcontroller.md)
  An object containing methods for starting and controlling a broadcast.
- [class RPBroadcastHandler](./rpbroadcasthandler.md)
  An object that sends messages to the broadcasting app.
- [class RPBroadcastSampleHandler](./rpbroadcastsamplehandler.md)
  An object that processes buffer objects as received from ReplayKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler)*