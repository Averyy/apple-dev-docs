# CKDatabaseSubscription

**Framework**: Cloudkit  
**Kind**: class

A subscription that generates push notifications when CloudKit modifies records in a database.

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
class CKDatabaseSubscription
```

#### Overview

Subscriptions track the creation, modification, and deletion of records in a database, and are fundamental in keeping data on the user’s device up to date. A subscription applies only to the user that creates it. When a subscription registers a change, such as CloudKit saving a new record, it sends push notifications to the user’s devices to inform your app about the change. You can then fetch the changes and cache them on-device. When appropriate, the server excludes the device where the change originates.

> **Note**:  You don’t need to explicitly enable push notifications for your App ID to receive subscription notifications. Xcode automatically adds the entitlement when you enable the CloudKit capability. For more information, see [`Enabling CloudKit in Your App`](enabling-cloudkit-in-your-app.md). To use silent push notifications, add the Background Modes capability in your Xcode project and then select the “Background fetch” and “Remote notifications” options.

A database subscription executes whenever a change occurs in a custom record zone that resides in the database where you save the subscription. This is important for the shared database because you don’t know what record zones exist in advance. The only exception to this is the default record zone in the user’s private database, which doesn’t participate in database subscriptions.

You can further specialize a database subscription by setting its [`recordType`](ckdatabasesubscription/recordtype-46v7a.md) property to a specific record type. This limits the scope of the subscription to only track changes to records of that type and reduces the number of notifications it generates.

> **Note**:  Only private and shared databases support database subscriptions. If you attempt to save a database subscription in the public database, CloudKit returns an error.

Create any subscriptions on your app’s first launch. After you initialize a subscription, save it to the server using [`CKModifySubscriptionsOperation`](ckmodifysubscriptionsoperation.md). After the operation completes, record that state on-device (in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults), for example). You can then check that state on subsequent launches to prevent unnecessary trips to the server.

To configure the notification that the subscription generates, set the subscription’s [`notificationInfo`](cksubscription/notificationinfo-swift.property.md) property. Because the system coalesces notifications, don’t rely on them for specific changes. CloudKit can omit data to keep the payload size under the APNs size limit. Consider notifications an indication of remote changes, and use [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md) to fetch the record zones that contain those changes. After you have the record zones, use [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md) to fetch the changed records in each zone. Server change tokens allow you to limit the fetch results to just the changes since your previous fetch.

The example below shows how to create a database subscription in the user’s private database, configure the notifications it generates — in this case, silent push notifications — and then save that subscription to the server:

```swift
// Only proceed if the subscription doesn't already exist.
if([[NSUserDefaults standardUserDefaults]
    boolForKey:@"didCreateFeedSubscription"] == NO) {
        
    // Create a subscription with an ID that's unique within the scope of
    // the user's private database.
    CKDatabaseSubscription *subscription = 
        [[CKDatabaseSubscription alloc]
         initWithSubscriptionID:@"feed-changes"];
        
    // Scope the subscription to just the 'FeedItem' record type.
    subscription.recordType = @"FeedItem";
        
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
             setBool:YES forKey:@"didCreateFeedSubscription"];
        }
    };
        
    // Set an appropriate QoS and add the operation to the private
    // database's operation queue to execute it.
    operation.qualityOfService = NSQualityOfServiceUtility;
    [CKContainer.defaultContainer.privateCloudDatabase addOperation:operation];
}
```

## Topics

### Creating a Database Subscription
- [convenience init()](ckdatabasesubscription/init.md)
  Creates an empty database subscription.
- [convenience init(subscriptionID: CKSubscription.ID)](ckdatabasesubscription/init(subscriptionid:).md)
  Creates a named subscription for all records in a database.
- [init(coder: NSCoder)](ckdatabasesubscription/init(coder:).md)
  Creates a database subscription from a serialized instance.
### Accessing the Subscription Metadata
- [var recordType: CKRecord.RecordType?](ckdatabasesubscription/recordtype-46v7a.md)
  The type of record that the subscription queries.

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

## See Also

- [class CKDatabaseNotification](ckdatabasenotification.md)
  A notification that triggers when the contents of a database change.
- [class CKFetchDatabaseChangesOperation](ckfetchdatabasechangesoperation.md)
  An operation that fetches database changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CloudKit/ckdatabasesubscription)*