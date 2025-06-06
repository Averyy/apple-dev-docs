# RPBroadcastController

**Framework**: ReplayKit  
**Kind**: class

An object containing methods for starting and controlling a broadcast.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class RPBroadcastController
```

## Topics

### Controlling the Broadcast
- [var broadcastURL: URL](rpbroadcastcontroller/broadcasturl.md)
  A URL that redirects users to an ongoing or completed broadcast.
- [func startBroadcast(handler: ((any Error)?) -> Void)](rpbroadcastcontroller/startbroadcast(handler:).md)
  Starts a broadcast.
- [func pauseBroadcast()](rpbroadcastcontroller/pausebroadcast.md)
  Pauses the current broadcast.
- [func resumeBroadcast()](rpbroadcastcontroller/resumebroadcast.md)
  Resumes a paused broadcast.
- [func finishBroadcast(handler: ((any Error)?) -> Void)](rpbroadcastcontroller/finishbroadcast(handler:).md)
  Stops the current broadcast.
- [var serviceInfo: [String : any NSCoding & NSObjectProtocol]?](rpbroadcastcontroller/serviceinfo.md)
  Information updated by the service during a broadcast.
### Retrieving Information About the Broadcast
- [var broadcastExtensionBundleID: String?](rpbroadcastcontroller/broadcastextensionbundleid.md)
  The bundle ID for the selected broadcast service.
- [var isBroadcasting: Bool](rpbroadcastcontroller/isbroadcasting.md)
  A Boolean value indicating whether the controller is broadcasting.
- [var isPaused: Bool](rpbroadcastcontroller/ispaused.md)
  A Boolean value indicating whether the broadcast is paused.
### Getting the Delegate
- [var delegate: (any RPBroadcastControllerDelegate)?](rpbroadcastcontroller/delegate.md)
  The delegate for the broadcast controller.
- [protocol RPBroadcastControllerDelegate](rpbroadcastcontrollerdelegate.md)
  The protocol you implement to respond to changes in a live broadcast.

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

- [class RPBroadcastHandler](rpbroadcasthandler.md)
  An object that sends messages to the broadcasting app.
- [class RPBroadcastSampleHandler](rpbroadcastsamplehandler.md)
  An object that processes buffer objects as received from ReplayKit.
- [class RPBroadcastMP4ClipHandler](rpbroadcastmp4cliphandler.md)
  An object that processes MP4 movie clips from ReplayKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller)*