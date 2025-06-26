# CKRecord.Reference

**Framework**: CloudKit  
**Kind**: class

A relationship between two records in a record zone.

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
class Reference
```

## Mentions

- [Encrypting User Data](encrypting-user-data.md)
- [Designing and Creating a CloudKit Database](designing-and-creating-a-cloudkit-database.md)

#### Overview

A `CKReference` object creates a many-to-one relationship between records in your database. Each reference object stores information about the one record that is the target of the reference. You then save the reference object in the fields of one or more records to create a link from those records to the target. Both records must be in the same zone of the same database.

References create a stronger relationship between records than just saving the ID of a record as a string. Specifically, you can use references to create an ownership model between two records. When the reference object’s action is [`CKRecord.ReferenceAction.deleteSelf`](ckrecord/referenceaction/deleteself.md), the target of the reference—that is, the record in the reference’s [`recordID`](ckrecord/reference/recordid.md) property—becomes the owner of the source record. Deleting the target (owner) record deletes all its source records. The deletion of any owned records can trigger further deletions if those records are the owners of other records. If a record contains two or more `CKReference` objects with an action of [`CKRecord.ReferenceAction.deleteSelf`](ckrecord/referenceaction/deleteself.md), CloudKit deletes the record when it deletes any of the objects it references.

> **Note**:  It is permissible to create circular owning references for a set of records.

To save multiple records that contain references between them, save the target records first or save all the records in one batch operation using [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md).

##### Interacting with Reference Objects

You use reference objects to create strong links between two records and to search for related fields. When you create new records, you create reference objects and assign them to fields of your records. The only other time you create reference objects is when you build a search predicate to search for related records.

###### Linking to Another Record

To link records together and create a strong relationship between them, create a new `CKReference` object, initialize it with the owner record, and assign that reference object to a field of the owned record. When you design the relationships among your own records, make the owner the more important of two related records. The owner record rarely depends on any records that point to it. The owner record is also the one that you typically fetch first from the database.

> ❗ **Important**:  There is a hard limit to the number of references with a [`CKRecord.ReferenceAction.deleteSelf`](ckrecord/referenceaction/deleteself.md) action that any one record can have. This limit is 750 references, and any attempt to exceed it results in an error from the server.

The figure below shows an example of a relationship between a to-do list record and a set of item records that represent individual items to complete. The to-do list is the primary record, or owner, in the relationship because it represents the entire to-do list, including all items on the list. As a result, each item record has a field that contains a `CKReference` object that points to the owning to-do list record.

![A figure that shows the relationship between a parent record and its children.](https://docs-assets.developer.apple.com/published/251fe779254091b04fe03fb4c610471d/media-1965777%402x.png)

The following code sample shows how to create the reference object for each item record and configure it to point at the list record:

An ownership type of organization is useful even if one object doesn’t explicitly own another. Ownership helps establish the relationships between records and how you search for them in the database. Ownership doesn’t require the deletion of the owned records when you delete their owner record. You can prevent such deletions by specifying the [`CKRecord.ReferenceAction.none`](ckrecord/referenceaction/none.md) action when you create a `CKReference` object.

> **Note**:  When you’re creating a `CKReference` between two objects and you have both objects in memory, be sure to fetch the object on the receiving end of the relationship. This is due to the creation of the `CKReference` between the two objects altering the [`recordChangeTag`](ckrecord/recordchangetag.md) of the receiving object on the server.

###### Searching for Related Records

When you want to find records for a single owner object, you create a `CKReference` object and use it to build your search predicate. When you use reference objects in search predicates, the search code looks only at the ID value in the reference object. It matches the ID in records of the specified type with the ID you provide in the `CKReference` object.

The code sample below shows how to use a reference object to construct a query for the records in the figure above. The `listID` variable is a placeholder for the record ID of the list with the items you want to retrieve. The predicate tells the query object to search the `owningList` field of the target records and compare the reference object there with the one in the `recordToMatch` variable. Executing the query operation object returns the matching records asynchronously to the completion block you provide.

## Topics

### Creating a Reference
- [init(recordID: CKRecord.ID, action: CKRecord.ReferenceAction)](ckrecord/reference/init(recordid:action:).md)
  Creates a reference object that points to the record with the specified ID.
- [convenience init(record: CKRecord, action: CKRecord.ReferenceAction)](ckrecord/reference/init(record:action:).md)
  Creates a reference object that points to the specified record object.
- [CKRecord.Reference.Action](ckrecord/reference/action-swift.typealias.md)
  A type that represents additional actions that occur when deleting references.
### Getting the Reference Attributes
- [var action: CKRecord.ReferenceAction](ckrecord/reference/action-swift.property.md)
  The ownership behavior for the records.
- [var recordID: CKRecord.ID](ckrecord/reference/recordid.md)
  The ID of the referenced record.
- [CKRecord.ReferenceAction](ckrecord/referenceaction.md)
  Constants that indicate the behavior when deleting a referenced record.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CKRecordValueProtocol](ckrecordvalueprotocol.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Designing and Creating a CloudKit Database](designing-and-creating-a-cloudkit-database.md)
  Create a schema to store your app’s objects as records in iCloud using CloudKit.
- [Managing iCloud Containers with CloudKit Database App](managing-icloud-containers-with-cloudkit-database-app.md)
  Inspect and modify the schema and data for your app’s iCloud container.
- [class CKRecordZone](ckrecordzone.md)
  A database partition that contains related records.
- [class CKRecord](ckrecord.md)
  A collection of key-value pairs that store your app’s data.
- [class CKAsset](ckasset.md)
  An external file that belongs to a record.
- [Integrating a Text-Based Schema into Your Workflow](integrating-a-text-based-schema-into-your-workflow.md)
  Define and update your schema with the CloudKit Schema Language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/reference)*