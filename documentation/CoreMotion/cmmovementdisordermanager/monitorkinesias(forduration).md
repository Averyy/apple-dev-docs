# monitorKinesias(forDuration:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Calculate and store tremor and dyskinetic symptom results for the duration of the specified time interval.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
func monitorKinesias(forDuration duration: TimeInterval)
```

```objc
- (void) monitorKinesiasForDuration:(NSTimeInterval) duration;
```

## Mentions

- [Getting movement disorder symptom data](../getting-movement-disorder-symptom-data.md)

#### Discussion

Call this method to begin monitoring, calculating, and storing tremor and dyskinetic symptom results. The manager stores results for a period of seven days after the time of recording. You can access the results at any time within that seven-day interval, after which they expire. To retrieve these results, call the [`queryTremor(from:to:withHandler:)`](./querytremor%28from,to,withhandler%29.md) and [`queryDyskineticSymptom(from:to:withHandler:)`](./querydyskineticsymptom%28from,to,withhandler%29.md) methods.

To determine whether the results are currently being monitored and calculated, call the [`monitorKinesiasExpirationDate()`](./monitorkinesiasexpirationdate%28%29.md) method. The maximum monitoring duration is seven days. In order to continue monitoring beyond the expiration date, you need to renew your subscription by calling [`monitorKinesias(forDuration:)`](./monitorkinesias%28forduration%29.md) again before the monitoring period expires. Note that repeated calls allow you to extend monitoring, but not shorten it.

## Parameters

- `duration`: The monitoring duration in seconds. The maximum duration is seven days.

## See Also

### Related Documentation
- [func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)](./querytremor%28from,to,withhandler%29.md)
  Query for tremor results from the provided time interval.
- [func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)](./querydyskineticsymptom%28from,to,withhandler%29.md)
  Query for dyskinetic symptoms from the provided time interval.
### Recording Movement Disorders
- [func monitorKinesiasExpirationDate() -> Date?](./monitorkinesiasexpirationdate%28%29.md)
  Returns the expiration date for the most recent monitoring period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesias(forduration:))*