# CWNetwork

**Framework**: Core WLAN  
**Kind**: class

Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class CWNetwork
```

## Topics

### Getting supported security types
- [func supportsSecurity(CWSecurity) -> Bool](cwnetwork/supportssecurity(_:).md)
  Method for determining which security types a network supports.
### Getting supported PHY modes
- [func supportsPHYMode(CWPHYMode) -> Bool](cwnetwork/supportsphymode(_:).md)
  Method for determining which PHY modes a network supports.
### Comparing wireless networks
- [func isEqual(to: CWNetwork) -> Bool](cwnetwork/isequal(to:).md)
  Method for determining CWNetwork object equality.
### Instance Properties
- [var beaconInterval: Int](cwnetwork/beaconinterval.md)
  The beacon interval (ms) for the network.
- [var bssid: String?](cwnetwork/bssid.md)
  The basic service set identifier (BSSID) for the network, returned as UTF-8 string.
- [var countryCode: String?](cwnetwork/countrycode.md)
  The country code (ISO/IEC 3166-1:1997) for the network.
- [var ibss: Bool](cwnetwork/ibss.md)
  The network is an IBSS network.
- [var informationElementData: Data?](cwnetwork/informationelementdata.md)
  Information element data included in beacon or probe response frames.
- [var noiseMeasurement: Int](cwnetwork/noisemeasurement.md)
  The aggregate noise measurement (dBm) for the network.
- [var rssiValue: Int](cwnetwork/rssivalue.md)
  The aggregate received signal strength indication (RSSI) measurement (dBm) for the network.
- [var ssid: String?](cwnetwork/ssid.md)
  The service set identifier (SSID) for the network, encoded as a string.
- [var ssidData: Data?](cwnetwork/ssiddata.md)
  The service set identifier (SSID) for the network, returned as data.
- [var wlanChannel: CWChannel?](cwnetwork/wlanchannel.md)
  The channel for the network.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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
- [class CWNetworkProfile](cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetwork)*