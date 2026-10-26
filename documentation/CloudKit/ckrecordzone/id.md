# CKRecordZone.ID

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that uniquely identifies a record zone in a database.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class ID
```

```objc
@interface CKRecordZoneID : NSObject
```

#### Overview

Zones are a mechanism for grouping related records together. You create zone ID objects when you want to fetch an existing zone object or create a new zone with a specific name.

A record zone ID distinguishes one zone from another by a name string and the ID of the user who creates the zone. You should specify ASCII strings that don’t exceed 255 characters. When creating your own record zone ID objects, you can use names that have more meaning to your app or to the user, providing each zone name is unique within the specified database. You should set the owner name to the current user name or the name of another user. Get the current user name from [`CKCurrentUserDefaultName`](../ckcurrentuserdefaultname.md) or by calling [`fetchUserRecordID(completionHandler:)`](../ckcontainer/fetchuserrecordid%28completionhandler%29.md).

When creating new record zones, make the name string in the record zone ID unique in the target database. Public databases don’t support custom zones, and only the user who owns the database can create zones in private databases.

Don’t create subclasses of this class.

##### Interacting with Record Zone IDs

After you create a record zone ID, interactions with it typically include:

- Creating a [`CKRecord.ID`](../ckrecord/id.md) object so that you can fetch or create records in that zone.
- Retrieving an existing [`CKRecordZone`](../ckrecordzone.md) object from the database.

You don’t need to create a record zone ID to create a record zone. The [`CKRecordZone`](../ckrecordzone.md) class has initialization methods that create a record zone ID using the name string you provide.

###### Creating Record Zone IDs for Records

To create a new record in a custom zone, create a record zone ID that specifies the zone name. Use the record zone ID to create a [`CKRecord.ID`](../ckrecord/id.md), and then use the record ID to create the record.

###### Fetching a Record Zone Object from the Database

To fetch a record zone from the database, use a [`CKFetchRecordZonesOperation`](../ckfetchrecordzonesoperation.md) object or the [`fetch(withRecordZoneID:completionHandler:)`](../ckdatabase/fetch%28withrecordzoneid,completionhandler%29.md) method of [`CKDatabase`](../ckdatabase.md). Both techniques accept a record zone ID that you provide and retrieve the corresponding record zone object asynchronously. If you use the operation object, you can retrieve multiple record zones at the same time.

## Topics

### Creating a Record Zone ID
- [convenience init(zoneName: String, ownerName: String)](./id/init%28zonename,ownername%29-22irr.md)
  Creates a record zone ID with the specified name and owner.
- [- initWithZoneName:ownerName:](../ckrecordzoneid/initwithzonename_ownername_.md)
  Creates a record zone ID with the specified name and owner.
### Getting the Record Zone ID Attributes
- [var zoneName: String](./id/zonename.md)
  The unique name of the record zone.
- [var ownerName: String](./id/ownername.md)
  The ID of the user who owns the record zone.
### Accessing the Default Zone
- [static let `default`: CKRecordZone.ID](./id/default.md)
  The default zone ID.
- [static let defaultZoneName: String](./id/defaultzonename.md)
  The name of the default zone.
### Initializers
- [init?(coder: NSCoder)](./id/init%28coder%29.md)
- [convenience init(zoneName: String, ownerName: String?)](./id/init%28zonename,ownername%29-2hzo4.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Record Zone
- [init(zoneName: String)](./init%28zonename%29.md)
  Creates a record zone object with the specified zone name.
- [init(zoneID: CKRecordZone.ID)](./init%28zoneid%29.md)
  Creates a record zone object with the specified zone ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/id)*