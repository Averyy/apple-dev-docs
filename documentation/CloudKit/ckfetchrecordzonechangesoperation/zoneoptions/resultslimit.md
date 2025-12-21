# resultsLimit

**Framework**: CloudKit  
**Kind**: property

The maximum number of records to fetch from the record zone.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var resultsLimit: Int { get set }
```

#### Discussion

Use this property to limit the number of results in situations where you expect a large number of records. The default value is 0, which causes the server to return an appropriate number of records using dynamic conditions.

When the number of records that CloudKit returns exceeds this limit, the operation sets its [`moreComing`](ckfetchrecordchangesoperation/morecoming.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) before it executes the [`fetchRecordChangesCompletionBlock`](ckfetchrecordchangesoperation/fetchrecordchangescompletionblock.md) handler. In the handler, check the property’s value and, if it’s [`true`](https://developer.apple.com/documentation/Swift/true), create a new [`CKFetchRecordChangesOperation`](ckfetchrecordchangesoperation.md) object to fetch more results.

## See Also

- [var desiredKeys: [String]?](ckfetchrecordzonechangesoperation/zoneoptions/desiredkeys.md)
  The fields to fetch for the requested records.
- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordzonechangesoperation/zoneoptions/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions/resultslimit)*