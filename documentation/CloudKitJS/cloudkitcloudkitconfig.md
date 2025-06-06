# CloudKit.CloudKitConfig

**Framework**: CloudKit JS  
**Kind**: struct

Dictionary used to configure the CloudKit environment.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.CloudKitConfig {
	CloudKit.ContainerConfig[] containers;
	Object services;
};
```

#### Overview

The table describes the `services` properties.

| Property | Description |
| --- | --- |
| `logger` | An object with methods `info`, `log`, `warn`, and `error`. You can set this to `window.console`. |
| `fetch` | A function compatible with `window.fetch`. |
| `Promise` | An object used for deferred and asynchronous computations. To learn more, go to [`Mozilla Developer Network: Promise`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). |
| `authTokenStore` | An object with these two methods: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `putToken(containerIdentifier:String, authToken:String) -> void;` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `getToken(containerIdentifier:String) -> String;` |

## Topics

### Instance Properties
- [containers](cloudkit.cloudkitconfig/containers.md)
  An array of dictionaries used to configure each container of type [`CloudKit.ContainerConfig`](cloudkit.containerconfig.md).
- [services](cloudkit.cloudkitconfig/services.md)
  Encapsulates information about services, described in the Discussion section.

## See Also

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
- [CloudKit.UserIdentity](cloudkit.useridentity.md)
  Information to identify a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.cloudkitconfig)*