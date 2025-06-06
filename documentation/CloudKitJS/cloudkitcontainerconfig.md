# CloudKit.ContainerConfig

**Framework**: CloudKit JS  
**Kind**: struct

A configuration for a container.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
dictionary CloudKit.ContainerConfig {
	String containerIdentifier;
	String environment;
	String apnsEnvironment;
	Object apiTokenAuth;
	Object serverToServerKeyAuth;
};
```

#### Overview

This table describes `apiTokenAuth` properties.

| Property | Description |
| --- | --- |
| `apiToken` | The API token generated and obtained using CloudKit Dashboard. To create an API token, read [`Accessing CloudKit Using an API Token`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW2) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240). |
| `persist` | Boolean value indicating whether the CloudKit session token persists. The default value is `false`. |
| `signInButton` | The sign-in button to display to the user. The properties are: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) id: The DOM element ID. The default value is `apple-sign-in-button`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) theme: The button theme. The default value is `medium`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If `null`, uses the default property values. |
| `signOutButton` | The sign-out button to display to the user. The properties are: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) id: The DOM element ID. The default value is `apple-sign-out-button`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) theme: The button theme. The default value is `medium`. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) If `null`, uses the default property values. |

This table describes `serverToServerKeyAuth` properties.

| Property | Description |
| --- | --- |
| `keyID` | A unique identifier for the key generated using CloudKit Dashboard. To create this key, read [`Accessing CloudKit Using a Server-to-Server Key`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW6) in [`CloudKit Web Services Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240). |
| `privateKeyFile` | The path to the PEM encoded key file. |
| `privateKeyPassPhrase` | The pass phrase for the key. |

## Topics

### Instance Properties
- [apiTokenAuth](cloudkit.containerconfig/apitokenauth.md)
  The API token and other authentication properties, described in the Discussion section. Either this key or the `serverToServerKeyAuth` key is required. If you include this key, don’t include the `serverToServerKeyAuth` key.
- [apnsEnvironment](cloudkit.containerconfig/apnsenvironment.md)
  The Apple Push Notification service (APNs) environment associated with this container. Possible values are [`CloudKit`](cloudkit.md).[`DEVELOPMENT_ENVIRONMENT`](cloudkit/development_environment.md) and [`CloudKit`](cloudkit.md).[`PRODUCTION_ENVIRONMENT`](cloudkit/production_environment.md).
- [containerIdentifier](cloudkit.containerconfig/containeridentifier.md)
  The string that identifies the app’s container. This key is required.
- [environment](cloudkit.containerconfig/environment.md)
  The version of the app’s container. Possible values are [`CloudKit`](cloudkit.md).[`DEVELOPMENT_ENVIRONMENT`](cloudkit/development_environment.md) and [`CloudKit`](cloudkit.md).[`PRODUCTION_ENVIRONMENT`](cloudkit/production_environment.md).
- [serverToServerKeyAuth](cloudkit.containerconfig/servertoserverkeyauth.md)
  The server-to-server authentication key and related properties, described in the Discussion section. Either this key or the `apiTokenAuth` key is required. If you include this key, don’t include the `apiTokenAuth` key.

## See Also

- [CloudKit.CloudKitConfig](cloudkit.cloudkitconfig.md)
  Dictionary used to configure the CloudKit environment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.containerconfig)*