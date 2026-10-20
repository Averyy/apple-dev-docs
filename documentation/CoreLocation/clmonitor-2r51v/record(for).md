# record(for:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

A record that contains a condition and the most recent event your app receives.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
func record(for identifier: String) -> CLMonitor.Record?
```

#### Return Value

Returns a [`CLMonitor.Record`](./record.md), or `nil` if the system can’t find the identifier.

## Parameters

- `identifier`: A string that identifies the monitored condition.

## See Also

### Adding and removing conditions
- [func add(any CLCondition, identifier: String)](./add%28_,identifier%29.md)
  Adds the given condition for monitoring.
- [func add(any CLCondition, identifier: String, assuming: CLMonitor.Event.State)](./add%28_,identifier,assuming%29.md)
  Adds the monitoring condition with the identifier and initial state you specify.
- [func remove(String)](./remove%28_%29.md)
  Removes the condition and its enclosed record associated with the identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/record(for:))*