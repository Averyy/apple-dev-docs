# stopMonitoringAllEvents()

**Framework**: Core WLAN  
**Kind**: method

Unregister for all Wi-Fi event notifications.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func stopMonitoringAllEvents() throws
```

#### Discussion

Use this method when you no longer want to receive any Wi-Fi notifications from the client.

> **Note**:  In order to monitor Wi-Fi events, you must specify the `com.apple.wifi.events` entitlement for your app.

 In order to monitor Wi-Fi events, you must specify the `com.apple.wifi.events` entitlement for your app.

## See Also

- [func startMonitoringEvent(with: CWEventType) throws](cwwificlient/startmonitoringevent(with:).md)
  Register for specific Wi-Fi event notifications.
- [func stopMonitoringEvent(with: CWEventType) throws](cwwificlient/stopmonitoringevent(with:).md)
  Unregister for specific Wi-Fi event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/stopmonitoringallevents())*