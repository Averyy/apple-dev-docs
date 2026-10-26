# AVSystemRouteMediaSession

**Framework**: AVSystemRouting  
**Kind**: class  
**Role**: Class

An object that provides playback controls and a data channel for a session running on a remote device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@interface AVSystemRouteMediaSession : NSObject
```

#### Overview

Use this object to access playback controls and a data channel for communicating with the remote application. Call [`startWithCompletionHandler:`](./avsystemroutesession-5i6j6/startwithcompletionhandler_.md) to get this object after adding a session to an [`AVSystemRoute`](./avsystemroute-9kkj3.md).

## Topics

### Instance Properties
- [dataChannel](./avsystemroutemediasession-4mo0j/datachannel.md)
  The data channel for sending and receiving data with the remote application.
- [playbackControl](./avsystemroutemediasession-4mo0j/playbackcontrol.md)
  The playback control interface for the remote session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Playback and communication
- [AVSystemRouteDataDelegate](./avsystemroutedatadelegate-3zbcm.md)
  A protocol for handling data from a remote application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutemediasession-4mo0j)*