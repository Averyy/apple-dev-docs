# CWWiFiClient

**Framework**: Core WLAN  
**Kind**: class

A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class CWWiFiClient
```

#### Overview

Wi-Fi client objects are heavy. Therefore, it’s more efficient to use a single, long-running client instance, rather than creating several short-lived instances. For convenience, you can use the singleton instance returned by the [`shared()`](cwwificlient/shared().md) class method.

Instead of instantiating [`CWInterface`](cwinterface.md) objects directly, use the ones provided by the instance methods of this class. For example, the [`interface()`](cwwificlient/interface().md) method returns the default Wi-Fi interface.

## Topics

### Getting the Shared Instance
- [class func shared() -> CWWiFiClient](cwwificlient/shared.md)
  The shared Wi-Fi client object.
### Initializing a Wi-Fi Client
- [init()](cwwificlient/init.md)
  Initializes a Wi-Fi client object.
### Setting a Delegate
- [var delegate: AnyObject?](cwwificlient/delegate.md)
  An object that provides Wi-Fi event handling.
### Getting Interfaces
- [func interface() -> CWInterface?](cwwificlient/interface.md)
  Returns the default Wi-Fi interface.
- [func interface(withName: String?) -> CWInterface?](cwwificlient/interface(withname:).md)
  Returns the Wi-Fi interface with the given name.
- [func interfaces() -> [CWInterface]?](cwwificlient/interfaces.md)
  Returns all available Wi-Fi interfaces.
- [class func interfaceNames() -> [String]?](cwwificlient/interfacenames-swift.type.method.md)
  Returns the list of the names of available Wi-Fi interfaces.
### Monitoring Events
- [func startMonitoringEvent(with: CWEventType) throws](cwwificlient/startmonitoringevent(with:).md)
  Register for specific Wi-Fi event notifications.
- [func stopMonitoringAllEvents() throws](cwwificlient/stopmonitoringallevents.md)
  Unregister for all Wi-Fi event notifications.
- [func stopMonitoringEvent(with: CWEventType) throws](cwwificlient/stopmonitoringevent(with:).md)
  Unregister for specific Wi-Fi event notifications.
### Instance Methods
- [func interfaceNames() -> [String]?](cwwificlient/interfacenames-swift.method.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient)*