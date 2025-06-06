# CWEventDelegate

**Framework**: Core WLAN  
**Kind**: protocol

The interface a Wi-Fi client object uses to notify its delegate about Wi-Fi events.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```swift
protocol CWEventDelegate
```

#### Overview

An object that adopts the `CWEventDelegate` protocol and that is assigned as the delegate of a [`CWWiFiClient`](cwwificlient.md) object receives notifications of changes on a Wi-Fi interface. Use the [`startMonitoringEvent(with:)`](cwwificlient/startmonitoringevent(with:).md) method to indicate to the client the event types for which you want to receive notifications. Use the [`stopMonitoringEvent(with:)`](cwwificlient/stopmonitoringevent(with:).md) method to stop receiving a particular notification type, or the [`stopMonitoringAllEvents()`](cwwificlient/stopmonitoringallevents().md) method to stop receiving all notifications.

## Topics

### Instance Methods
- [func bssidDidChangeForWiFiInterface(withName: String)](cweventdelegate/bssiddidchangeforwifiinterface(withname:).md)
  Tells the delegate that the current BSSID has changed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cweventdelegate)*