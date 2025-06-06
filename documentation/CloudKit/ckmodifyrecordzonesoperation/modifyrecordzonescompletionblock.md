# modifyRecordZonesCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute after CloudKit modifies all of the record zones.

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
var modifyRecordZonesCompletionBlock: (([CKRecordZone]?, [CKRecordZone.ID]?, (any Error)?) -> Void)? { get set }
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- The record zones that CloudKit saves.
- The IDs of the record zones that CloudKit deletes.
- If CloudKit can’t modify any of the record zones, this parameter provides information about the failure; otherwise, it’s `nil`.

The closure executes once, and represents your only opportunity to process the results.

The closure reports an error of type [`CKError.Code.partialFailure`](ckerror/code/partialfailure.md) when it modifies only some of the record zones successfully. The [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary of the error contains a [`CKPartialErrorsByItemIDKey`](ckpartialerrorsbyitemidkey.md) key that has a dictionary as its value. The keys of the dictionary are the IDs of the record zones that the operation can’t modify, and the corresponding values are errors that contain information about the failures.

If you intend to use this closure to process the results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/modifyrecordzonescompletionblock)*