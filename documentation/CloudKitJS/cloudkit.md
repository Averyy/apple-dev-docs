# CloudKit

**Framework**: CloudKit JS  
**Kind**: class

Use the `CloudKit` namespace to configure CloudKit JS, and to access app containers and global constants.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
interface CloudKit
```

#### Overview

Set up CloudKit JS by passing container and authentication information to the [`configure`](cloudkit/configure.md) method. Also, specify whether to use the development or production environment. You’ll need the container ID and API token to configure CloudKit JS. (Use CloudKit Dashboard to create an API token, as described in [`Accessing CloudKit Using an API Token`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW2).) Some operations require users to enter their Apple ID credentials. Apple presents the sign-in dialog, but you can customize the position and theme of the sign-in and sign-out buttons.

After configuring CloudKit JS, use the container methods to get the app’s container objects ([`CloudKit.Container`](cloudkit.container.md)), and from the container objects, get the database objects ([`CloudKit.Database`](cloudkit.database.md)).

## Topics

### Configuring CloudKit JS
- [configure](cloudkit/configure.md)
  Configures CloudKit JS.
### Accessing Containers
- [getDefaultContainer](cloudkit/getdefaultcontainer.md)
  Returns the default container.
- [getContainer](cloudkit/getcontainer.md)
  Returns the container with the specified container ID.
- [getAllContainers](cloudkit/getallcontainers.md)
  Returns all the containers that were configured.
### Constants
- [CloudKit Build Version and Status](cloudkit-build-version-and-status.md)
  Constants describing the environment that stores the containers.
- [Environments](environments.md)
  Constants to use when configuring the environment of containers.
### Enumerations
- [CloudKit.AppleIDButtonTheme](cloudkit.appleidbuttontheme.md)
  Specifies the look of the Apple ID button.
- [CloudKit.DatabaseScope](cloudkit.databasescope.md)
  Available database scopes.
- [CloudKit.QueryFilterComparator](cloudkit.queryfiltercomparator.md)
  The comparators you use to create queries.
- [CloudKit.ReferenceAction](cloudkit.referenceaction.md)
  The delete action for a reference object.
- [CloudKit.ShareParticipantAcceptanceStatus](cloudkit.shareparticipantacceptancestatus.md)
  The status of a participant accepting a share invitation.
- [CloudKit.ShareParticipantPermission](cloudkit.shareparticipantpermission.md)
  The status of a participant accepting a share invitation.
- [CloudKit.ShareParticipantType](cloudkit.shareparticipanttype.md)
  Determines whether a participant can modify the list of participants of a shared record.
- [CloudKit.SubscriptionType](cloudkit.subscriptiontype.md)
  The type of subscription.
### Properties
- [CKError](cloudkit/ckerror.md)
  Property to access the error codes.
- [DatabaseScope](cloudkit/databasescope.md)
  Property to access the enumeration.
- [Promise](cloudkit/promise.md)
  Represents an operation that hasn’t completed yet, but is expected in the future.
- [QueryFilterComparator](cloudkit/queryfiltercomparator.md)
  Property to access the enumeration.
- [ReferenceAction](cloudkit/referenceaction.md)
  Property to access the enumeration.
- [ShareParticipantAcceptanceStatus](cloudkit/shareparticipantacceptancestatus.md)
  Property to access the enumeration.
- [ShareParticipantPermission](cloudkit/shareparticipantpermission.md)
  Property to access the enumeration.
- [ShareParticipantType](cloudkit/shareparticipanttype.md)
  Property to access the enumeration.
- [ShareRecordType](cloudkit/sharerecordtype.md)
  Property to access the class instance.
- [SubscriptionType](cloudkit/subscriptiontype.md)
  Property to access the enumeration.
### Classes
- [CloudKit.CKError](cloudkit.ckerror.md)
  A [`CloudKit.CKError`](cloudkit.ckerror.md) object encapsulates an error that may occur when you use CloudKit JS. This includes CloudKit server errors and local errors.
- [CloudKit.Container](cloudkit.container.md)
  A [`CloudKit.Container`](cloudkit.container.md) object provides access to an app container, and through the app container, access to its databases. It also contains methods for authenticating and fetching users.
- [CloudKit.Database](cloudkit.database.md)
  A [`CloudKit.Database`](cloudkit.database.md) object represents a public or private database in an app container.
- [CloudKit.DatabaseChangesResponse](cloudkit.databasechangesresponse.md)
  A [`CloudKit.DatabaseChangesResponse`](cloudkit.databasechangesresponse.md) object encapsulates the results of fetching changed record zones in a database.
- [CloudKit.Notification](cloudkit.notification.md)
  A [`CloudKit.Notification`](cloudkit.notification.md) object represents a push notification that was sent to your app. Notifications are triggered by subscriptions that you save to the database. To subscribe to record changes and handle push notifications, see the `saveSubscription` method in [`CloudKit.Database`](cloudkit.database.md).
- [CloudKit.QueryNotification](cloudkit.querynotification.md)
  A [`CloudKit.QueryNotification`](cloudkit.querynotification.md) object represents a push notification that was generated by a subscription object. A query notification is triggered by subscriptions where the `subscriptionType` key is `query`. Use a [`CloudKit.QueryNotification`](cloudkit.querynotification.md) object to get information about the record that changed. To create query subscriptions and handle push notifications, see the [`saveSubscriptions`](cloudkit.database/savesubscriptions.md) method in [`CloudKit.Database`](cloudkit.database.md).
- [CloudKit.QueryResponse](cloudkit.queryresponse.md)
  A [`CloudKit.QueryResponse`](cloudkit.queryresponse.md) object encapsulates the results of using a query to fetch records
- [CloudKit.RecordInfosResponse](cloudkit.recordinfosresponse.md)
  A [`CloudKit.RecordInfosResponse`](cloudkit.recordinfosresponse.md) object encapsulates the results of fetching information about records in general and shared records in particular.
- [CloudKit.RecordsBatchBuilder](cloudkit.recordsbatchbuilder.md)
  A [`CloudKit.RecordsBatchBuilder`](cloudkit.recordsbatchbuilder.md) object encapsulates the results of changes to multiple records in a single database operation.
- [CloudKit.RecordsResponse](cloudkit.recordsresponse.md)
  A [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) object encapsulates the results of fetching records.
- [CloudKit.RecordZoneChangesResponse](cloudkit.recordzonechangesresponse.md)
  The [`CloudKit.RecordZoneChangesResponse`](cloudkit.recordzonechangesresponse.md) object encapsulates the results of fetching changes to one or more record zones.
- [CloudKit.RecordZoneNotification](cloudkit.recordzonenotification.md)
  A [`CloudKit.RecordZoneNotification`](cloudkit.recordzonenotification.md) object represents a push notification that was caused by changes to the contents of a record zone. A zone notification is triggered by subscriptions where the `subscriptionType` key is `zone`. Use a [`CloudKit.RecordZoneNotification`](cloudkit.recordzonenotification.md) object to get information about the record that changed. To create zone subscriptions and handle push notifications, see the [`saveSubscriptions`](cloudkit.database/savesubscriptions.md) method in [`CloudKit.Database`](cloudkit.database.md).
- [CloudKit.RecordZonesResponse](cloudkit.recordzonesresponse.md)
  A [`CloudKit.RecordZonesResponse`](cloudkit.recordzonesresponse.md) object encapsulates the results of database operations on a record zone.
- [CloudKit.Response](cloudkit.response.md)
  The [`CloudKit.Response`](cloudkit.response.md) class is an abstract superclass for subclasses that encapsulate the response from server requests. Don’t create instances of this class. Instances of subclasses are returned by methods in the [`CloudKit.Container`](cloudkit.container.md) and [`CloudKit.Database`](cloudkit.database.md) classes. Most of these methods return a `Promise` object that resolves to a subclass of [`CloudKit.Response`](cloudkit.response.md) if the operation is successful.
- [CloudKit.ShareRecordType](cloudkit.sharerecordtype.md)
  Display information about the record type of a shared record.
- [CloudKit.SubscriptionsResponse](cloudkit.subscriptionsresponse.md)
  A [`CloudKit.SubscriptionsResponse`](cloudkit.subscriptionsresponse.md) object encapsulates the results of database operations on subscriptions.
- [CloudKit.UserIdentitiesResponse](cloudkit.useridentitiesresponse.md)
  A [`CloudKit.UserIdentitiesResponse`](cloudkit.useridentitiesresponse.md) object encapsulates the results of fetching user identities.
### Structures
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
- [CloudKit.UserIdentity](cloudkit.useridentity.md)
  Information to identify a user.
- [CloudKit.UserLookupInfo](cloudkit.userlookupinfo.md)
  Information that can be used to fetch a user.
- [CloudKit.ZoneID](cloudkit.zoneid.md)
  An identifier for a zone, which is an area in a database for organizing related records.

## See Also

- [CloudKit.CKError](cloudkit.ckerror.md)
  A [`CloudKit.CKError`](cloudkit.ckerror.md) object encapsulates an error that may occur when you use CloudKit JS. This includes CloudKit server errors and local errors.
- [CloudKit.Container](cloudkit.container.md)
  A [`CloudKit.Container`](cloudkit.container.md) object provides access to an app container, and through the app container, access to its databases. It also contains methods for authenticating and fetching users.
- [CloudKit.Database](cloudkit.database.md)
  A [`CloudKit.Database`](cloudkit.database.md) object represents a public or private database in an app container.
- [CloudKit.DatabaseChangesResponse](cloudkit.databasechangesresponse.md)
  A [`CloudKit.DatabaseChangesResponse`](cloudkit.databasechangesresponse.md) object encapsulates the results of fetching changed record zones in a database.
- [CloudKit.Notification](cloudkit.notification.md)
  A [`CloudKit.Notification`](cloudkit.notification.md) object represents a push notification that was sent to your app. Notifications are triggered by subscriptions that you save to the database. To subscribe to record changes and handle push notifications, see the `saveSubscription` method in [`CloudKit.Database`](cloudkit.database.md).
- [CloudKit.QueryNotification](cloudkit.querynotification.md)
  A [`CloudKit.QueryNotification`](cloudkit.querynotification.md) object represents a push notification that was generated by a subscription object. A query notification is triggered by subscriptions where the `subscriptionType` key is `query`. Use a [`CloudKit.QueryNotification`](cloudkit.querynotification.md) object to get information about the record that changed. To create query subscriptions and handle push notifications, see the [`saveSubscriptions`](cloudkit.database/savesubscriptions.md) method in [`CloudKit.Database`](cloudkit.database.md).
- [CloudKit.QueryResponse](cloudkit.queryresponse.md)
  A [`CloudKit.QueryResponse`](cloudkit.queryresponse.md) object encapsulates the results of using a query to fetch records
- [CloudKit.RecordInfosResponse](cloudkit.recordinfosresponse.md)
  A [`CloudKit.RecordInfosResponse`](cloudkit.recordinfosresponse.md) object encapsulates the results of fetching information about records in general and shared records in particular.
- [CloudKit.RecordsBatchBuilder](cloudkit.recordsbatchbuilder.md)
  A [`CloudKit.RecordsBatchBuilder`](cloudkit.recordsbatchbuilder.md) object encapsulates the results of changes to multiple records in a single database operation.
- [CloudKit.RecordsResponse](cloudkit.recordsresponse.md)
  A [`CloudKit.RecordsResponse`](cloudkit.recordsresponse.md) object encapsulates the results of fetching records.
- [CloudKit.RecordZoneChangesResponse](cloudkit.recordzonechangesresponse.md)
  The [`CloudKit.RecordZoneChangesResponse`](cloudkit.recordzonechangesresponse.md) object encapsulates the results of fetching changes to one or more record zones.
- [CloudKit.RecordZoneNotification](cloudkit.recordzonenotification.md)
  A [`CloudKit.RecordZoneNotification`](cloudkit.recordzonenotification.md) object represents a push notification that was caused by changes to the contents of a record zone. A zone notification is triggered by subscriptions where the `subscriptionType` key is `zone`. Use a [`CloudKit.RecordZoneNotification`](cloudkit.recordzonenotification.md) object to get information about the record that changed. To create zone subscriptions and handle push notifications, see the [`saveSubscriptions`](cloudkit.database/savesubscriptions.md) method in [`CloudKit.Database`](cloudkit.database.md).
- [CloudKit.RecordZonesResponse](cloudkit.recordzonesresponse.md)
  A [`CloudKit.RecordZonesResponse`](cloudkit.recordzonesresponse.md) object encapsulates the results of database operations on a record zone.
- [CloudKit.Response](cloudkit.response.md)
  The [`CloudKit.Response`](cloudkit.response.md) class is an abstract superclass for subclasses that encapsulate the response from server requests. Don’t create instances of this class. Instances of subclasses are returned by methods in the [`CloudKit.Container`](cloudkit.container.md) and [`CloudKit.Database`](cloudkit.database.md) classes. Most of these methods return a `Promise` object that resolves to a subclass of [`CloudKit.Response`](cloudkit.response.md) if the operation is successful.
- [CloudKit.ShareRecordType](cloudkit.sharerecordtype.md)
  Display information about the record type of a shared record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit)*