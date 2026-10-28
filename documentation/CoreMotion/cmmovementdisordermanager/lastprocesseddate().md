# lastProcessedDate()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Returns the date of the most recently calculated results.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
func lastProcessedDate() -> Date?
```

```objc
- (NSDate *) lastProcessedDate;
```

## Return Value

The date of the most recently calculated results, or `nil` if no results are available.

## Discussion

Because the manager processes results in batches, data may not be available immediately.  Use this method to determine the end date for the currently processed data. Additional data will continue to become available, until the manager processes everything up to the monitor expiration date.

This method returns `nil` if you have not yet begun monitoring the user, or if the manager has not yet processed any data.

## See Also

### Querying for Movement Disorders
- [func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)](./querytremor%28from,to,withhandler%29.md)
  Query for tremor results from the provided time interval.
- [typealias CMTremorResultHandler](../cmtremorresulthandler.md)
  A completion handler for accessing and processing tremor results.
- [func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)](./querydyskineticsymptom%28from,to,withhandler%29.md)
  Query for dyskinetic symptoms from the provided time interval.
- [typealias CMDyskineticSymptomResultHandler](../cmdyskineticsymptomresulthandler.md)
  A completion handler for processing dyskinetic symptom results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/lastprocesseddate())*