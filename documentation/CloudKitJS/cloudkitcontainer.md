# CloudKit.Container

**Framework**: CloudKit JS  
**Kind**: class

A [`CloudKit.Container`](cloudkit.container.md) object provides access to an app container, and through the app container, access to its databases. It also contains methods for authenticating and fetching users.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
interface CloudKit.Container
```

#### Overview

You do not create container objects yourself, nor should you subclass the [`CloudKit.Container`](cloudkit.container.md) class. You configure a container using the `CloudKit`.[`configure`](cloudkit/configure.md) method and obtain a container using one of the [`CloudKit`](cloudkit.md) namespace container methods.

The asynchronous methods in this class return a `Promise` object that resolves when the operation completes. For a description of the `Promise` class returned by these methods, go to [`Mozilla Developer Network: Promise`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

This class is similar to the [`CKContainer`](https://developer.apple.com/documentation/CloudKit/CKContainer) class in the CloudKit framework.

## Topics

### Getting the Public and Private Databases
- [publicCloudDatabase](cloudkit.container/publicclouddatabase.md)
  The database containing the data shared by all users.
- [privateCloudDatabase](cloudkit.container/privateclouddatabase.md)
  The database containing the user’s private data.
- [sharedCloudDatabase](cloudkit.container/sharedclouddatabase.md)
  The database containing shared records accepted by the current user.
- [getDatabaseWithDatabaseScope](cloudkit.container/getdatabasewithdatabasescope.md)
  Returns the specified (public, private, or shared) database.
### Getting the Identifier and Environment
- [containerIdentifier](cloudkit.container/containeridentifier.md)
  The string that identifies the app’s container.
- [environment](cloudkit.container/environment.md)
  The container environment, either development or production.
- [apnsEnvironment](cloudkit.container/apnsenvironment.md)
  The Apple Push Notification service (APNs) environment associated with this container.
### Authenticating Users
- [setUpAuth](cloudkit.container/setupauth.md)
  Determines whether a user is signed in and presents an appropriate sign in or sign out button.
- [whenUserSignsIn](cloudkit.container/whenusersignsin.md)
  Returns an object representing a deferred or asynchronous operation that resolves when the user signs in.
- [whenUserSignsOut](cloudkit.container/whenusersignsout.md)
  Returns an object representing a deferred or asynchronous operation that resolves when the user signs out.
### Discovering Users
- [fetchCurrentUserIdentity](cloudkit.container/fetchcurrentuseridentity.md)
  Fetches information about the current user asynchronously.
- [discoverAllUserIdentities](cloudkit.container/discoveralluseridentities.md)
  Fetches all user identities in the current user’s address book.
- [discoverUserIdentities](cloudkit.container/discoveruseridentities.md)
  Fetches all users in the specified array.
- [discoverUserIdentityWithEmailAddress](cloudkit.container/discoveruseridentitywithemailaddress.md)
  Fetches information about a single user based on the user’s email address.
- [discoverUserIdentityWithPhoneNumber](cloudkit.container/discoveruseridentitywithphonenumber.md)
  Fetches information about a single user based on the user’s phone number.
- [discoverUserIdentityWithUserRecordName](cloudkit.container/discoveruseridentitywithuserrecordname.md)
  Fetches information about a single user using the record name.
### Accepting Shared Records
- [acceptShares](cloudkit.container/acceptshares.md)
  Accepts a share—that is represented by a `shortGUID`—on behalf of the current user.
- [fetchRecordInfos](cloudkit.container/fetchrecordinfos.md)
  Returns information about a record for which you have a `shortGUID` property.
### Receiving Notifications
- [addNotificationListener](cloudkit.container/addnotificationlistener.md)
  Adds a function to call when a push notification occurs.
- [removeNotificationListener](cloudkit.container/removenotificationlistener.md)
  Removes a function to call when a push notification occurs.
- [registerForNotifications](cloudkit.container/registerfornotifications.md)
  Registers to receive push notifications.
- [unregisterForNotifications](cloudkit.container/unregisterfornotifications.md)
  Unregisters to receive push notifications.
- [isRegisteredForNotifications](cloudkit.container/isregisteredfornotifications.md)
  Boolean value indicating whether this container is registered to receive push notifications.
### Logging
- [toString](cloudkit.container/tostring.md)
  Returns a string representation of this [`CloudKit.Container`](cloudkit.container.md) object.

## See Also

- [CloudKit](cloudkit.md)
  Use the `CloudKit` namespace to configure CloudKit JS, and to access app containers and global constants.
- [CloudKit.CKError](cloudkit.ckerror.md)
  A [`CloudKit.CKError`](cloudkit.ckerror.md) object encapsulates an error that may occur when you use CloudKit JS. This includes CloudKit server errors and local errors.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container)*