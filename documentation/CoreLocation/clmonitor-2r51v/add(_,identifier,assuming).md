# add(_:identifier:assuming:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Adds the monitoring condition with the identifier and initial state you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
func add(_ condition: any CLCondition, identifier: String, assuming state: CLMonitor.Event.State)
```

## Parameters

- `condition`: The condition to monitor.
- `identifier`: A string that identifies the monitored condition.
- `state`: The monitoring state to initialize the condition with.

## See Also

### Adding and removing conditions
- [func add(any CLCondition, identifier: String)](./add%28_,identifier%29.md)
  Adds the given condition for monitoring.
- [func record(for: String) -> CLMonitor.Record?](./record%28for%29.md)
  A record that contains a condition and the most recent event your app receives.
- [func remove(String)](./remove%28_%29.md)
  Removes the condition and its enclosed record associated with the identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/add(_:identifier:assuming:))*