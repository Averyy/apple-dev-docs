# init(recordName:zoneID:)

**Framework**: CloudKit  
**Kind**: init

Creates a new record ID with the specified name and zone information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
convenience init(recordName: String = UUID().uuidString, zoneID: CKRecordZone.ID = CKRecordZone.ID.default)
```

#### Discussion

Use this method when you create or search for records in a zone other than the default zone. The value in the `zoneID` parameter must represent a zone that already exists in the database. If the record zone doesn’t exist, save the corresponding [`CKRecordZone`](ckrecordzone.md) object to the database before attempting to save any [`CKRecord`](ckrecord.md) objects in that zone.

## Parameters

- `recordName`: The name that identifies the record. The string must contain only ASCII characters, must not exceed 255 characters, and must not start with an underscore. If you specify   or an empty string for this parameter, the method throws an exception.
- `zoneID`: The ID of the record zone where you want to store the record. This parameter must not be  .

## See Also

- [convenience init(recordName: String)](ckrecord/id/init(recordname:).md)
  Creates a new record ID with the specified name in the default zone.
- [let CKRecordNameZoneWideShare: String](ckrecordnamezonewideshare.md)
  The name of a share record that manages a shared record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/id/init(recordname:zoneid:))*