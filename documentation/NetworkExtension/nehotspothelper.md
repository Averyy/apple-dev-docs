# NEHotspotHelper

**Framework**: Network Extension  
**Kind**: class

A class to register a hotspot helper.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class NEHotspotHelper
```

#### Overview

The [`NEHotspotHelper`](nehotspothelper.md) API gives your app the ability to perform custom authentication for Wi-Fi Hotspots. It gives users a way to seamlessly connect to a large aggregated network of Wi-Fi Hotspots. The [`NEHotspotConfiguration`](nehotspotconfiguration.md) API lets your app configure those hotspots.

## Topics

### Registering a hotspot helper
- [class func register(options: [String : NSObject]?, queue: dispatch_queue_t, handler: NEHotspotHelperHandler) -> Bool](nehotspothelper/register(options:queue:handler:).md)
  Register the application as a Hotspot Helper.
- [let kNEHotspotHelperOptionDisplayName: String](knehotspothelperoptiondisplayname.md)
  The string displayed in Wi-Fi Settings for a network handled by the application.
- [typealias NEHotspotHelperHandler](nehotspothelperhandler.md)
  The type definition for the Hotspot Helper’s command handler block.
### Getting hotspot network status
- [class func supportedNetworkInterfaces() -> [Any]?](nehotspothelper/supportednetworkinterfaces.md)
  Return the list of network interfaces managed by the Hotspot Helper infrastructure.
### Logging off
- [class func logoff(NEHotspotNetwork) -> Bool](nehotspothelper/logoff(_:).md)
  Terminate the authentication session for a Hotspot network.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelper)*