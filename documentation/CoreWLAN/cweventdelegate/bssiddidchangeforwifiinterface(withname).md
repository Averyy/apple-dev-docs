# bssidDidChangeForWiFiInterface(withName:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the current BSSID has changed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
optional func bssidDidChangeForWiFiInterface(withName interfaceName: String)
```

```objc
- (void) bssidDidChangeForWiFiInterfaceWithName:(NSString *) interfaceName;
```

#### Discussion

Register for BSSID change notifications by sending the [`startMonitoringEvent(with:)`](../cwwificlient/startmonitoringevent%28with%29.md) message to a Wi-Fi client object with the [`CWEventType.bssidDidChange`](../cweventtype/bssiddidchange.md) event type.

Use the Wi-Fi interface’s [`bssid()`](../cwinterface/bssid%28%29.md) method to query the current BSSID.

## Parameters

- `interfaceName`: The name of the Wi-Fi interface on which the BSSID changed.

## See Also

### Instance Methods
- [func clientConnectionInterrupted()](./clientconnectioninterrupted%28%29.md)
  Tells the delegate that the connection to the Wi-Fi subsystem is temporarily interrupted.
- [func clientConnectionInvalidated()](./clientconnectioninvalidated%28%29.md)
  Tells the delegate that the connection to the Wi-Fi subsystem is permanently invalidated.
- [func countryCodeDidChangeForWiFiInterface(withName: String)](./countrycodedidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the currently adopted country code has changed.
- [func linkDidChangeForWiFiInterface(withName: String)](./linkdidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the Wi-Fi link state changed.
- [func linkQualityDidChangeForWiFiInterface(withName: String, rssi: Int, transmitRate: Double)](./linkqualitydidchangeforwifiinterface%28withname,rssi,transmitrate%29.md)
  Tells the delegate that the link quality has changed.
- [func modeDidChangeForWiFiInterface(withName: String)](./modedidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the operating mode has changed.
- [func powerStateDidChangeForWiFiInterface(withName: String)](./powerstatedidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the Wi-Fi power state changed.
- [func scanCacheUpdatedForWiFiInterface(withName: String)](./scancacheupdatedforwifiinterface%28withname%29.md)
  Tells the delegate that the Wi-Fi interface’s scan cache has been updated with new results.
- [func ssidDidChangeForWiFiInterface(withName: String)](./ssiddidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the current SSID has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cweventdelegate/bssiddidchangeforwifiinterface(withname:))*