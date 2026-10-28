# init(recordZoneID:previousServerChangeToken:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an operation for fetching changes in the specified record zone.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- iPadOS 8.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CKFetchRecordZoneChangesOperation)
- macOS 10.10+ - Deprecated in 10.12 (renamed: CKFetchRecordZoneChangesOperation)
- tvOS 9.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CKFetchRecordZoneChangesOperation)
- watchOS 3.0+ - Deprecated in 3.0 (renamed: CKFetchRecordZoneChangesOperation)

## Declaration

```swift
convenience init(recordZoneID: CKRecordZone.ID, previousServerChangeToken: CKServerChangeToken?)
```

```objc
- (instancetype) initWithRecordZoneID:(CKRecordZoneID *) recordZoneID previousServerChangeToken:(CKServerChangeToken *) previousServerChangeToken;
```

## Return Value

An initialized operation object.

## Discussion

When initializing the operation object, use the token from a previous fetch request if you have one. You can archive tokens and write them to disk for later use.

The returned operation object retrieves all changed fields of the record, including any assets in those fields. If you want to minimize the amount of data that returns even further, configure the [`desiredKeys`](./desiredkeys.md) property with the subset of keys that have values you want to fetch.

After initializing the operation, associate at least one progress block with the operation object (excluding the completion block) to process the results.

## Parameters

- `recordZoneID`: The zone that contains the records you want to fetch. You can fetch changes in a custom zone. CloudKit doesn’t support syncing the default zone.
- `previousServerChangeToken`: The change token from a previous fetch operation. This is the token that the system passes to your [`fetchRecordChangesCompletionBlock`](./fetchrecordchangescompletionblock.md) handler during a previous fetch operation. Use this token to limit the returned data to only those changes that occur after that fetch request. If you specify `nil` for this parameter, the operation object fetches all records and their contents.

## See Also

### Creating the Fetch Record Changes Operation
- [init()](./init%28%29.md)
  Creates an empty fetch record changes operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/init(recordzoneid:previousserverchangetoken:))*