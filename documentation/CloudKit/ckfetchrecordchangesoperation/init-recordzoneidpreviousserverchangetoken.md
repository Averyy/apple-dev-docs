# init(recordZoneID:previousServerChangeToken:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for fetching changes in the specified record zone.

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
convenience init(recordZoneID: CKRecordZone.ID, previousServerChangeToken: CKServerChangeToken?)
```

#### Return Value

An initialized operation object.

#### Discussion

When initializing the operation object, use the token from a previous fetch request if you have one. You can archive tokens and write them to disk for later use.

The returned operation object retrieves all changed fields of the record, including any assets in those fields. If you want to minimize the amount of data that returns even further, configure the [`desiredKeys`](ckfetchrecordchangesoperation/desiredkeys.md) property with the subset of keys that have values you want to fetch.

After initializing the operation, associate at least one progress block with the operation object (excluding the completion block) to process the results.

## Parameters

- `recordZoneID`: The zone that contains the records you want to fetch. The zone can be a custom zone. The system doesn’t support syncing the default zone.
- `previousServerChangeToken`: The change token from a previous fetch operation. This is the token that the system passes to your   handler during a previous fetch operation. Use this token to limit the returned data to only those changes that occur after that fetch request. If you specify   for this parameter, the operation object fetches all records and their contents.

## See Also

- [init()](ckfetchrecordchangesoperation/init.md)
  Creates an empty fetch record changes operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/init(recordzoneid:previousserverchangetoken:))*