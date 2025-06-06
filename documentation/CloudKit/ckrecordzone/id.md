# CKRecordZone.ID

**Framework**: CloudKit  
**Kind**: class

An object that uniquely identifies a record zone in a database.

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

Zones are a mechanism for grouping related records together. You create zone ID objects when you want to fetch an existing zone object or create a new zone with a specific name.

A record zone ID distinguishes one zone from another by a name string and the ID of the user who creates the zone. Both strings must be ASCII strings that don’t exceed 255 characters. When creating your own record zone ID objects, you can use names that have more meaning to your app or to the user, providing each zone name is unique within the specified database. The owner name must be either the current user name or the name of another user. Get the current user name from [`CKCurrentUserDefaultName`](ckcurrentuserdefaultname.md) or by calling [`fetchUserRecordID(completionHandler:)`](ckcontainer/fetchuserrecordid(completionhandler:).md).

When creating new record zones, make the name string in the record zone ID unique in the target database. Public databases don’t support custom zones, and only the user who owns the database can create zones in private databases.

Don’t create subclasses of this class.

##### Interacting with Record Zone Ids

After you create a record zone ID, interactions with it typically include:

- Creating a [`CKRecord.ID`](ckrecord/id.md) object so that you can fetch or create records in that zone.
- Retrieving an existing [`CKRecordZone`](ckrecordzone.md) object from the database.

You don’t need to create a record zone ID to create a record zone. The [`CKRecordZone`](ckrecordzone.md) class has initialization methods that create a record zone ID using the name string you provide.

###### Creating Record Zone Ids for Records

To create a new record in a custom zone, create a record zone ID that specifies the zone name. Use the record zone ID to create a [`CKRecord.ID`](ckrecord/id.md), and then use the record ID to create the record.

###### Fetching a Record Zone Object From the Database

To fetch a record zone from the database, use a [`CKFetchRecordZonesOperation`](ckfetchrecordzonesoperation.md) object or the [`fetch(withRecordZoneID:completionHandler:)`](ckdatabase/fetch(withrecordzoneid:completionhandler:).md) method of [`CKDatabase`](ckdatabase.md). Both techniques accept a record zone ID that you provide and retrieve the corresponding record zone object asynchronously. If you use the operation object, you can retrieve multiple record zones at the same time.

## Topics

### Creating a Record Zone ID
- [convenience init(zoneName: String, ownerName: String)](ckrecordzone/id/init(zonename:ownername:)-22irr.md)
  Creates a record zone ID with the specified name and owner.
### Getting the Record Zone ID Attributes
- [var zoneName: String](ckrecordzone/id/zonename.md)
  The unique name of the record zone.
- [var ownerName: String](ckrecordzone/id/ownername.md)
  The ID of the user who owns the record zone.
### Accessing the Default Zone
- [static let `default`: CKRecordZone.ID](ckrecordzone/id/default.md)
  The default zone ID.
- [static let defaultZoneName: String](ckrecordzone/id/defaultzonename.md)
  The name of the default zone.
### Initializers
- [convenience init(zoneName: String, ownerName: String?)](ckrecordzone/id/init(zonename:ownername:)-2hzo4.md)

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

## See Also

- [init(zoneName: String)](ckrecordzone/init(zonename:).md)
  Creates a record zone object with the specified zone name.
- [init(zoneID: CKRecordZone.ID)](ckrecordzone/init(zoneid:).md)
  Creates a record zone object with the specified zone ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id)*