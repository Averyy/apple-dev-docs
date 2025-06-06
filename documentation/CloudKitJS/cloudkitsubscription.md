# CloudKit.Subscription

**Framework**: CloudKit JS  
**Kind**: struct

A subscription, which is a persistent query on the server that tracks the creation, deletion, and modification of records.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.Subscription {
	String subscriptionType;
	String subscriptionID;
	CloudKit.ZoneID zoneID;
	CloudKit.NotificationInfo notificationInfo;
	Boolean zoneWide;
	String[] firesOn;
	Boolean firesOnce;
	Query query;
};
```

#### Overview

The `CloudKit.Subscription` dictionary is the same as the dictionary described in [`Subscription Dictionary`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/Types.html#//apple_ref/doc/uid/TP40015240-CH3-SW12) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Topics

### Instance Properties
- [firesOn](cloudkit.subscription/fireson.md)
  An array of keywords that specify the actions that should trigger push notifications. Possible values in the array are: `"create"`, `"update"`, and `"delete"`. This key is not used if `query` is null.
- [firesOnce](cloudkit.subscription/firesonce.md)
  A Boolean value indicating whether push notifications should be triggered once. If `true`, push notifications are sent once. If `false`, they can be sent multiple times. The default value is `false`.
- [notificationInfo](cloudkit.subscription/notificationinfo.md)
  A dictionary containing information about how the system should alert the user.
- [query](cloudkit.subscription/query.md)
  The matching criteria to apply to records.
- [subscriptionID](cloudkit.subscription/subscriptionid.md)
  A unique identifier for the subscription.
- [subscriptionType](cloudkit.subscription/subscriptiontype.md)
  The type of subscription. Possible values are: `"zone"`, and `"query”`. This key is required.
- [zoneID](cloudkit.subscription/zoneid.md)
  Dictionary that identifies a record zone to monitor in the database.
- [zoneWide](cloudkit.subscription/zonewide.md)
  A Boolean value determining whether all zones should be searched. If `true`, all zones are searched. If `false`, the default zone is searched.

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
- [CloudKit.UserIdentity](cloudkit.useridentity.md)
  Information to identify a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.subscription)*