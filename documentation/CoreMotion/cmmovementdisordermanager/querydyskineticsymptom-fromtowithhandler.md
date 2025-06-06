# queryDyskineticSymptom(from:to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Query for dyskinetic symptoms from the provided time interval.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
func queryDyskineticSymptom(from fromDate: Date, to toDate: Date, withHandler handler: @escaping CMDyskineticSymptomResultHandler)
```

#### Discussion

Use this method to asynchronously query for dyskinetic symptoms recorded by the [`monitorKinesias(forDuration:)`](cmmovementdisordermanager/monitorkinesias(forduration:).md) method. The movement disorder manager keeps dyskinetic symptom results for only seven days after the time of recording.

After the manager retrieves the queried results, it calls your handler block from an anonymous background queue. Provide a completion handler to access and process these results.

## Parameters

- `fromDate`: The start date and time of the query. The start must be within the last seven days.
- `toDate`: The end date and time of the query. The end must be within the last seven days, and must be after the start date.
- `handler`: A block for handling the dyskinetic symptom results returned by the query.

## See Also

- [func monitorKinesias(forDuration: TimeInterval)](cmmovementdisordermanager/monitorkinesias(forduration:).md)
  Calculate and store tremor and dyskinetic symptom results for the duration of the specified time interval.
- [func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)](cmmovementdisordermanager/querytremor(from:to:withhandler:).md)
  Query for tremor results from the provided time interval.
- [typealias CMTremorResultHandler](cmtremorresulthandler.md)
  A completion handler for accessing and processing tremor results.
- [typealias CMDyskineticSymptomResultHandler](cmdyskineticsymptomresulthandler.md)
  A completion handler for processing dyskinetic symptom results.
- [func lastProcessedDate() -> Date?](cmmovementdisordermanager/lastprocesseddate.md)
  Returns the date of the most recently calculated results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:))*