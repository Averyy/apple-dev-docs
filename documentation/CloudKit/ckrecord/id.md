# CKRecord.ID

**Framework**: CloudKit  
**Kind**: class

An object that uniquely identifies a record in a database.

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
class ID
```

#### Overview

A record ID object consists of a name string and a zone ID. The name string is an ASCII string that doesn’t exceed 255 characters in length. For automatically created records, the ID name string derives from a UUID and is, therefore, unique. When creating your own record ID objects, you can use names that have more meaning to your app or to the user, as long as each name is unique within the specified zone. For example, you might use a document name for the name string.

Record IDs must be unique within the specified database, but you can reuse record IDs in different databases. Each container has a public and a private database, and the private database is different for each unique user. This configuration provides for the reusing of record IDs in each user’s private database, but ensures that only one record uses a specific record ID in the public database.

CloudKit generally creates record IDs when it first saves a new record, but you might manually instantiate instances of `CKRecordID` in  specific situations. For example, you must create an instance when saving a record in a zone other than the default zone. You also instantiate instances of `CKRecordID` when retrieving specific records from a database.

Don’t subclass `CKRecordID`.

##### Interacting with Record Ids

After you create a `CKRecordID` object, interactions with that object typically involve creating a new record or retrieving an existing record from a database.

You might also use record IDs when you can’t use a [`CKRecord.Reference`](ckrecord/reference.md) object to refer to a record. References are only valid within a single zone of a database. To refer to objects outside of the current zone or database, save the strings in the record’s `CKRecordID` and [`CKRecordZone.ID`](ckrecordzone/id.md) objects. When you want to retrieve the record later, use those strings to recreate the record and zone ID objects so that you can fetch the record.

###### Creating Record Ids for New Records

To assign a custom record ID to a new record, you must create the `CKRecordID` object first. You need to know the intended name and zone information for that record, which might also require creating a [`CKRecordZone.ID`](ckrecordzone/id.md) object. After creating the record ID object, initialize your new record using its [`initWithRecordType:recordID:`](ckrecord/initwithrecordtype:recordid:.md) method.

###### Using Record Ids to Fetch Records

Use a record ID to fetch the corresponding [`CKRecord`](ckrecord.md) object from a database quickly. You perform the fetch operation using a [`CKFetchRecordsOperation`](ckfetchrecordsoperation.md) object or the [`fetch(withRecordID:completionHandler:)`](ckdatabase/fetch(withrecordid:completionhandler:).md) method of the [`CKDatabase`](ckdatabase.md) class. In both cases, CloudKit returns the record asynchronously using the handler you provide.

## Topics

### Creating a Record ID
- [convenience init(recordName: String)](ckrecord/id/init(recordname:).md)
  Creates a new record ID with the specified name in the default zone.
- [convenience init(recordName: String, zoneID: CKRecordZone.ID)](ckrecord/id/init(recordname:zoneid:).md)
  Creates a new record ID with the specified name and zone information.
- [let CKRecordNameZoneWideShare: String](ckrecordnamezonewideshare.md)
  The name of a share record that manages a shared record zone.
### Getting the Record ID’s Name
- [var recordName: String](ckrecord/id/recordname.md)
  The unique name of the record.
### Getting the Record ID’s Zone
- [var zoneID: CKRecordZone.ID](ckrecord/id/zoneid.md)
  The ID of the zone that contains the record.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var recordID: CKRecord.ID](ckrecord/recordid.md)
  The unique ID of the record.
- [var recordType: CKRecord.RecordType](ckrecord/recordtype-6v7au.md)
  The value that your app defines to identify the type of record.
- [CKRecord.SystemType](ckrecord/systemtype.md)
  Possible values for record types of system records.
- [var creationDate: Date?](ckrecord/creationdate.md)
  The time when CloudKit first saves the record to the server.
- [var creatorUserRecordID: CKRecord.ID?](ckrecord/creatoruserrecordid.md)
  The ID of the user who creates the record.
- [var modificationDate: Date?](ckrecord/modificationdate.md)
  The most recent time that CloudKit saved the record to the server.
- [var lastModifiedUserRecordID: CKRecord.ID?](ckrecord/lastmodifieduserrecordid.md)
  The ID of the user who most recently modified the record.
- [var recordChangeTag: String?](ckrecord/recordchangetag.md)
  The server change token for the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/id)*