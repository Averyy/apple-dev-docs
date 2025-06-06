# bssidDidChangeForWiFiInterface(withName:)

**Framework**: Core WLAN  
**Kind**: method

Tells the delegate that the current BSSID has changed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
optional func bssidDidChangeForWiFiInterface(withName interfaceName: String)
```

#### Discussion

Register for BSSID change notifications by sending the [`startMonitoringEvent(with:)`](cwwificlient/startmonitoringevent(with:).md) message to a Wi-Fi client object with the [`CWEventType.bssidDidChange`](cweventtype/bssiddidchange.md) event type.

Use the Wi-Fi interface’s [`bssid()`](cwinterface/bssid().md) method to query the current BSSID.

## Parameters

- `interfaceName`: The name of the Wi-Fi interface on which the BSSID changed.

## See Also

- [func clientConnectionInterrupted()](cweventdelegate/clientconnectioninterrupted.md)
  Tells the delegate that the connection to the Wi-Fi subsystem is temporarily interrupted.
- [func clientConnectionInvalidated()](cweventdelegate/clientconnectioninvalidated.md)
  Tells the delegate that the connection to the Wi-Fi subsystem is permanently invalidated.
- [func countryCodeDidChangeForWiFiInterface(withName: String)](cweventdelegate/countrycodedidchangeforwifiinterface(withname:).md)
  Tells the delegate that the currently adopted country code has changed.
- [func linkDidChangeForWiFiInterface(withName: String)](cweventdelegate/linkdidchangeforwifiinterface(withname:).md)
  Tells the delegate that the Wi-Fi link state changed.
- [func linkQualityDidChangeForWiFiInterface(withName: String, rssi: Int, transmitRate: Double)](cweventdelegate/linkqualitydidchangeforwifiinterface(withname:rssi:transmitrate:).md)
  Tells the delegate that the link quality has changed.
- [func modeDidChangeForWiFiInterface(withName: String)](cweventdelegate/modedidchangeforwifiinterface(withname:).md)
  Tells the delegate that the operating mode has changed.
- [func powerStateDidChangeForWiFiInterface(withName: String)](cweventdelegate/powerstatedidchangeforwifiinterface(withname:).md)
  Tells the delegate that the Wi-Fi power state changed.
- [func scanCacheUpdatedForWiFiInterface(withName: String)](cweventdelegate/scancacheupdatedforwifiinterface(withname:).md)
  Tells the delegate that the Wi-Fi interface’s scan cache has been updated with new results.
- [func ssidDidChangeForWiFiInterface(withName: String)](cweventdelegate/ssiddidchangeforwifiinterface(withname:).md)
  Tells the delegate that the current SSID has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cweventdelegate/bssiddidchangeforwifiinterface(withname:))*