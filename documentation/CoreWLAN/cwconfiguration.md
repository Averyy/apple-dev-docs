# CWConfiguration

**Framework**: Core WLAN  
**Kind**: class  
**Role**: Class

Encapsulates an immutable configuration for an AirPort WLAN interface.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class CWConfiguration
```

```objc
@interface CWConfiguration : NSObject
```

## Topics

### Creating a configuration
- [init()](./cwconfiguration/init%28%29.md)
  Creates an empty CWConfiguration object.
- [init(configuration: CWConfiguration)](./cwconfiguration/init%28configuration%29.md)
  Creates and returns a CWConfiguration object initialized with the given CWConfiguration object.
- [+ configuration](./cwconfiguration/configuration.md)
  Convenience method for getting an empty CWConfiguration object.
- [+ configurationWithConfiguration:](./cwconfiguration/configurationwithconfiguration_.md)
  Convenience method for getting a CWConfiguration object initialized with the given CWConfiguration object.
### Comparing configurations
- [func isEqual(to: CWConfiguration) -> Bool](./cwconfiguration/isequal%28to%29.md)
  Determine CWConfiguration object equality.
### Instance Properties
- [var networkProfiles: NSOrderedSet](./cwconfiguration/networkprofiles.md)
  An array of remembered CWNetworkProfile objects.
- [var rememberJoinedNetworks: Bool](./cwconfiguration/rememberjoinednetworks.md)
  AirPort client will remember all joined networks.
- [var requireAdministratorForAssociation: Bool](./cwconfiguration/requireadministratorforassociation.md)
  Require an administrator password to change networks.
- [var requireAdministratorForIBSSMode: Bool](./cwconfiguration/requireadministratorforibssmode.md)
  Require an administrator password to create a computer-to-computer network.
- [var requireAdministratorForPower: Bool](./cwconfiguration/requireadministratorforpower.md)
  Require an administrator password to change the interface power state.
### Initializers
- [init?(coder: NSCoder)](./cwconfiguration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CWMutableConfiguration](./cwmutableconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Classes
- [class CWChannel](./cwchannel.md)
  Encapsulates an IEEE 802.11 channel.
- [class CWInterface](./cwinterface.md)
  Encapsulates an IEEE 802.11 interface.
- [class CWMutableConfiguration](./cwmutableconfiguration.md)
  Encapsulates a mutable configuration for an AirPort WLAN interface.
- [class CWMutableNetworkProfile](./cwmutablenetworkprofile.md)
  Encapsulates a mutable network profile entry.
- [class CWNetwork](./cwnetwork.md)
  Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- [class CWNetworkProfile](./cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](./cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwconfiguration)*