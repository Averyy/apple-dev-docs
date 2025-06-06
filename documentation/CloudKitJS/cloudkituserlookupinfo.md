# CloudKit.UserLookupInfo

**Framework**: CloudKit JS  
**Kind**: struct

Information that can be used to fetch a user.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.UserLookupInfo {
	String userRecordName;
	String emailAddress;
	String phoneNumber;
};
```

## Topics

### Instance Properties
- [emailAddress](cloudkit.userlookupinfo/emailaddress.md)
  The user’s email address.
- [phoneNumber](cloudkit.userlookupinfo/phonenumber.md)
  The user’s phone number.
- [userRecordName](cloudkit.userlookupinfo/userrecordname.md)
  The name of the user record.

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
- [CloudKit.Share](cloudkit.share.md)
  Represents a shared record.
- [CloudKit.ShareParticipant](cloudkit.shareparticipant.md)
  Represents a user who accepted a shared record.
- [CloudKit.SharingUIResult](cloudkit.sharinguiresult.md)
  Represents the results of sharing a record with other users.
- [CloudKit.Subscription](cloudkit.subscription.md)
  A subscription, which is a persistent query on the server that tracks the creation, deletion, and modification of records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.userlookupinfo)*