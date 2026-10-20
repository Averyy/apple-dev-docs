# CMTremorResultHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

A completion handler for accessing and processing tremor results.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
typealias CMTremorResultHandler = ([CMTremorResult], (any Error)?) -> Void
```

```c
typedef void (^)(NSArray<CMTremorResult *> *, NSError *) CMTremorResultHandler;
```

## Parameters

- `tremorResult`: An array of tremor results found by the query.
- `error`: If an error occurred, this parameter contains information about the error; otherwise it is `nil`.

## See Also

### Querying for Movement Disorders
- [func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)](./cmmovementdisordermanager/querytremor%28from,to,withhandler%29.md)
  Query for tremor results from the provided time interval.
- [func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)](./cmmovementdisordermanager/querydyskineticsymptom%28from,to,withhandler%29.md)
  Query for dyskinetic symptoms from the provided time interval.
- [typealias CMDyskineticSymptomResultHandler](./cmdyskineticsymptomresulthandler.md)
  A completion handler for processing dyskinetic symptom results.
- [func lastProcessedDate() -> Date?](./cmmovementdisordermanager/lastprocesseddate%28%29.md)
  Returns the date of the most recently calculated results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmtremorresulthandler)*