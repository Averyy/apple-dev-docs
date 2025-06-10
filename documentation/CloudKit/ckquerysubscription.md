# CKQuerySubscription

**Framework**: CloudKit  
**Kind**: class

A subscription that generates push notifications when CloudKit modifies records that match a predicate.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CKQuerySubscription
```

#### Overview

Subscriptions track the creation, modification, and deletion of records in a database, and are fundamental in keeping data on the user’s device up to date. A subscription applies only to the user that creates it. When a subscription registers a change, such as CloudKit saving a new record, it sends push notifications to the user’s devices to inform your app about the change. You can then fetch the changes and cache them on-device. When appropriate, the server excludes the device where the change originates.

> **Note**:  You don’t need to explicitly enable push notifications for your App ID to receive subscription notifications. Xcode automatically adds the entitlement when you enable the CloudKit capability. For more information, see [`Enabling CloudKit in Your App`](enabling-cloudkit-in-your-app.md). To use silent push notifications, add the Background Modes capability in your Xcode project and then select the “Background fetch” and “Remote notifications” options.

Query subscriptions execute whenever a change occurs in a database that matches the predicate and options you specify. You scope a query subscription to an individual record type that you provide during initialization. You can set the subscription’s [`zoneID`](ckquerysubscription/zoneid.md) property to further specialize the subscription to a specific record zone in the database. This limits the scope of the subscription to only track changes in that record zone and reduces the number of notifications it generates. For more information about defining CloudKit-compatible predicates, see [`CKQuery`](ckquery.md).

> **Note**:  Only public and private databases support query subscriptions. If you attempt to save a database subscription in the shared database, CloudKit returns an error.

Create any subscriptions on your app’s first launch. After you initialize a subscription, save it to the server using [`CKModifySubscriptionsOperation`](ckmodifysubscriptionsoperation.md). When the operation completes, record that state on-device (in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults), for example). You can then check that state on subsequent launches to prevent unnecessary trips to the server.

To configure the notification the subscription generates, set the subscription’s [`notificationInfo`](cksubscription/notificationinfo-swift.property.md) property. Because the system coalesces notifications, don’t rely on them for specific changes. CloudKit can omit data to keep the payload size under the APNs size limit. Consider notifications an indication of remote changes and use [`CKQueryOperation`](ckqueryoperation.md) to fetch the changed records. Create the operation with an instance of [`CKQuery`](ckquery.md) that you configure with the same record type and predicate as the subscription. If you limit the subscription to a specific record zone, set the operation’s [`zoneID`](ckqueryoperation/zoneid.md) property to that record zone’s ID. Because [`CKQueryOperation`](ckqueryoperation.md) doesn’t employ server change tokens, dispose of any records you cache on-device and use the query’s results instead.

The example below shows how to create a query subscription in the user’s private database, configure the notifications it generates — in this case, silent push notifications — and then save that subscription to the server:

```swift
// Only proceed if the subscription doesn't already exist.
if([[NSUserDefaults standardUserDefaults]
    boolForKey:@"didCreateQuerySubscription"] == NO) {
        
// Define a predicate that matches records with a tags field
// that contains the word 'Swift'.
NSPredicate *predicate = [NSPredicate predicateWithFormat:
                          @"tags CONTAINS 'Swift'"];
        
// Create a subscription and scope it to the 'FeedItem' record type.
// Provide a unique identifier for the subscription and declare the
// circumstances for invoking it.
CKQuerySubscriptionOptions options = 
    CKQuerySubscriptionOptionsFiresOnRecordCreation;
CKQuerySubscription *subscription = [[CKQuerySubscription alloc]
                                     initWithRecordType:@"FeedItem"
                                     predicate:predicate
                                     subscriptionID:@"tagged-feed-changes"
                                     options:options];
        
// Further specialize the subscription to only evaluate
// records in a specific record zone
subscription.zoneID = recordZone.zoneID;
        
// Configure the notification so that the system delivers it silently
// and, therefore, doesn't require permission from the user.
CKNotificationInfo *notificationInfo = [CKNotificationInfo new];
notificationInfo.shouldSendContentAvailable = YES;
subscription.notificationInfo = notificationInfo;
        
// Create an operation that saves the subscription to the server.
CKModifySubscriptionsOperation *operation =
    [[CKModifySubscriptionsOperation alloc]
     initWithSubscriptionsToSave:@[subscription]
     subscriptionIDsToDelete:NULL];

operation.modifySubscriptionsCompletionBlock =
    ^(NSArray *subscriptions, NSArray *deleted, NSError *error) {
    if (error) {
        // Handle the error.
    } else {
        // Record that the system successfully creates the subscription
        // to prevent unnecessary trips to the server in later launches.
        [[NSUserDefaults standardUserDefaults]
         setBool:YES forKey:@"didCreateQuerySubscription"];
    }
};
        
// Set an appropriate QoS and add the operation to the private
// database's operation queue to execute it.
operation.qualityOfService = NSQualityOfServiceUtility;
[CKContainer.defaultContainer.privateCloudDatabase addOperation:operation];
```

## Topics

### Creating a Subscription
- [convenience init(recordType: CKRecord.RecordType, predicate: NSPredicate, subscriptionID: CKSubscription.ID, options: CKQuerySubscription.Options)](ckquerysubscription/init(recordtype:predicate:subscriptionid:options:).md)
  Creates a named query-based subscription that queries records of a specific type.
- [init(coder: NSCoder)](ckquerysubscription/init(coder:).md)
  Creates a query-based subscription from a serialized instance.
### Accessing the Subscription Search Parameters
- [var predicate: NSPredicate](ckquerysubscription/predicate.md)
  The matching criteria to apply to records.
- [var querySubscriptionOptions: CKQuerySubscription.Options](ckquerysubscription/querysubscriptionoptions.md)
  Options that define the behavior of the subscription.
- [CKQuerySubscription.Options](ckquerysubscription/options.md)
  Configuration options for a query subscription.
### Accessing the Subscription Metadata
- [var recordType: CKRecord.RecordType?](ckquerysubscription/recordtype-4qgdo.md)
  The type of record that the subscription queries.
- [var zoneID: CKRecordZone.ID?](ckquerysubscription/zoneid.md)
  The ID of the record zone that the subscription queries.
### Initializers
- [convenience init(recordType: CKRecord.RecordType, predicate: NSPredicate, options: CKQuerySubscription.Options)](ckquerysubscription/init(recordtype:predicate:options:).md)

## Relationships

### Inherits From
- [CKSubscription](cksubscription.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CKQueryNotification](ckquerynotification.md)
  A notification that triggers when a record that matches the subscription’s predicate changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription)*