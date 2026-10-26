# addConditionForMonitoring:identifier:assumedState:

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Adds a condition to monitor with the state and identifier you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
- (void) addConditionForMonitoring:(CLCondition *) condition identifier:(NSString *) identifier assumedState:(CLMonitoringState) state;
```

## Parameters

- `condition`: A [`CLCondition`](../clcondition-swift.protocol.md) to monitor for.
- `identifier`: A string you use to identify this condition.
- `state`: A [`CLMonitoringState`](../clmonitoringstate.md) that satisfies `condition`.

## See Also

### Adding and removing conditions
- [- addConditionForMonitoring:identifier:](./addconditionformonitoring_identifier_.md)
  Adds a condition to monitor with the identifier you provide.
- [- monitoringRecordForIdentifier:](./monitoringrecordforidentifier_.md)
  Gets the monitoring record containing the condition and most recent monitoring event for the identifier you supply, if applicable.
- [- removeConditionFromMonitoringWithIdentifier:](./removeconditionfrommonitoringwithidentifier_.md)
  Removes the monitoring record with the identifier from monitoring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz/addconditionformonitoring:identifier:assumedstate:)*