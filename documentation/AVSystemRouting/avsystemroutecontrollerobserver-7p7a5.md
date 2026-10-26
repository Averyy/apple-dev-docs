# AVSystemRouteControllerObserver

**Framework**: AVSystemRouting  
**Kind**: protocol  
**Role**: Protocol

A protocol for observers of a system routing controller.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@protocol AVSystemRouteControllerObserver <NSObject>
```

## Topics

### Instance Methods
- [- systemRouteController:handleEvent:completionHandler:](./avsystemroutecontrollerobserver-7p7a5/systemroutecontroller_handleevent_completionhandler_.md)
  Connects to, or disconnects from, a device when a user requests it in the picker.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Essentials
- [Routing media to third-party devices](./routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [Routing and streaming media to remote devices](./routing-and-streaming-media-to-remote-devices.md)
  Send media from an app to nearby remote playback devices.
- [AVSystemRouteController](./avsystemroutecontroller-4teia.md)
  An object that manages interaction with system routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontrollerobserver-7p7a5)*