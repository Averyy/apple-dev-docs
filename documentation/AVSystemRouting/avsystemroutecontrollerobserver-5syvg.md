# AVSystemRouteControllerObserver

**Framework**: AVSystemRouting  
**Kind**: protocol

A protocol for observers of a system routing controller.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
protocol AVSystemRouteControllerObserver : AnyObject
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

## Topics

### Instance Methods
- [func systemRouteController(AVSystemRouteController, handle: AVSystemRouteEvent) async -> Bool](avsystemroutecontrollerobserver-5syvg/systemroutecontroller(_:handle:).md)
  Connects to, or disconnects from, a device when a user requests it in the picker.

## See Also

- [Routing media to third-party devices](routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
  Send media from an app to nearby remote playback devices.
- [class AVSystemRouteController](avsystemroutecontroller-18ns8.md)
  An object that manages interaction with system routes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontrollerobserver-5syvg)*