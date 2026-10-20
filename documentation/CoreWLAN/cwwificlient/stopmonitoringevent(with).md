# stopMonitoringEvent(with:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Unregister for specific Wi-Fi event notifications.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func stopMonitoringEvent(with type: CWEventType) throws
```

```objc
- (BOOL) stopMonitoringEventWithType:(CWEventType) type error:(NSError **) error;
```

#### Discussion

Use this method to indicate that the client should no longer send notifications for the given event type.

> **Note**:  In order to monitor Wi-Fi events, you must specify the `com.apple.wifi.events` entitlement for your app.

## Parameters

- `type`: The type of event notifications to unregister for. See [`CWEventType`](../cweventtype.md) for a list of possible values.

## See Also

### Monitoring Events
- [func startMonitoringEvent(with: CWEventType) throws](./startmonitoringevent%28with%29.md)
  Register for specific Wi-Fi event notifications.
- [func stopMonitoringAllEvents() throws](./stopmonitoringallevents%28%29.md)
  Unregister for all Wi-Fi event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/stopmonitoringevent(with:))*