# Core WLAN

**Framework**: Core WLAN  
**Kind**: module

Query AirPort interfaces and choose wireless networks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

#### Overview

The CoreWLAN framework provides APIs for querying AirPort interfaces and choosing networks.

You access the Wi-Fi subsystem by working with a [`CWWiFiClient`](cwwificlient.md) instance. This client object provides methods to obtain a handle on all of the system’s Wi-Fi interfaces, represented by [`CWInterface`](cwinterface.md) objects. You can also use the client to register to receive Wi-Fi event notifications. You assign a delegate conforming to the [`CWEventDelegate`](cweventdelegate.md) protocol to process these notifications.

Because creating the client object is resource intensive, it’s usually best to work with a single object over the life of your app rather than creating a series of short lived instances. For convenience, the client class defines a shared instance singleton that you can use for this purpose.

You can use the CoreWLAN framework in an app that adopts App Sandbox without any special exceptions as long as you use the interface objects vended from a client instance. If you initialize interface objects directly, you incur low level system socket accesses that are not considered sandbox safe. For more information about App Sandbox, read [`App Sandbox Design Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183).

## Topics

### Classes
- [class CWChannel](cwchannel.md)
  Encapsulates an IEEE 802.11 channel.
- [class CWConfiguration](cwconfiguration.md)
  Encapsulates an immutable configuration for an AirPort WLAN interface.
- [class CWInterface](cwinterface.md)
  Encapsulates an IEEE 802.11 interface.
- [class CWMutableConfiguration](cwmutableconfiguration.md)
  Encapsulates a mutable configuration for an AirPort WLAN interface.
- [class CWMutableNetworkProfile](cwmutablenetworkprofile.md)
  Encapsulates a mutable network profile entry.
- [class CWNetwork](cwnetwork.md)
  Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- [class CWNetworkProfile](cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.
### Protocols
- [protocol CWEventDelegate](cweventdelegate.md)
  The interface a Wi-Fi client object uses to notify its delegate about Wi-Fi events.
### Reference
- [CoreWLANConstants.h](corewlanconstants-h.md)
- [CoreWLANTypes.h](corewlantypes-h.md)
- [CoreWLANUtil.h](corewlanutil-h.md)
- [CoreWLAN Enumerations](corewlan-enumerations.md)
- [CoreWLAN Functions](corewlan-functions.md)
### Structures
- [struct CWCipherKeyFlags](cwcipherkeyflags.md)
  Cipher key flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreWLAN)*