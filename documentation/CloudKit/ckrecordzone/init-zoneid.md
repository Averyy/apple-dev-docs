# init(zoneID:)

**Framework**: CloudKit  
**Kind**: init

Creates a record zone object with the specified zone ID.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(zoneID: CKRecordZone.ID)
```

#### Return Value

The custom record zone, or `nil` if CloudKit can’t create the zone.

#### Discussion

Use this method when you want to create a new record zone from the information in a zone ID. After creating the zone, save it to the server using a [`CKModifyRecordZonesOperation`](ckmodifyrecordzonesoperation.md) object or the [`save(_:completionHandler:)`](ckdatabase/save(_:completionhandler:)-32ffr.md) method of [`CKDatabase`](ckdatabase.md).

Don’t use this method to create a [`CKRecordZone`](ckrecordzone.md) object that corresponds to a zone that already exists in the database. If the zone exists, fetch it using a [`CKFetchRecordZonesOperation`](ckfetchrecordzonesoperation.md) object or the [`fetch(withRecordZoneID:completionHandler:)`](ckdatabase/fetch(withrecordzoneid:completionhandler:).md) method of [`CKDatabase`](ckdatabase.md).

## Parameters

- `zoneID`: The ID for the new zone. This parameter must not be  .

## See Also

- [init(zoneName: String)](ckrecordzone/init(zonename:).md)
  Creates a record zone object with the specified zone name.
- [CKRecordZone.ID](ckrecordzone/id.md)
  An object that uniquely identifies a record zone in a database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/init(zoneid:))*