# CKSubscription

**Framework**: CloudKit  
**Kind**: class

An abstract base class for subscriptions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKSubscription
```

#### Overview

A subscription acts like a persistent query on the server that can track the creation, deletion, and modification of records. When changes occur, they trigger the delivery of push notifications so that your app can respond appropriately.

Subscriptions don’t become active until you save them to the server and the server has time to index them. To save a subscription, use an instance of [`CKModifySubscriptionsOperation`](ckmodifysubscriptionsoperation.md) or the [`save(_:completionHandler:)`](ckdatabase/save(_:completionhandler:)-9pona.md) method of [`CKDatabase`](ckdatabase.md). To cancel a subscription, delete the corresponding subscription from the server.

> **Note**:  You don’t need to enable push notifications for the app’s explicit App ID in your developer account at [`developer.apple.com`](https://developer.apple.comhttps://developer.apple.com) to receive subscription notifications. Xcode automatically adds the APNs entitlement to your entitlement file when you enable CloudKit. To learn about enabling CloudKit, see [`Enabling CloudKit in Your App`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/EnablingiCloudandConfiguringCloudKit/EnablingiCloudandConfiguringCloudKit.html#//apple_ref/doc/uid/TP40014987-CH2).

 You don’t need to enable push notifications for the app’s explicit App ID in your developer account at [`developer.apple.com`](https://developer.apple.comhttps://developer.apple.com) to receive subscription notifications. Xcode automatically adds the APNs entitlement to your entitlement file when you enable CloudKit. To learn about enabling CloudKit, see [`Enabling CloudKit in Your App`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/EnablingiCloudandConfiguringCloudKit/EnablingiCloudandConfiguringCloudKit.html#//apple_ref/doc/uid/TP40014987-CH2).

Most of a subscription’s configuration happens at initialization time. You must, however, specify how to deliver push notifications to the user’s device. Use the [`notificationInfo`](cksubscription/notificationinfo-swift.property.md) property to configure the delivery options. You must save the subscription before the changes take effect.

> **Note**:  Create subscriptions in the development environment first and then promote them to production.  Attempting to create a subscription directly in the production environment results in an error.

 Create subscriptions in the development environment first and then promote them to production.  Attempting to create a subscription directly in the production environment results in an error.

##### Handling the Resulting Push Notifications

When CloudKit modifies a record and triggers a subscription, the server sends push notifications to all devices with that subscription except for the one that makes the original changes. For subscription-based push notifications, the server can add data to the notification payload that indicates the condition that triggers the notification. In the [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didReceiveRemoteNotification:fetchCompletionHandler:)) method of your app delegate, create a [`CKNotification`](cknotification.md) object from the provided `userInfo` dictionary. You can then query it for the information that’s relevant to the notification.

In addition to sending a record ID with a push notification, you can ask the server to send a limited amount of data from the record that triggers the notification. Use the [`desiredKeys`](cksubscription/notificationinfo-swift.class/desiredkeys.md) property of the object you assign to [`notificationInfo`](cksubscription/notificationinfo-swift.property.md) to specify the keys to include.

APNs limits the size of a push notification’s payload and CloudKit may omit keys and other pieces of data to keep the payload’s size under that limit. If this happens, you can fetch the entire payload from the server using an instance of `CKFetchNotificationChangesOperation`. This operation provides instances of [`CKQueryNotification`](ckquerynotification.md) or [`CKRecordZoneNotification`](ckrecordzonenotification.md), which contain information about the push notifications that CloudKit delivers to your app.

## Topics

### Specifying the Push Notification Data
- [var notificationInfo: CKSubscription.NotificationInfo?](cksubscription/notificationinfo-swift.property.md)
  The configuration for a subscription’s push notifications.
- [CKSubscription.NotificationInfo](cksubscription/notificationinfo-swift.class.md)
  An object that describes the configuration of a subscription’s push notifications.
### Accessing the Subscription Metadata
- [var subscriptionID: CKSubscription.ID](cksubscription/subscriptionid-6fp3j.md)
  The subscription’s unique identifier.
- [CKSubscription.ID](cksubscription/id.md)
  A type that represents a subscription’s identifier.
- [var subscriptionType: CKSubscription.SubscriptionType](cksubscription/subscriptiontype-swift.property.md)
  The behavior that a subscription provides.
- [CKSubscription.SubscriptionType](cksubscription/subscriptiontype-swift.enum.md)
  Constants that identify a subscription’s behavior.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CKDatabaseSubscription](ckdatabasesubscription.md)
- [CKQuerySubscription](ckquerysubscription.md)
- [CKRecordZoneSubscription](ckrecordzonesubscription.md)
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

- [class CKNotification](cknotification.md)
  The abstract base class for CloudKit notifications.
- [class CKDatabaseOperation](ckdatabaseoperation.md)
  The abstract base class for operations that act upon databases in CloudKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription)*