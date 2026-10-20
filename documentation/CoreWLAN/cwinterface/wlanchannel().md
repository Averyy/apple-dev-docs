# wlanChannel()

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

The current channel for the interface.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func wlanChannel() -> CWChannel?
```

```objc
- (CWChannel *) wlanChannel;
```

#### Discussion

Dynamically queries the interface for the current channel. Returns *nil* in the case of an error, or if the interface is not participating in a network.

## See Also

### Instance Methods
- [func activePHYMode() -> CWPHYMode](./activephymode%28%29.md)
  The current active PHY modes for the interface.
- [func bssid() -> String?](./bssid%28%29.md)
  The current basic service set identifier (BSSID) for the interface, returned as a UTF-8 string.
- [func cachedScanResults() -> Set<CWNetwork>?](./cachedscanresults%28%29.md)
  The networks currently in the scan cache for the WLAN interface.
- [func configuration() -> CWConfiguration?](./configuration%28%29.md)
  The current configuration for the given WLAN interface.
- [func countryCode() -> String?](./countrycode%28%29.md)
  The current country code (ISO/IEC 3166-1:1997) for the interface.
- [func hardwareAddress() -> String?](./hardwareaddress%28%29.md)
  The hardware media access control (MAC) address for the interface, returned as a UTF-8 string.
- [func interfaceMode() -> CWInterfaceMode](./interfacemode%28%29.md)
  The current mode for the interface.
- [func noiseMeasurement() -> Int](./noisemeasurement%28%29.md)
  The current aggregate noise measurement (dBm) for the interface.
- [func powerOn() -> Bool](./poweron%28%29.md)
  The interface power state is set to “ON”.
- [func rssiValue() -> Int](./rssivalue%28%29.md)
  The current aggregate received signal strength indication (RSSI) measurement (dBm) for the interface.
- [func scanForNetworks(withName: String?, includeHidden: Bool) throws -> Set<CWNetwork>](./scanfornetworks%28withname,includehidden%29.md)
  Scans for networks with the name you specify, optionally including hidden networks.
- [func scanForNetworks(withSSID: Data?, includeHidden: Bool) throws -> Set<CWNetwork>](./scanfornetworks%28withssid,includehidden%29.md)
  Scans for networks with the SSID you specify, optionally including hidden networks.
- [func security() -> CWSecurity](./security%28%29.md)
  The current security mode for the interface.
- [func serviceActive() -> Bool](./serviceactive%28%29.md)
  The interface has its corresponding network service enabled.
- [func ssid() -> String?](./ssid%28%29.md)
  The current service set identifier (SSID) for the interface, encoded as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/wlanchannel())*