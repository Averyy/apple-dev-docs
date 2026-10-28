# AVSystemRouteController

**Framework**: AVSystemRouting  
**Kind**: class  
**Role**: Class

An object that manages interaction with system routes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@interface AVSystemRouteController : NSObject
```

## Overview

Important: Your app must declare support for extensions with the `MDESupportsUniversalURLPlayback` key and/or for specific protocols in the `MDESupportedProtocols` key of  the app’s `Info.plist`.

```xml
<key>MDESupportsUniversalURLPlayback</key>
    <true/>
<key>MDESupportedProtocols</key>
   <dict>
       <key>com.example.sharingprotocol</key>
       <string>com.example.myapplicationidentifier</string>
</dict>
```

Where the key in `MDESupportedProtocols` is the Protocol ID of the extension you are declaring support for and the string value is the application ID of your remote application which the protocol would launch on the receiver.

Use the shared [`sharedController`](./avsystemroutecontroller-4teia/sharedcontroller.md) instance to observe routing events. Register an [`AVSystemRouteControllerObserver`](./avsystemroutecontrollerobserver-7p7a5.md) to receive callbacks when users select or deselect routes in the system route picker.

## Topics

### Instance Methods
- [- addObserver:](./avsystemroutecontroller-4teia/addobserver_.md)
  Adds an observer to receive notifications about system routing events.
- [- removeObserver:](./avsystemroutecontroller-4teia/removeobserver_.md)
  Removes a previously registered observer from the system routing controller.
### Type Properties
- [sharedController](./avsystemroutecontroller-4teia/sharedcontroller.md)
  The shared system routing controller instance.
- [supportedExtensionAvailable](./avsystemroutecontroller-4teia/supportedextensionavailable.md)
  A Boolean value that indicates whether a supported system routing extension is available.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Essentials
- [Routing media to third-party devices](./routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [Routing and streaming media to remote devices](./routing-and-streaming-media-to-remote-devices.md)
  Send media from an app to nearby remote playback devices.
- [AVSystemRouteControllerObserver](./avsystemroutecontrollerobserver-7p7a5.md)
  A protocol for observers of a system routing controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontroller-4teia)*