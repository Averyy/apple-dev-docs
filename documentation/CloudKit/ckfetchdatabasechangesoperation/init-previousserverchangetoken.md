# init(previousServerChangeToken:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for fetching database changes.

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
convenience init(previousServerChangeToken: CKServerChangeToken?)
```

#### Discussion

After creating the operation, assign a handler to the [`fetchDatabaseChangesCompletionBlock`](ckfetchdatabasechangesoperation/fetchdatabasechangescompletionblock.md) property so that you can process the operation’s results.

If this is your first fetch, or if you want to refetch all zones, pass `nil` for the change token. If you provide a change token from a previous [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md), CloudKit returns only the zones with changes since that token. The per-database [`CKServerChangeToken`](ckserverchangetoken.md) isn’t the same as the per-record zone [`CKServerChangeToken`](ckserverchangetoken.md) from [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md).

## Parameters

- `previousServerChangeToken`: The change token that CloudKit uses to determine which database changes to return.

## See Also

- [init()](ckfetchdatabasechangesoperation/init.md)
  Creates an empty fetch database changes operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/init(previousserverchangetoken:))*