# startMonitoringEvent(with:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Register for specific Wi-Fi event notifications.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func startMonitoringEvent(with type: CWEventType) throws
```

```objc
- (BOOL) startMonitoringEventWithType:(CWEventType) type error:(NSError **) error;
```

## Discussion

After registering for notifications, when an event of the given type happens, the client sends an appropriate message to its delegate. See the [`CWEventDelegate`](../cweventdelegate.md) protocol for the complete list of possible messages.

Use the [`stopMonitoringEvent(with:)`](./stopmonitoringevent%28with%29.md) method when you want to stop receiving notifications of the given event type. Use [`stopMonitoringAllEvents()`](./stopmonitoringallevents%28%29.md) to stop receiving all notifications from a client.

> **Note**:  In order to monitor Wi-Fi events, you must specify the `com.apple.wifi.events` entitlement for your app.

## Parameters

- `type`: The type of event notifications to register for. See [`CWEventType`](../cweventtype.md) for a list of possible values.

## See Also

### Monitoring Events
- [func stopMonitoringAllEvents() throws](./stopmonitoringallevents%28%29.md)
  Unregister for all Wi-Fi event notifications.
- [func stopMonitoringEvent(with: CWEventType) throws](./stopmonitoringevent%28with%29.md)
  Unregister for specific Wi-Fi event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/startmonitoringevent(with:))*