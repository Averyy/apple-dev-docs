# RPBroadcastHandler

**Framework**: ReplayKit  
**Kind**: class

An object that sends messages to the broadcasting app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class RPBroadcastHandler
```

## Topics

### Updating Current Broadcast Information
- [func updateServiceInfo([String : any NSCoding & NSObjectProtocol])](rpbroadcasthandler/updateserviceinfo(_:).md)
  Sends information about the current broadcast to the broadcasting app.
- [func updateBroadcast(URL)](rpbroadcasthandler/updatebroadcast(_:).md)
  Sends the current broadcast URL to the broadcast controller.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [RPBroadcastMP4ClipHandler](rpbroadcastmp4cliphandler.md)
- [RPBroadcastSampleHandler](rpbroadcastsamplehandler.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class RPBroadcastController](rpbroadcastcontroller.md)
  An object containing methods for starting and controlling a broadcast.
- [class RPBroadcastSampleHandler](rpbroadcastsamplehandler.md)
  An object that processes buffer objects as received from ReplayKit.
- [class RPBroadcastMP4ClipHandler](rpbroadcastmp4cliphandler.md)
  An object that processes MP4 movie clips from ReplayKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler)*