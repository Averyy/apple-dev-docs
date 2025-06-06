# CWMutableConfiguration

**Framework**: Core WLAN  
**Kind**: class

Encapsulates a mutable configuration for an AirPort WLAN interface.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class CWMutableConfiguration
```

#### Overview

Use this class to change configuration settings or the preferred networks list. To commit configuration changes, use [`commitConfiguration(_:authorization:)`](cwinterface/commitconfiguration(_:authorization:).md).

## Topics

### Configuring Preferred Networks
- [var networkProfiles: NSOrderedSet](cwmutableconfiguration/networkprofiles.md)
  The preferred networks list.
### Configuring Settings
- [var rememberJoinedNetworks: Bool](cwmutableconfiguration/rememberjoinednetworks.md)
  A Boolean value that determines whether to remember all joined Wi-Fi networks unless the user specifies otherwise when joining a particular Wi-Fi network.
- [var requireAdministratorForAssociation: Bool](cwmutableconfiguration/requireadministratorforassociation.md)
  A Boolean value that determines whether to require an administrator password to change networks.
- [var requireAdministratorForPower: Bool](cwmutableconfiguration/requireadministratorforpower.md)
  A Boolean value that determines whether to require an administrator password to change the interface power state.
- [var requireAdministratorForIBSSMode: Bool](cwmutableconfiguration/requireadministratorforibssmode.md)
  A Boolean value that determines whether to require an administrator password to create a computer-to-computer network.

## Relationships

### Inherits From
- [CWConfiguration](cwconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CWChannel](cwchannel.md)
  Encapsulates an IEEE 802.11 channel.
- [class CWConfiguration](cwconfiguration.md)
  Encapsulates an immutable configuration for an AirPort WLAN interface.
- [class CWInterface](cwinterface.md)
  Encapsulates an IEEE 802.11 interface.
- [class CWMutableNetworkProfile](cwmutablenetworkprofile.md)
  Encapsulates a mutable network profile entry.
- [class CWNetwork](cwnetwork.md)
  Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- [class CWNetworkProfile](cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration)*