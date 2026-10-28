# previousServerChangeToken

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The token that identifies the starting point for retrieving changes.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- iPadOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- macOS 10.12+ - Deprecated in 10.14 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- tvOS 10.0+ - Deprecated in 12.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)
- watchOS 3.0+ - Deprecated in 5.0 (renamed: CKFetchRecordZoneChangesOperation.ZoneConfiguration)

## Declaration

```swift
@NSCopying
var previousServerChangeToken: CKServerChangeToken? { get set }
```

```objc
@property (nonatomic, copy, nullable) CKServerChangeToken * previousServerChangeToken;
```

## Discussion

Each fetch request returns a unique token in addition to any changes. CloudKit passes the token to your [`recordZoneFetchCompletionBlock`](../recordzonefetchcompletionblock.md) handler. During a subsequent fetch request, providing the previous token causes the server to return only the changes since the previous fetch request. Tokens are opaque values that you can write to disk safely and reuse later.

## See Also

### Zone Change Options
- [var desiredKeys: [String]?](./desiredkeys.md)
  The fields to fetch for the requested records.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of records to fetch from the record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions/previousserverchangetoken)*