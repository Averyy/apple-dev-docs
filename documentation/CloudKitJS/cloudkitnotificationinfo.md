# CloudKit.NotificationInfo

**Framework**: CloudKit JS  
**Kind**: struct

Information about a notification.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.NotificationInfo {
	String alertBody;
	String alertLocalizationKey;
	String[] alertLocalizationArgs;
	String alertActionLocalizationKey;
	String alertLaunchImage;
	String soundName;
	Boolean shouldBadge;
	Boolean shouldSendContentAvailable;
	String[] additionalFields;
	String category;
};
```

#### Overview

The `CloudKit.NotificationInfo` dictionary is the same as the dictionary described in [`Notification Info Dictionary`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/Types.html#//apple_ref/doc/uid/TP40015240-CH3-SW13) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240).

## Topics

### Instance Properties
- [additionalFields](cloudkit.notificationinfo/additionalfields.md)
  Fields the server sends along with this notification.
- [alertActionLocalizationKey](cloudkit.notificationinfo/alertactionlocalizationkey.md)
  A key to get a localized right button title that appears in the alert dialog.
- [alertBody](cloudkit.notificationinfo/alertbody.md)
  The text of the alert message.
- [alertLaunchImage](cloudkit.notificationinfo/alertlaunchimage.md)
  The filename of an image file in the app bundle used as a launch image.
- [alertLocalizationArgs](cloudkit.notificationinfo/alertlocalizationargs.md)
  Array of strings to appear as variables if `alertLocalizationKey` is a format specifier.
- [alertLocalizationKey](cloudkit.notificationinfo/alertlocalizationkey.md)
  A key to a localized alert-message.
- [category](cloudkit.notificationinfo/category.md)
  The name of the action group corresponding to this notification.
- [shouldBadge](cloudkit.notificationinfo/shouldbadge.md)
  A Boolean value indicating whether a badge should be displayed. If `true`, a badge is displayed; otherwise, it is not. The default value is `false`.
- [shouldSendContentAvailable](cloudkit.notificationinfo/shouldsendcontentavailable.md)
  A Boolean value indicating whether new content is available. If `true`, new content is available; otherwise, it is not. The default value is `false`.
- [soundName](cloudkit.notificationinfo/soundname.md)
  The name of a sound file in the app bundle to play as an alert.

## See Also

- [CloudKit.CloudKitConfig](cloudkit.cloudkitconfig.md)
  Dictionary used to configure the CloudKit environment.
- [CloudKit.ContainerConfig](cloudkit.containerconfig.md)
  A configuration for a container.
- [CloudKit.NameComponents](cloudkit.namecomponents.md)
  The parts of the user’s name.
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
- [CloudKit.UserIdentity](cloudkit.useridentity.md)
  Information to identify a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.notificationinfo)*