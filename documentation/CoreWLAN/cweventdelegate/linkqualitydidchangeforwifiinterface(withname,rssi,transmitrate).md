# linkQualityDidChangeForWiFiInterface(withName:rssi:transmitRate:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the link quality has changed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
optional func linkQualityDidChangeForWiFiInterface(withName interfaceName: String, rssi: Int, transmitRate: Double)
```

```objc
- (void) linkQualityDidChangeForWiFiInterfaceWithName:(NSString *) interfaceName rssi:(NSInteger) rssi transmitRate:(double) transmitRate;
```

#### Discussion

Register for link quality change notifications by sending the [`startMonitoringEvent(with:)`](../cwwificlient/startmonitoringevent%28with%29.md) message to a Wi-Fi client object with the [`CWEventType.linkQualityDidChange`](../cweventtype/linkqualitydidchange.md) event type.

Use the Wi-Fi interface’s [`rssiValue()`](../cwinterface/rssivalue%28%29.md) and [`transmitRate()`](../cwinterface/transmitrate%28%29.md) methods to query the current RSSI and transmit rate, respectively.

## Parameters

- `interfaceName`: The name of the Wi-Fi interface on which the link quality changed.
- `rssi`: The receive signal strength indicator (RSSI) value measured in dBm for the currently associated network.
- `transmitRate`: The transmit rate measured in Mbps for the currently associated network.

## See Also

### Instance Methods
- [func bssidDidChangeForWiFiInterface(withName: String)](./bssiddidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the current BSSID has changed.
- [func clientConnectionInterrupted()](./clientconnectioninterrupted%28%29.md)
  Tells the delegate that the connection to the Wi-Fi subsystem is temporarily interrupted.
- [func clientConnectionInvalidated()](./clientconnectioninvalidated%28%29.md)
  Tells the delegate that the connection to the Wi-Fi subsystem is permanently invalidated.
- [func countryCodeDidChangeForWiFiInterface(withName: String)](./countrycodedidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the currently adopted country code has changed.
- [func linkDidChangeForWiFiInterface(withName: String)](./linkdidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the Wi-Fi link state changed.
- [func modeDidChangeForWiFiInterface(withName: String)](./modedidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the operating mode has changed.
- [func powerStateDidChangeForWiFiInterface(withName: String)](./powerstatedidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the Wi-Fi power state changed.
- [func scanCacheUpdatedForWiFiInterface(withName: String)](./scancacheupdatedforwifiinterface%28withname%29.md)
  Tells the delegate that the Wi-Fi interface’s scan cache has been updated with new results.
- [func ssidDidChangeForWiFiInterface(withName: String)](./ssiddidchangeforwifiinterface%28withname%29.md)
  Tells the delegate that the current SSID has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cweventdelegate/linkqualitydidchangeforwifiinterface(withname:rssi:transmitrate:))*