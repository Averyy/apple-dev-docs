# RPBroadcastHandler

**Framework**: ReplayKit  
**Kind**: class  
**Role**: Class

An object that sends messages to the broadcasting app.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
class RPBroadcastHandler
```

```objc
@interface RPBroadcastHandler : NSObject
```

## Topics

### Updating Current Broadcast Information
- [func updateServiceInfo([String : any NSCoding & NSObjectProtocol])](./rpbroadcasthandler/updateserviceinfo%28_%29.md)
  Sends information about the current broadcast to the broadcasting app.
- [func updateBroadcast(URL)](./rpbroadcasthandler/updatebroadcast%28_%29.md)
  Sends the current broadcast URL to the broadcast controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [RPBroadcastMP4ClipHandler](./rpbroadcastmp4cliphandler.md)
- [RPBroadcastSampleHandler](./rpbroadcastsamplehandler.md)
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
- [class RPBroadcastSampleHandler](./rpbroadcastsamplehandler.md)
  An object that processes buffer objects as received from ReplayKit.
- [class RPBroadcastMP4ClipHandler](./rpbroadcastmp4cliphandler.md)
  An object that processes MP4 movie clips from ReplayKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler)*