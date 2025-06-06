# CloudKit.Query

**Framework**: CloudKit JS  
**Kind**: struct

Search parameters to use when fetching records from the database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.Query {
	String recordType;
	Object[] filterBy;
	Object[] sortBy;
};
```

#### Overview

The `CloudKit.Query` dictionary is the same as the dictionary described in [`Fetching Records Using a Query (records/query)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/QueryingRecords.html#//apple_ref/doc/uid/TP40015240-CH5) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Topics

### Instance Properties
- [filterBy](cloudkit.query/filterby.md)
  An array of predicate dictionaries used to determine whether a record matches the query.
- [recordType](cloudkit.query/recordtype.md)
  The name of the record type. This key is required.
- [sortBy](cloudkit.query/sortby.md)
  An array of sort descriptor dictionaries that specify how to order the fetched records.

## See Also

- [CloudKit.CloudKitConfig](cloudkit.cloudkitconfig.md)
  Dictionary used to configure the CloudKit environment.
- [CloudKit.ContainerConfig](cloudkit.containerconfig.md)
  A configuration for a container.
- [CloudKit.NameComponents](cloudkit.namecomponents.md)
  The parts of the user’s name.
- [CloudKit.NotificationInfo](cloudkit.notificationinfo.md)
  Information about a notification.
- [CloudKit.Record](cloudkit.record.md)
  A record in the database.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.query)*