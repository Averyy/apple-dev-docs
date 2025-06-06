# add(_:identifier:)

**Framework**: Core Location  
**Kind**: method

Adds the given condition for monitoring.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
func add(_ Condition: any CLCondition, identifier: String)
```

#### Discussion

The framework encapsulates the condition in an instance of [`CLMonitor.Record`](clmonitor-2r51v/record.md) and then associates the record, along with the condition with the given identifier. The initial state is [`CLRegionState.unknown`](clregionstate/unknown.md).

## Parameters

- `Condition`: The condition to monitor.
- `identifier`: A string that identifies the monitored condition.

## See Also

- [func add(any CLCondition, identifier: String, assuming: CLMonitor.Event.State)](clmonitor-2r51v/add(_:identifier:assuming:).md)
  Adds the monitoring condition with the identifier and initial state you specify.
- [func record(for: String) -> CLMonitor.Record?](clmonitor-2r51v/record(for:).md)
  A record that contains a condition and the most recent event your app receives.
- [func remove(String)](clmonitor-2r51v/remove(_:).md)
  Removes the condition and its enclosed record associated with the identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/add(_:identifier:))*