# CloudKit.Share

**Framework**: CloudKit JS  
**Kind**: struct

Represents a shared record.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.Share {
	String recordType;
	CloudKit.ShareParticipantPermission publicPermission;
	CloudKit.ShareParticipant[] participants;
};
```

## Topics

### Instance Properties
- [participants](cloudkit.share/participants.md)
  Users who accepted this shared record.
- [publicPermission](cloudkit.share/publicpermission.md)
  Th public’s read and write permissions.
- [recordType](cloudkit.share/recordtype.md)
  The type of record.

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
- [CloudKit.ShareParticipant](cloudkit.shareparticipant.md)
  Represents a user who accepted a shared record.
- [CloudKit.SharingUIResult](cloudkit.sharinguiresult.md)
  Represents the results of sharing a record with other users.
- [CloudKit.Subscription](cloudkit.subscription.md)
  A subscription, which is a persistent query on the server that tracks the creation, deletion, and modification of records.
- [CloudKit.UserIdentity](cloudkit.useridentity.md)
  Information to identify a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.share)*