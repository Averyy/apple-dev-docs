# CKNotification

**Framework**: CloudKit  
**Kind**: class

The abstract base class for CloudKit notifications.

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
class CKNotification
```

#### Overview

Use subclasses of `CKNotification` to extract data from push notifications that the system receives, or to fetch a container’s previous push notifications. In both cases, the object indicates the changed data.

`CKNotification` is an abstract class. When you create a notification from a payload dictionary, the [`init(fromRemoteNotificationDictionary:)`](cknotification/init(fromremotenotificationdictionary:).md) method returns an instance of the appropriate subclass. Similarly, when you fetch notifications from a container, you receive instances of a concrete subclass. `CKNotification` provides information about the push notification and its method of delivery. Subclasses contain specific data that provides the changes.

## Topics

### Creating a Notification
- [convenience init?(fromRemoteNotificationDictionary: [AnyHashable : Any])](cknotification/init(fromremotenotificationdictionary:).md)
  Creates a new notification using the specified payload data.
### Identifying the Notification
- [var notificationID: CKNotification.ID?](cknotification/notificationid.md)
  The notification’s ID.
- [CKNotification.ID](cknotification/id.md)
  An object that uniquely identifies a push notification that a container sends.
- [var notificationType: CKNotification.NotificationType](cknotification/notificationtype-swift.property.md)
  The type of event that generates the notification.
- [CKNotification.NotificationType](cknotification/notificationtype-swift.enum.md)
  Constants that indicate the type of event that generates the push notification.
- [var containerIdentifier: String?](cknotification/containeridentifier.md)
  The ID of the container with the content that triggers the notification.
### Getting the Notification’s Status
- [var isPruned: Bool](cknotification/ispruned.md)
  A Boolean value that indicates whether the system removes some push notification content before delivery.
### Accessing the Notification Info
- [var alertBody: String?](cknotification/alertbody.md)
  The notification’s alert body.
- [var alertLocalizationKey: String?](cknotification/alertlocalizationkey.md)
  The key that identifies the localized text for the alert body.
- [var alertLocalizationArgs: [String]?](cknotification/alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](cknotification/alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var alertLaunchImage: String?](cknotification/alertlaunchimage.md)
  The filename of an image to use as a launch image.
- [var soundName: String?](cknotification/soundname.md)
  The name of the sound file to play when a notification arrives.
- [var badge: NSNumber?](cknotification/badge.md)
  The value that the app icon’s badge displays.
- [var category: String?](cknotification/category.md)
  The name of the action group that corresponds to this notification.
- [var subscriptionID: CKSubscription.ID?](cknotification/subscriptionid-16ygj.md)
  The ID of the subscription that triggers the notification.
- [var subscriptionOwnerUserRecordID: CKRecord.ID?](cknotification/subscriptionowneruserrecordid.md)
  The ID of the user record that creates the subscription that generates the push notification.
- [var title: String?](cknotification/title.md)
  The notification’s title.
- [var titleLocalizationKey: String?](cknotification/titlelocalizationkey.md)
  The key that identifies the localized string for the notification’s title.
- [var titleLocalizationArgs: [String]?](cknotification/titlelocalizationargs.md)
  The fields for building a notification’s title.
- [var subtitle: String?](cknotification/subtitle.md)
  The notification’s subtitle.
- [var subtitleLocalizationKey: String?](cknotification/subtitlelocalizationkey.md)
  The key that identifies the localized string for the notification’s subtitle.
- [var subtitleLocalizationArgs: [String]?](cknotification/subtitlelocalizationargs.md)
  The fields for building a notification’s subtitle.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CKDatabaseNotification](ckdatabasenotification.md)
- [CKQueryNotification](ckquerynotification.md)
- [CKRecordZoneNotification](ckrecordzonenotification.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CKSubscription](cksubscription.md)
  An abstract base class for subscriptions.
- [class CKDatabaseOperation](ckdatabaseoperation.md)
  The abstract base class for operations that act upon databases in CloudKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification)*