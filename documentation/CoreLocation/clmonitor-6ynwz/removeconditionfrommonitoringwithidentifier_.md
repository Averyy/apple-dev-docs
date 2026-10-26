# removeConditionFromMonitoringWithIdentifier:

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Removes the monitoring record with the identifier from monitoring.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
- (void) removeConditionFromMonitoringWithIdentifier:(NSString *) identifier;
```

## Parameters

- `identifier`: A string that identifies the monitoring record.

## See Also

### Adding and removing conditions
- [- addConditionForMonitoring:identifier:](./addconditionformonitoring_identifier_.md)
  Adds a condition to monitor with the identifier you provide.
- [- addConditionForMonitoring:identifier:assumedState:](./addconditionformonitoring_identifier_assumedstate_.md)
  Adds a condition to monitor with the state and identifier you provide.
- [- monitoringRecordForIdentifier:](./monitoringrecordforidentifier_.md)
  Gets the monitoring record containing the condition and most recent monitoring event for the identifier you supply, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz/removeconditionfrommonitoringwithidentifier:)*