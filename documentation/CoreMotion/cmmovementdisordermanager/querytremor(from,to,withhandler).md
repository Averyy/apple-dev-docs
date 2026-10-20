# queryTremor(from:to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Query for tremor results from the provided time interval.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
func queryTremor(from fromDate: Date, to toDate: Date, withHandler handler: @escaping CMTremorResultHandler)
```

#### Discussion

Use this method to asynchronously query for tremor results recorded by the [`monitorKinesias(forDuration:)`](cmmovementdisordermanager/monitorkinesias(forduration:).md) method. The movement disorder manager keeps tremor results for only seven days after the time of recording.

After the manager retrieves the queried results, it calls your handler block from an anonymous background queue. Provide a completion handler to access and process these results.

## Parameters

- `fromDate`: The start date and time of the query. The start must be within the last seven days.
- `toDate`: The end date and time of the query. The end must be within the last seven days, and must be after the start date.
- `handler`: A block for handling the tremor results returned by the query.

## See Also

- [func monitorKinesias(forDuration: TimeInterval)](cmmovementdisordermanager/monitorkinesias(forduration:).md)
  Calculate and store tremor and dyskinetic symptom results for the duration of the specified time interval.
- [typealias CMTremorResultHandler](cmtremorresulthandler.md)
  A completion handler for accessing and processing tremor results.
- [func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)](cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:).md)
  Query for dyskinetic symptoms from the provided time interval.
- [typealias CMDyskineticSymptomResultHandler](cmdyskineticsymptomresulthandler.md)
  A completion handler for processing dyskinetic symptom results.
- [func lastProcessedDate() -> Date?](cmmovementdisordermanager/lastprocesseddate.md)
  Returns the date of the most recently calculated results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querytremor(from:to:withhandler:))*