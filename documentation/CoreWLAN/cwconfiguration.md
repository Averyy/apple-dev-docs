# CWConfiguration

**Framework**: Core WLAN  
**Kind**: class

Encapsulates an immutable configuration for an AirPort WLAN interface.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class CWConfiguration
```

## Topics

### Creating a configuration
- [init()](cwconfiguration/init.md)
  Creates an empty CWConfiguration object.
- [init(configuration: CWConfiguration)](cwconfiguration/init(configuration:).md)
  Creates and returns a CWConfiguration object initialized with the given CWConfiguration object.
### Comparing configurations
- [func isEqual(to: CWConfiguration) -> Bool](cwconfiguration/isequal(to:).md)
  Determine CWConfiguration object equality.
### Instance Properties
- [var networkProfiles: NSOrderedSet](cwconfiguration/networkprofiles.md)
  An array of remembered CWNetworkProfile objects.
- [var rememberJoinedNetworks: Bool](cwconfiguration/rememberjoinednetworks.md)
  AirPort client will remember all joined networks.
- [var requireAdministratorForAssociation: Bool](cwconfiguration/requireadministratorforassociation.md)
  Require an administrator password to change networks.
- [var requireAdministratorForIBSSMode: Bool](cwconfiguration/requireadministratorforibssmode.md)
  Require an administrator password to create a computer-to-computer network.
- [var requireAdministratorForPower: Bool](cwconfiguration/requireadministratorforpower.md)
  Require an administrator password to change the interface power state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CWMutableConfiguration](cwmutableconfiguration.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwconfiguration)*