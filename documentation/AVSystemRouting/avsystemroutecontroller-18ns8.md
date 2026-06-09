# AVSystemRouteController

**Framework**: AVSystemRouting  
**Kind**: class

An object that manages interaction with system routes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class AVSystemRouteController
```

## Mentions

- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

#### Overview

Important: Your app must declare support for Media Sharing Extensions with the `MDESupportsUniversalURLPlayback` key and/or for specific protocols in the `MDESupportedProtocols` key of  the app’s `Info.plist`.  ///

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

Use the shared [`shared`](avsystemroutecontroller-18ns8/shared.md) instance to observe routing events. Register an [`AVSystemRouteControllerObserver`](avsystemroutecontrollerobserver-5syvg.md) to receive callbacks when users select or deselect routes in the system route picker.

## Topics

### Instance Methods
- [func addObserver(any AVSystemRouteControllerObserver) -> Bool](avsystemroutecontroller-18ns8/addobserver(_:).md)
  Adds an observer to receive notifications about system routing events.
- [func removeObserver(any AVSystemRouteControllerObserver)](avsystemroutecontroller-18ns8/removeobserver(_:).md)
  Removes a previously registered observer from the system routing controller.
### Type Properties
- [class var shared: AVSystemRouteController](avsystemroutecontroller-18ns8/shared.md)
  The shared system routing controller instance.
- [class var supportedExtensionAvailable: Bool](avsystemroutecontroller-18ns8/supportedextensionavailable.md)
  A Boolean value that indicates whether a supported system routing extension is available.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Routing media to third-party devices](routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
  Send media from an app to nearby remote playback devices.
- [protocol AVSystemRouteControllerObserver](avsystemroutecontrollerobserver-5syvg.md)
  A protocol for observers of a system routing controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontroller-18ns8)*