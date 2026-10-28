# ssid

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Instance Property

The service set identifier (SSID) for the network, encoded as a string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var ssid: String? { get }
```

```objc
@property (readonly, nullable) NSString * ssid;
```

## Discussion

If the SSID can not be encoded as a valid UTF-8 or WinLatin1 string, this method returns *nil*.

## See Also

### Instance Properties
- [var beaconInterval: Int](./beaconinterval.md)
  The beacon interval (ms) for the network.
- [var bssid: String?](./bssid.md)
  The basic service set identifier (BSSID) for the network, returned as UTF-8 string.
- [var countryCode: String?](./countrycode.md)
  The country code (ISO/IEC 3166-1:1997) for the network.
- [var ibss: Bool](./ibss.md)
  The network is an IBSS network.
- [var informationElementData: Data?](./informationelementdata.md)
  Information element data included in beacon or probe response frames.
- [var noiseMeasurement: Int](./noisemeasurement.md)
  The aggregate noise measurement (dBm) for the network.
- [var rssiValue: Int](./rssivalue.md)
  The aggregate received signal strength indication (RSSI) measurement (dBm) for the network.
- [var ssidData: Data?](./ssiddata.md)
  The service set identifier (SSID) for the network, returned as data.
- [var wlanChannel: CWChannel?](./wlanchannel.md)
  The channel for the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetwork/ssid)*