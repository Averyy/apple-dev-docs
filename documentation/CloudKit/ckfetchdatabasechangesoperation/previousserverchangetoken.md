# previousServerChangeToken

**Framework**: CloudKit  
**Kind**: property

The server change token.

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
@NSCopying
var previousServerChangeToken: CKServerChangeToken? { get set }
```

#### Discussion

Assign the token you receive from the [`fetchDatabaseChangesCompletionBlock`](ckfetchdatabasechangesoperation/fetchdatabasechangescompletionblock.md) to this property. Doing so yields only the changes that occur after your most recent fetch operation. If you specify `nil` for this parameter, the operation fetches all changes.

## See Also

- [var fetchAllChanges: Bool](ckfetchdatabasechangesoperation/fetchallchanges.md)
  A Boolean value that indicates whether to send repeated requests to the server.
- [var resultsLimit: Int](ckfetchdatabasechangesoperation/resultslimit.md)
  The maximum number of results that the operation fetches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/previousserverchangetoken)*