# stopMonitoringEvent(with:)

**Framework**: Core WLAN  
**Kind**: method

Unregister for specific Wi-Fi event notifications.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func stopMonitoringEvent(with type: CWEventType) throws
```

#### Discussion

Use this method to indicate that the client should no longer send notifications for the given event type.

> **Note**:  In order to monitor Wi-Fi events, you must specify the `com.apple.wifi.events` entitlement for your app.

 In order to monitor Wi-Fi events, you must specify the `com.apple.wifi.events` entitlement for your app.

## Parameters

- `type`: The type of event notifications to unregister for. See   for a list of possible values.

## See Also

- [func startMonitoringEvent(with: CWEventType) throws](cwwificlient/startmonitoringevent(with:).md)
  Register for specific Wi-Fi event notifications.
- [func stopMonitoringAllEvents() throws](cwwificlient/stopmonitoringallevents.md)
  Unregister for all Wi-Fi event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/stopmonitoringevent(with:))*