# monitoringRecordForIdentifier:

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Gets the monitoring record containing the condition and most recent monitoring event for the identifier you supply, if applicable.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
- (CLMonitoringRecord *) monitoringRecordForIdentifier:(NSString *) identifier;
```

## Return Value

The monitoring record; otherwise, [`nil`](../../ObjectiveC/nil-227m0.md).

## Parameters

- `identifier`: A string that identifies the monitoring record.

## See Also

### Adding and removing conditions
- [- addConditionForMonitoring:identifier:](./addconditionformonitoring_identifier_.md)
  Adds a condition to monitor with the identifier you provide.
- [- addConditionForMonitoring:identifier:assumedState:](./addconditionformonitoring_identifier_assumedstate_.md)
  Adds a condition to monitor with the state and identifier you provide.
- [- removeConditionFromMonitoringWithIdentifier:](./removeconditionfrommonitoringwithidentifier_.md)
  Removes the monitoring record with the identifier from monitoring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz/monitoringrecordforidentifier:)*