# resultsLimit

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of records to fetch from the record zone.

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
var resultsLimit: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger resultsLimit;
```

## Discussion

Use this property to limit the number of results in situations where you expect a large number of records. The default value is 0, which causes the server to return an appropriate number of records using dynamic conditions.

When the number of records that CloudKit returns exceeds this limit, the operation sets the `moreComing` property to [`true`](../../../Swift/true.md) when executing the [`recordZoneFetchCompletionBlock`](../recordzonefetchcompletionblock.md) handler.

## See Also

### Zone Change Options
- [var desiredKeys: [String]?](./desiredkeys.md)
  The fields to fetch for the requested records.
- [var previousServerChangeToken: CKServerChangeToken?](./previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneoptions/resultslimit)*