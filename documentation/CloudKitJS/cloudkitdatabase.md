# CloudKit.Database

**Framework**: CloudKit JS  
**Kind**: class

A [`CloudKit.Database`](cloudkit.database.md) object represents a public or private database in an app container.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
interface CloudKit.Database
```

#### Overview

Each container has a public database whose data is accessible to all users and, if the current user is signed in, a private database whose data is accessible only by the current user. A database object applies operations to records, subscriptions, and zones within a database.

You do not create database objects yourself, nor should you subclass the [`CloudKit.Database`](cloudkit.database.md) class. You get a database object using either the [`publicCloudDatabase`](cloudkit.container/publicclouddatabase.md) or [`privateCloudDatabase`](cloudkit.container/privateclouddatabase.md) properties in the [`CloudKit.Container`](cloudkit.container.md) class. You get a [`CloudKit.Container`](cloudkit.container.md) object using methods in the [`CloudKit`](cloudkit.md) namespace. For example, use [`CloudKit`](cloudkit.md).[`getDefaultContainer`](cloudkit/getdefaultcontainer.md) to get the default container object.

```javascript
var container = CloudKit.getDefaultContainer();
var publicDatabase = container.publicCloudDatabase;
var privateDatabase = container.privateCloudDatabase;
```

Read access to the public database doesn’t require that the user sign in. Your web app may fetch records and perform queries on the public database, but by default your app may not save changes to the public database without a signed-in user. Access to the private database requires that the user sign in. To determine whether a user is authenticated, see [`setUpAuth`](cloudkit.container/setupauth.md) in [`CloudKit.Container`](cloudkit.container.md).

The asynchronous methods in this class return a `Promise` object that resolves when the operation completes or is rejected due to an error. For a description of the `Promise` class returned by these methods, go to [`Mozilla Developer Network: Promise`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

This class is similar to the [`CKDatabase`](https://developer.apple.com/documentation/CloudKit/CKDatabase) class in the CloudKit framework.

##### Creating Your Schema

Before you can access records, you must create a schema from your native app using just-in-time schema (see [`Creating a Database Schema by Saving Records`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/CreatingaSchemabySavingRecords/CreatingaSchemabySavingRecords.html#//apple_ref/doc/uid/TP40014987-CH3)) or using CloudKit Dashboard (see [`Using CloudKit Dashboard to Manage Databases`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/EditingSchemesUsingCloudKitDashboard/EditingSchemesUsingCloudKitDashboard.html#//apple_ref/doc/uid/TP40014987-CH5)). Use CloudKit Dashboard to verify that the record types and fields appear in your app’s containers before you test your JavaScript code.

![None](https://docs-assets.developer.apple.com/published/0b25b802e8e3f81ba6af903b14cfe23e/media-2556286%402x.png)

## Topics

### Getting the Container ID
- [containerIdentifier](cloudkit.database/containeridentifier.md)
  A unique identifier for the container that this database resides in.
### Accessing Records
- [saveRecords](cloudkit.database/saverecords.md)
  Saves records to the database.
- [fetchRecords](cloudkit.database/fetchrecords.md)
  Fetches one or more records.
- [deleteRecords](cloudkit.database/deleterecords.md)
  Deletes one or more records.
- [performQuery](cloudkit.database/performquery.md)
  Fetches records by using a query.
- [newRecordsBatch](cloudkit.database/newrecordsbatch.md)
  Creates records batch builder object for modifying multiple records.
### Accessing Record Zones
- [saveRecordZones](cloudkit.database/saverecordzones.md)
  Creates one or more zones in the database.
- [fetchRecordZones](cloudkit.database/fetchrecordzones.md)
  Fetches one or more zones.
- [fetchAllRecordZones](cloudkit.database/fetchallrecordzones.md)
  Fetches all zones in the database.
- [deleteRecordZones](cloudkit.database/deleterecordzones.md)
  Deletes the specified zones.
### Subscribing to Changes
- [saveSubscriptions](cloudkit.database/savesubscriptions.md)
  Saves one or more subscriptions to record changes.
- [fetchSubscriptions](cloudkit.database/fetchsubscriptions.md)
  Fetches one or more subscriptions.
- [fetchAllSubscriptions](cloudkit.database/fetchallsubscriptions.md)
  Fetches all subscriptions in the schema.
- [deleteSubscriptions](cloudkit.database/deletesubscriptions.md)
  Deletes one or more subscriptions.
### Fetching Changes
- [databaseScope](cloudkit.database/databasescope.md)
  The type of database (public, private, or shared).
- [fetchDatabaseChanges](cloudkit.database/fetchdatabasechanges.md)
  Fetch changed record zones in the database.
- [fetchRecordZoneChanges](cloudkit.database/fetchrecordzonechanges.md)
  Fetch changes to the specified record zones in the database.
### Sharing Records
- [shareWithUI](cloudkit.database/sharewithui.md)
  Presents a UI to the user which lets them share a record with other users.
### Logging
- [toString](cloudkit.database/tostring.md)
  Returns a string representation of this object.

## See Also

- [CloudKit](cloudkit.md)
  Use the `CloudKit` namespace to configure CloudKit JS, and to access app containers and global constants.
- [CloudKit.CKError](cloudkit.ckerror.md)
  A [`CloudKit.CKError`](cloudkit.ckerror.md) object encapsulates an error that may occur when you use CloudKit JS. This includes CloudKit server errors and local errors.
- [CloudKit.Container](cloudkit.container.md)
  A [`CloudKit.Container`](cloudkit.container.md) object provides access to an app container, and through the app container, access to its databases. It also contains methods for authenticating and fetching users.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database)*