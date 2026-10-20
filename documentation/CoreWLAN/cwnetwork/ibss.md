# ibss

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

The network is an IBSS network.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var ibss: Bool { get }
```

```objc
@property (readonly) BOOL ibss;
```

## See Also

### Instance Properties
- [var beaconInterval: Int](./beaconinterval.md)
  The beacon interval (ms) for the network.
- [var bssid: String?](./bssid.md)
  The basic service set identifier (BSSID) for the network, returned as UTF-8 string.
- [var countryCode: String?](./countrycode.md)
  The country code (ISO/IEC 3166-1:1997) for the network.
- [var informationElementData: Data?](./informationelementdata.md)
  Information element data included in beacon or probe response frames.
- [var noiseMeasurement: Int](./noisemeasurement.md)
  The aggregate noise measurement (dBm) for the network.
- [var rssiValue: Int](./rssivalue.md)
  The aggregate received signal strength indication (RSSI) measurement (dBm) for the network.
- [var ssid: String?](./ssid.md)
  The service set identifier (SSID) for the network, encoded as a string.
- [var ssidData: Data?](./ssiddata.md)
  The service set identifier (SSID) for the network, returned as data.
- [var wlanChannel: CWChannel?](./wlanchannel.md)
  The channel for the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetwork/ibss)*