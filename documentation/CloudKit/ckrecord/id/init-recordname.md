# init(recordName:)

**Framework**: CloudKit  
**Kind**: init

Creates a new record ID with the specified name in the default zone.

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
convenience init(recordName: String)
```

#### Return Value

An initialized record ID object, or `nil` if CloudKit can’t create the object.

#### Discussion

Use this method when you’re creating or searching for records in the default zone.

## Parameters

- `recordName`: The name that identifies the record. The string must contain only ASCII characters, must not exceed 255 characters, and must not start with an underscore. If you specify   or an empty string for this parameter, the method throws an exception.

## See Also

- [convenience init(recordName: String, zoneID: CKRecordZone.ID)](ckrecord/id/init(recordname:zoneid:).md)
  Creates a new record ID with the specified name and zone information.
- [let CKRecordNameZoneWideShare: String](ckrecordnamezonewideshare.md)
  The name of a share record that manages a shared record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/id/init(recordname:))*