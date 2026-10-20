# CWNetwork

**Framework**: Core WLAN  
**Kind**: class  
**Role**: Class

Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class CWNetwork
```

```objc
@interface CWNetwork : NSObject
```

## Topics

### Getting supported security types
- [func supportsSecurity(CWSecurity) -> Bool](./cwnetwork/supportssecurity%28_%29.md)
  Method for determining which security types a network supports.
### Getting supported PHY modes
- [func supportsPHYMode(CWPHYMode) -> Bool](./cwnetwork/supportsphymode%28_%29.md)
  Method for determining which PHY modes a network supports.
### Comparing wireless networks
- [func isEqual(to: CWNetwork) -> Bool](./cwnetwork/isequal%28to%29.md)
  Method for determining CWNetwork object equality.
### Instance Properties
- [var beaconInterval: Int](./cwnetwork/beaconinterval.md)
  The beacon interval (ms) for the network.
- [var bssid: String?](./cwnetwork/bssid.md)
  The basic service set identifier (BSSID) for the network, returned as UTF-8 string.
- [var countryCode: String?](./cwnetwork/countrycode.md)
  The country code (ISO/IEC 3166-1:1997) for the network.
- [var ibss: Bool](./cwnetwork/ibss.md)
  The network is an IBSS network.
- [var informationElementData: Data?](./cwnetwork/informationelementdata.md)
  Information element data included in beacon or probe response frames.
- [var noiseMeasurement: Int](./cwnetwork/noisemeasurement.md)
  The aggregate noise measurement (dBm) for the network.
- [var rssiValue: Int](./cwnetwork/rssivalue.md)
  The aggregate received signal strength indication (RSSI) measurement (dBm) for the network.
- [var ssid: String?](./cwnetwork/ssid.md)
  The service set identifier (SSID) for the network, encoded as a string.
- [var ssidData: Data?](./cwnetwork/ssiddata.md)
  The service set identifier (SSID) for the network, returned as data.
- [var wlanChannel: CWChannel?](./cwnetwork/wlanchannel.md)
  The channel for the network.
### Initializers
- [init?(coder: NSCoder)](./cwnetwork/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Classes
- [class CWChannel](./cwchannel.md)
  Encapsulates an IEEE 802.11 channel.
- [class CWConfiguration](./cwconfiguration.md)
  Encapsulates an immutable configuration for an AirPort WLAN interface.
- [class CWInterface](./cwinterface.md)
  Encapsulates an IEEE 802.11 interface.
- [class CWMutableConfiguration](./cwmutableconfiguration.md)
  Encapsulates a mutable configuration for an AirPort WLAN interface.
- [class CWMutableNetworkProfile](./cwmutablenetworkprofile.md)
  Encapsulates a mutable network profile entry.
- [class CWNetworkProfile](./cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](./cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetwork)*