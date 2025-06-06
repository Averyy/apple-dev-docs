# scanForNetworks(withSSID:includeHidden:)

**Framework**: Core WLAN  
**Kind**: method

Scans for networks with the SSID you specify, optionally including hidden networks.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func scanForNetworks(withSSID ssid: Data?, includeHidden: Bool) throws -> Set<CWNetwork>
```

## See Also

- [func activePHYMode() -> CWPHYMode](cwinterface/activephymode.md)
  The current active PHY modes for the interface.
- [func bssid() -> String?](cwinterface/bssid.md)
  The current basic service set identifier (BSSID) for the interface, returned as a UTF-8 string.
- [func cachedScanResults() -> Set<CWNetwork>?](cwinterface/cachedscanresults.md)
  The networks currently in the scan cache for the WLAN interface.
- [func configuration() -> CWConfiguration?](cwinterface/configuration.md)
  The current configuration for the given WLAN interface.
- [func countryCode() -> String?](cwinterface/countrycode.md)
  The current country code (ISO/IEC 3166-1:1997) for the interface.
- [func hardwareAddress() -> String?](cwinterface/hardwareaddress.md)
  The hardware media access control (MAC) address for the interface, returned as a UTF-8 string.
- [func interfaceMode() -> CWInterfaceMode](cwinterface/interfacemode.md)
  The current mode for the interface.
- [func noiseMeasurement() -> Int](cwinterface/noisemeasurement.md)
  The current aggregate noise measurement (dBm) for the interface.
- [func powerOn() -> Bool](cwinterface/poweron.md)
  The interface power state is set to “ON”.
- [func rssiValue() -> Int](cwinterface/rssivalue.md)
  The current aggregate received signal strength indication (RSSI) measurement (dBm) for the interface.
- [func scanForNetworks(withName: String?, includeHidden: Bool) throws -> Set<CWNetwork>](cwinterface/scanfornetworks(withname:includehidden:).md)
  Scans for networks with the name you specify, optionally including hidden networks.
- [func security() -> CWSecurity](cwinterface/security.md)
  The current security mode for the interface.
- [func serviceActive() -> Bool](cwinterface/serviceactive.md)
  The interface has its corresponding network service enabled.
- [func ssid() -> String?](cwinterface/ssid.md)
  The current service set identifier (SSID) for the interface, encoded as a string.
- [func ssidData() -> Data?](cwinterface/ssiddata.md)
  The current service set identifier (SSID) for the interface, returned as data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/scanfornetworks(withssid:includehidden:))*