# CKSubscription.NotificationInfo

**Framework**: CloudKit  
**Kind**: class

An object that describes the configuration of a subscription’s push notifications.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class NotificationInfo
```

#### Overview

When configuring a subscription, use this class to specify the type of push notifications you want to generate when conditions meet the subscription’s trigger. You can provide content that the system displays to the user, describe the sounds to play, and indicate whether the app’s icon has a badge. You can request that the notification include information about the record that triggers it.

When your app receives a push notification that a subscription generates, instantiate an instance of [`CKNotification`](cknotification.md) using the [`init(fromRemoteNotificationDictionary:)`](cknotification/init(fromremotenotificationdictionary:).md) method and pass the notification’s payload. The object that the method returns contains the data you specify when configuring the subscription.

For more information about push notification alerts and how they display to the user, see [`Apple Push Notification Service`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html#//apple_ref/doc/uid/TP40008194-CH100) in [`Local and Remote Notification Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

> **Note**:  If you don’t set any of the [`alertBody`](cksubscription/notificationinfo-swift.class/alertbody.md), [`soundName`](cksubscription/notificationinfo-swift.class/soundname.md), or [`shouldBadge`](cksubscription/notificationinfo-swift.class/shouldbadge.md) properties, CloudKit sends the push notification using a lower priority and doesn’t display any content to the user.

## Topics

### Creating Notification Information
- [convenience init(alertBody: String?, alertLocalizationKey: String?, alertLocalizationArgs: [CKRecord.FieldKey], title: String?, titleLocalizationKey: String?, titleLocalizationArgs: [CKRecord.FieldKey], subtitle: String?, subtitleLocalizationKey: String?, subtitleLocalizationArgs: [CKRecord.FieldKey], alertActionLocalizationKey: String?, alertLaunchImage: String?, soundName: String?, desiredKeys: [CKRecord.FieldKey], shouldBadge: Bool, shouldSendContentAvailable: Bool, shouldSendMutableContent: Bool, category: String?, collapseIDKey: String?)](cksubscription/notificationinfo-swift.class/init(alertbody:alertlocalizationkey:alertlocalizationargs:title:titlelocalizationkey:titlelocalizationargs:subtitle:subtitlelocalizationkey:subtitlelocalizationargs:alertactionlocalizationkey:alertlaunchimage:soundname:desiredkeys:shouldbad-47rj5.md)
  Creates a notification with the specified values.
### Grouping Notifications
- [var category: String?](cksubscription/notificationinfo-swift.class/category.md)
  The name of the action group that corresponds to this notification.
- [var collapseIDKey: String?](cksubscription/notificationinfo-swift.class/collapseidkey.md)
  A value that the system uses to coalesce unseen push notifications.
### Displaying Badges
- [var shouldBadge: Bool](cksubscription/notificationinfo-swift.class/shouldbadge.md)
  A Boolean value that determines whether an app’s icon badge increments its value.
### Accessing the Notification Alert
- [var alertBody: String?](cksubscription/notificationinfo-swift.class/alertbody.md)
  The text for the notification’s alert.
- [var alertLocalizationKey: String?](cksubscription/notificationinfo-swift.class/alertlocalizationkey.md)
  The key that identifies the localized string for the notification’s alert.
- [var alertLocalizationArgs: [CKRecord.FieldKey]?](cksubscription/notificationinfo-swift.class/alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](cksubscription/notificationinfo-swift.class/alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var alertLaunchImage: String?](cksubscription/notificationinfo-swift.class/alertlaunchimage.md)
  The filename of an image to use as a launch image.
- [var soundName: String?](cksubscription/notificationinfo-swift.class/soundname.md)
  The filename of the sound file to play when a notification arrives.
### Accessing the Notification Info
- [var shouldSendContentAvailable: Bool](cksubscription/notificationinfo-swift.class/shouldsendcontentavailable.md)
  A Boolean value that indicates whether the push notification includes the content available flag.
- [var shouldSendMutableContent: Bool](cksubscription/notificationinfo-swift.class/shouldsendmutablecontent.md)
  A Boolean value that indicates whether the push notification sets the mutable content flag.
### Accessing the Record’s Data
- [var desiredKeys: [CKRecord.FieldKey]?](cksubscription/notificationinfo-swift.class/desiredkeys.md)
  The names of fields to include in the push notification’s payload.
### Accessing the Notification Title
- [var title: String?](cksubscription/notificationinfo-swift.class/title.md)
  The notification’s title.
- [var titleLocalizationKey: String?](cksubscription/notificationinfo-swift.class/titlelocalizationkey.md)
  The key that identifies the localized string for the notification’s title.
- [var titleLocalizationArgs: [CKRecord.FieldKey]?](cksubscription/notificationinfo-swift.class/titlelocalizationargs.md)
  The fields for building a notification’s title.
### Accessing the Notification Subtitle
- [var subtitle: String?](cksubscription/notificationinfo-swift.class/subtitle.md)
  The notification’s subtitle.
- [var subtitleLocalizationKey: String?](cksubscription/notificationinfo-swift.class/subtitlelocalizationkey.md)
  The key that identifies the localized string for the notification’s subtitle.
- [var subtitleLocalizationArgs: [CKRecord.FieldKey]?](cksubscription/notificationinfo-swift.class/subtitlelocalizationargs.md)
  The fields for building a notification’s subtitle.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [var notificationInfo: CKSubscription.NotificationInfo?](cksubscription/notificationinfo-swift.property.md)
  The configuration for a subscription’s push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class)*