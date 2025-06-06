# init(zoneName:)

**Framework**: CloudKit  
**Kind**: init

Creates a record zone object with the specified zone name.

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
init(zoneName: String)
```

#### Return Value

The new custom zone, or `nil` if CloudKit can’t create the zone.

#### Discussion

Use this method to create a new record zone. The new zone has the name you provide and the zone’s owner is the current user. After creating the zone, save it to the server using a [`CKModifyRecordZonesOperation`](ckmodifyrecordzonesoperation.md) object or the [`save(_:completionHandler:)`](ckdatabase/save(_:completionhandler:)-32ffr.md) method of [`CKDatabase`](ckdatabase.md). You must save the zone to the server before you attempt to save any records to that zone.

Don’t use this method to create a `CKRecordZone` object that corresponds to a zone that already exists in the database. If the zone exists, fetch it using a [`CKFetchRecordZonesOperation`](ckfetchrecordzonesoperation.md) object or the [`fetch(withRecordZoneID:completionHandler:)`](ckdatabase/fetch(withrecordzoneid:completionhandler:).md) method of [`CKDatabase`](ckdatabase.md).

## Parameters

- `zoneName`: If this parameter is   or is an empty string, the method throws an exception.

## See Also

- [init(zoneID: CKRecordZone.ID)](ckrecordzone/init(zoneid:).md)
  Creates a record zone object with the specified zone ID.
- [CKRecordZone.ID](ckrecordzone/id.md)
  An object that uniquely identifies a record zone in a database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/init(zonename:))*