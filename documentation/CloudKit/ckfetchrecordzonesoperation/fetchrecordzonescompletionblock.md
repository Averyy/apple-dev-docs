# fetchRecordZonesCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute after CloudKit retrieves all of the record zones.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var fetchRecordZonesCompletionBlock: (([CKRecordZone.ID : CKRecordZone]?, (any Error)?) -> Void)? { get set }
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- A dictionary that maps the zone IDs you request to the results. The keys in the dictionary are [`CKRecordZone.ID`](ckrecordzone/id.md) objects, and the values are the corresponding [`CKRecordZone`](ckrecordzone.md) objects that CloudKit returns.
- If CloudKit can’t retrieve any of the record zones, an error that provides information about the failure; otherwise, `nil`.

The operation executes the closure only once, and it’s your only chance to process the results. The closure must be capable of executing on a background thread, so any tasks that require access to the main thread must redirect accordingly.

The closure reports an error of type [`CKError.Code.partialFailure`](ckerror/code/partialfailure.md) when it retrieves only some of the record zones successfully. The [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary of the error contains a [`CKPartialErrorsByItemIDKey`](ckpartialerrorsbyitemidkey.md) key that has a dictionary as its value. The keys of the dictionary are the IDs of the record zones that the operation can’t retrieve, and the corresponding values are errors that contain information about the failures.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/fetchrecordzonescompletionblock)*