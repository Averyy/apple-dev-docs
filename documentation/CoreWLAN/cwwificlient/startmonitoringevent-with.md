# startMonitoringEvent(with:)

**Framework**: Core WLAN  
**Kind**: method

Register for specific Wi-Fi event notifications.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func startMonitoringEvent(with type: CWEventType) throws
```

#### Discussion

After registering for notifications, when an event of the given type happens, the client sends an appropriate message to its delegate. See the [`CWEventDelegate`](cweventdelegate.md) protocol for the complete list of possible messages.

Use the [`stopMonitoringEvent(with:)`](cwwificlient/stopmonitoringevent(with:).md) method when you want to stop receiving notifications of the given event type. Use [`stopMonitoringAllEvents()`](cwwificlient/stopmonitoringallevents().md) to stop receiving all notifications from a client.

> **Note**:  In order to monitor Wi-Fi events, you must specify the `com.apple.wifi.events` entitlement for your app.

 In order to monitor Wi-Fi events, you must specify the `com.apple.wifi.events` entitlement for your app.

## Parameters

- `type`: The type of event notifications to register for. See   for a list of possible values.

## See Also

- [func stopMonitoringAllEvents() throws](cwwificlient/stopmonitoringallevents.md)
  Unregister for all Wi-Fi event notifications.
- [func stopMonitoringEvent(with: CWEventType) throws](cwwificlient/stopmonitoringevent(with:).md)
  Unregister for specific Wi-Fi event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/startmonitoringevent(with:))*