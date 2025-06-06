# CloudKit.RecordZoneChangesOptions

**Framework**: CloudKit JS  
**Kind**: struct

Options about fetching changes in a record zone.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.RecordZoneChangesOptions {
	CloudKit.ZoneID zoneID;
	String[] desiredKeys;
	String[] desiredRecordTypes;
	String syncToken;
};
```

## Topics

### Instance Properties
- [desiredKeys](cloudkit.recordzonechangesoptions/desiredkeys.md)
  An array of record field names that limit the amount of data returned. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields.
- [desiredRecordTypes](cloudkit.recordzonechangesoptions/desiredrecordtypes.md)
- [syncToken](cloudkit.recordzonechangesoptions/synctoken.md)
  Identifies a point in the zone’s change history. The first time you get record changes, omit this key and if `moreComing` is `true` in the response, use the `syncToken` in the response in the next request until `moreComing` is `false`. Otherwise, get the current sync token by fetching a zone.
- [zoneID](cloudkit.recordzonechangesoptions/zoneid.md)
  The record zone identifier.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordzonechangesoptions)*