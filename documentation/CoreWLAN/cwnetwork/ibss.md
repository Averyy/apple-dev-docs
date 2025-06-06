# ibss

**Framework**: Core WLAN  
**Kind**: property

The network is an IBSS network.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var ibss: Bool { get }
```

## See Also

- [var beaconInterval: Int](cwnetwork/beaconinterval.md)
  The beacon interval (ms) for the network.
- [var bssid: String?](cwnetwork/bssid.md)
  The basic service set identifier (BSSID) for the network, returned as UTF-8 string.
- [var countryCode: String?](cwnetwork/countrycode.md)
  The country code (ISO/IEC 3166-1:1997) for the network.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetwork/ibss)*