# CKRecord

**Framework**: Cloudkit  
**Kind**: class

A collection of key-value pairs that store your app’s data.

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
class CKRecord
```

## Mentions

- [Designing and Creating a CloudKit Database](designing-and-creating-a-cloudkit-database.md)
- [Encrypting User Data](encrypting-user-data.md)

#### Overview

Records are the fundamental objects that manage data in CloudKit. You can define any number of record types for your app, with each record type corresponding to a different type of information. Within a record type, you then define one or more fields, each with a name and a value. Records can contain simple data types, such as strings and numbers, or more complex types, such as geographic locations or pointers to other records.

An important step in using CloudKit is defining the record types your app supports. A new record object doesn’t contain any keys or values. During development, you can add new keys and values at any time. The first time you set a value for a key and save the record, the server associates that type with the key for all records of the same type. The `CKRecord` class doesn’t impose these type constraints or do any local validation of a record’s contents. CloudKit enforces these constraints when you save the records.

> **Note**:  The ability to add new keys is only possible during development. When you deploy to a production environment, the server returns an error if you try to specify an unknown record type or try to save a record that contains unknown keys.

Although records behave like dictionaries, there are limitations to the types of values you can assign to keys. The following are the object types that the `CKRecord` class supports. Attempting to specify objects of any other type results in failure. Fields of all types are searchable unless otherwise noted.

##### Supported Data Types

`CKRecord` fields support the following data types:

> ❗ **Important**:  To ensure the speed of fetching and saving records, the data that a record stores must not exceed 1 MB. Assets don’t count toward this limit, but all other data types do.

##### Defining Records

The process for defining your record types depends entirely on your app and the data you’re trying to represent. It’s best to design records that encapsulate data for one unit of information. For example, you might use one record type to store an employee’s name, job title, and date of hire, and use a separate record type to store the employee’s address information. Using different record types lets you manage, manipulate, and validate the two types of information separately.

Use fields that contain [`CKRecord.Reference`](ckrecord/reference.md) objects to establish relationships between different types of records. After you define your record types, use the iCloud Dashboard to set them up. During development, you can also create new record types programmatically.

##### Indexing the Fields of a Record

Indexes make it possible to search the contents of your records efficiently. During development, the server indexes all fields with data types it can use in the predicate of a query. This automatic indexing makes it easier to experiment with queries during development, but the indexes require space in a database and require time to generate and maintain.

To manage the indexing behavior of your records in the production environment, use CloudKit Dashboard. When migrating your schema from the development environment to the production environment, enable indexing only for the fields that your app uses in queries, and disable it for all other fields.

##### Customizing Records

Use this class as-is to manage data coming from or going to the server, and don’t subclass it.

##### Storing Records Locally

If you store records in a local database, use the [`encodeSystemFields(with:)`](ckrecord/encodesystemfields(with:).md) method to encode and store the record’s metadata. The metadata contains the record ID and the change tag, which you need later to sync records in a local database with those in CloudKit.

## Topics

### Creating a Record
- [convenience init(recordType: CKRecord.RecordType, recordID: CKRecord.ID)](ckrecord/init(recordtype:recordid:).md)
  Creates a record using an ID that you provide.
- [typealias RecordType](ckrecord/recordtype-swift.typealias.md)
  The data type that CloudKit requires for record types.
- [typealias FieldKey](ckrecord/fieldkey.md)
  The data type that CloudKit requires for record field names.
- [convenience init(recordType: CKRecord.RecordType, zoneID: CKRecordZone.ID)](ckrecord/init(recordtype:zoneid:).md)
  Creates a record in the specified zone.
### Accessing the Record’s Fields
- [func object(forKey: CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](ckrecord/object(forkey:).md)
  Returns the object that the record stores for the specified key.
- [subscript(String) -> (any __CKRecordObjCValue)?](ckrecord/subscript(_:)-51whk.md)
  Returns the object that the record stores for the specified key.
- [subscript(CKRecord.FieldKey) -> (any __CKRecordObjCValue)?](ckrecord/subscript(_:)-4g91i.md)
  Returns the object that the record stores for the specified key.
- [func setObject((any __CKRecordObjCValue)?, forKey: CKRecord.FieldKey)](ckrecord/setobject(_:forkey:).md)
  Stores an object in the record using the specified key.
- [func allKeys() -> [CKRecord.FieldKey]](ckrecord/allkeys.md)
  Returns an array of the record’s keys.
- [func changedKeys() -> [CKRecord.FieldKey]](ckrecord/changedkeys.md)
  Returns an array of keys with recent changes to their values.
- [struct CKRecordKeyValueIterator](ckrecordkeyvalueiterator.md)
  An iterator of the record’s key-value pairs.
- [protocol CKRecordValueProtocol](ckrecordvalueprotocol.md)
  A description of a CloudKit record value.
- [protocol CKRecordKeyValueSetting](ckrecordkeyvaluesetting.md)
  A protocol for managing the key-value pairs of a CloudKit record.
- [typealias CKRecordValue](ckrecordvalue-swift.typealias.md)
  A data type for objects that CloudKit stores on the server.
### Accessing the Record’s Metadata
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
- [CKRecord.ID](ckrecord/id.md)
  An object that uniquely identifies a record in a database.
### Encrypting the Record’s Values
- [var encryptedValues: any CKRecordKeyValueSetting & Sendable](ckrecord/encryptedvalues.md)
  An object that manages the record’s encrypted key-value pairs.
### Getting Data for Full-Text Searches
- [func allTokens() -> [String]](ckrecord/alltokens.md)
  Returns an array of strings to use for full-text searches of the field’s string-based values.
### Encoding the Record’s Metadata
- [func encodeSystemFields(with: NSCoder)](ckrecord/encodesystemfields(with:).md)
  Encodes the record’s system fields using the specified archiver.
### Sharing Records
- [var parent: CKRecord.Reference?](ckrecord/parent.md)
  A reference to the record’s parent record.
- [var share: CKRecord.Reference?](ckrecord/share.md)
  A reference to the share object that determines the share status of the record.
- [CKRecord.Reference](ckrecord/reference.md)
  A relationship between two records in a record zone.
- [func setParent(CKRecord?)](ckrecord/setparent(_:)-23du1.md)
  Creates and sets a reference object for a parent from its record.
- [func setParent(CKRecord.ID?)](ckrecord/setparent(_:)-7egcx.md)
  Creates and sets a reference object for a parent from the parent’s record ID.
- [CKRecord.SystemFieldKey](ckrecord/systemfieldkey.md)
  Possible values for types of system field keys on records.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CKShare](ckshare.md)
### Conforms To
- [CKRecordKeyValueSetting](ckrecordkeyvaluesetting.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [Designing and Creating a CloudKit Database](designing-and-creating-a-cloudkit-database.md)
  Create a schema to store your app’s objects as records in iCloud using CloudKit.
- [Managing iCloud Containers with CloudKit Database App](managing-icloud-containers-with-cloudkit-database-app.md)
  Inspect and modify the schema and data for your app’s iCloud container.
- [class CKRecordZone](ckrecordzone.md)
  A database partition that contains related records.
- [CKRecord.Reference](ckrecord/reference.md)
  A relationship between two records in a record zone.
- [class CKAsset](ckasset.md)
  An external file that belongs to a record.
- [Integrating a Text-Based Schema into Your Workflow](integrating-a-text-based-schema-into-your-workflow.md)
  Define and update your schema with the CloudKit Schema Language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CloudKit/ckrecord)*