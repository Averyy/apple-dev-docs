# CloudKit.Record

**Framework**: CloudKit JS  
**Kind**: struct

A record in the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.Record {
	Object created;
	Object modified;
	String recordType;
	String recordName;
	String recordChangeTag;
	Boolean deleted;
	Boolean createShortGUID;
	String shortGUID;
	CKReference parent;
	CKReference share;
	Object<string, CloudKit.RecordField> fields;
};
```

#### Overview

The `CloudKit.Record` dictionary is the same as the dictionary described in [`Modifying Records (records/modify)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ModifyRecords.html#//apple_ref/doc/uid/TP40015240-CH2) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Topics

### Instance Properties
- [createShortGUID](cloudkit.record/createshortguid.md)
  A Boolean value indicating whether to create a short GUID.
- [created](cloudkit.record/created.md)
  Information about when the record was created on the server. The properties of this object are: `timestamp` (`Number`), the time at which the record was created, and `user` (`String`), the ID of the user who created the record. This field is used by the [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) class. The value of this field is set by the server. Omit this key when saving a record.
- [deleted](cloudkit.record/deleted.md)
  A Boolean value indicating whether the record was deleted. `true` if the record was deleted; otherwise, `false`.
- [fields](cloudkit.record/fields.md)
  Names of the fields or field-value pairs.
- [modified](cloudkit.record/modified.md)
  Information about when the record was last modified. The properties of this object are: `timestamp` (`Number`), the time at which the record was created, and `user` (`String`), the ID of the user who modified the record. This field is used by the [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) class. This value of this field is set by the server. Omit this key when saving a record.
- [parent](cloudkit.record/parent.md)
  A reference to a parent object used for sharing.
- [recordChangeTag](cloudkit.record/recordchangetag.md)
  A string containing the server change token for the record. Use this tag to indicate which version of the record you last fetched. This key is required if you are saving an existing record.
- [recordName](cloudkit.record/recordname.md)
  The unique name used to identify the record. The default value is a random UUID.
- [recordType](cloudkit.record/recordtype.md)
  The name of the record type. This key is required if the record doesn’t exist.
- [share](cloudkit.record/share.md)
  A reference to the shared object for this record.
- [shortGUID](cloudkit.record/shortguid.md)
  A global unique identifier for this record used for sharing.

## See Also

- [CloudKit.CloudKitConfig](cloudkit.cloudkitconfig.md)
  Dictionary used to configure the CloudKit environment.
- [CloudKit.ContainerConfig](cloudkit.containerconfig.md)
  A configuration for a container.
- [CloudKit.NameComponents](cloudkit.namecomponents.md)
  The parts of the user’s name.
- [CloudKit.NotificationInfo](cloudkit.notificationinfo.md)
  Information about a notification.
- [CloudKit.Query](cloudkit.query.md)
  Search parameters to use when fetching records from the database.
- [CloudKit.RecordField](cloudkit.recordfield.md)
  A field value of a record.
- [CloudKit.RecordInfo](cloudkit.recordinfo.md)
  Encapsulates the results of fetching information about a record.
- [CloudKit.RecordZone](cloudkit.recordzone.md)
  Represents a record zone.
- [CloudKit.RecordZoneChanges](cloudkit.recordzonechanges.md)
  Represents the changes in a record zone.
- [CloudKit.RecordZoneChangesOptions](cloudkit.recordzonechangesoptions.md)
  Options about fetching changes in a record zone.
- [CloudKit.Share](cloudkit.share.md)
  Represents a shared record.
- [CloudKit.ShareParticipant](cloudkit.shareparticipant.md)
  Represents a user who accepted a shared record.
- [CloudKit.SharingUIResult](cloudkit.sharinguiresult.md)
  Represents the results of sharing a record with other users.
- [CloudKit.Subscription](cloudkit.subscription.md)
  A subscription, which is a persistent query on the server that tracks the creation, deletion, and modification of records.
- [CloudKit.UserIdentity](cloudkit.useridentity.md)
  Information to identify a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.record)*