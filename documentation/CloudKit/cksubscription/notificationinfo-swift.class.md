# CKSubscription.NotificationInfo

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that describes the configuration of a subscription’s push notifications.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class NotificationInfo
```

```objc
@interface CKNotificationInfo : NSObject
```

#### Overview

When configuring a subscription, use this class to specify the type of push notifications you want to generate when conditions meet the subscription’s trigger. You can provide content that the system displays to the user, describe the sounds to play, and indicate whether the app’s icon has a badge. You can request that the notification include information about the record that triggers it.

When your app receives a push notification that a subscription generates, instantiate an instance of [`CKNotification`](../cknotification.md) using the [`init(fromRemoteNotificationDictionary:)`](../cknotification/init%28fromremotenotificationdictionary%29.md) method and pass the notification’s payload. The object that the method returns contains the data you specify when configuring the subscription.

For more information about push notification alerts and how they display to the user, see [Apple Push Notification Service](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html#//apple_ref/doc/uid/TP40008194-CH100) in [Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

> **Note**: If you don’t set any of the [`alertBody`](./notificationinfo-swift.class/alertbody.md), [`soundName`](./notificationinfo-swift.class/soundname.md), or [`shouldBadge`](./notificationinfo-swift.class/shouldbadge.md) properties, CloudKit sends the push notification using a lower priority and doesn’t display any content to the user.

## Topics

### Creating Notification Information
- [convenience init(alertBody: String?, alertLocalizationKey: String?, alertLocalizationArgs: [CKRecord.FieldKey], title: String?, titleLocalizationKey: String?, titleLocalizationArgs: [CKRecord.FieldKey], subtitle: String?, subtitleLocalizationKey: String?, subtitleLocalizationArgs: [CKRecord.FieldKey], alertActionLocalizationKey: String?, alertLaunchImage: String?, soundName: String?, desiredKeys: [CKRecord.FieldKey], shouldBadge: Bool, shouldSendContentAvailable: Bool, shouldSendMutableContent: Bool, category: String?, collapseIDKey: String?)](./notificationinfo-swift.class/init%28alertbody_alertlocalizationkey_alertlocalizationargs_title_titlelocalizationkey_titlelocalizationargs_subtitle_subtitlelocalizationkey_subtitlelocalizationargs_alertactionlocalizationkey_alertlaunchimage_soundname-a72a0c89.md)
  Creates a notification with the specified values.
### Grouping Notifications
- [var category: String?](./notificationinfo-swift.class/category.md)
  The name of the action group that corresponds to this notification.
- [var collapseIDKey: String?](./notificationinfo-swift.class/collapseidkey.md)
  A value that the system uses to coalesce unseen push notifications.
### Displaying Badges
- [var shouldBadge: Bool](./notificationinfo-swift.class/shouldbadge.md)
  A Boolean value that determines whether an app’s icon badge increments its value.
### Accessing the Notification Alert
- [var alertBody: String?](./notificationinfo-swift.class/alertbody.md)
  The text for the notification’s alert.
- [var alertLocalizationKey: String?](./notificationinfo-swift.class/alertlocalizationkey.md)
  The key that identifies the localized string for the notification’s alert.
- [var alertLocalizationArgs: [CKRecord.FieldKey]?](./notificationinfo-swift.class/alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](./notificationinfo-swift.class/alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var alertLaunchImage: String?](./notificationinfo-swift.class/alertlaunchimage.md)
  The filename of an image to use as a launch image.
- [var soundName: String?](./notificationinfo-swift.class/soundname.md)
  The filename of the sound file to play when a notification arrives.
### Accessing the Notification Info
- [var shouldSendContentAvailable: Bool](./notificationinfo-swift.class/shouldsendcontentavailable.md)
  A Boolean value that indicates whether the push notification includes the content available flag.
- [var shouldSendMutableContent: Bool](./notificationinfo-swift.class/shouldsendmutablecontent.md)
  A Boolean value that indicates whether the push notification sets the mutable content flag.
### Accessing the Record’s Data
- [var desiredKeys: [CKRecord.FieldKey]?](./notificationinfo-swift.class/desiredkeys.md)
  The names of fields to include in the push notification’s payload.
### Accessing the Notification Title
- [var title: String?](./notificationinfo-swift.class/title.md)
  The notification’s title.
- [var titleLocalizationKey: String?](./notificationinfo-swift.class/titlelocalizationkey.md)
  The key that identifies the localized string for the notification’s title.
- [var titleLocalizationArgs: [CKRecord.FieldKey]?](./notificationinfo-swift.class/titlelocalizationargs.md)
  The fields for building a notification’s title.
### Accessing the Notification Subtitle
- [var subtitle: String?](./notificationinfo-swift.class/subtitle.md)
  The notification’s subtitle.
- [var subtitleLocalizationKey: String?](./notificationinfo-swift.class/subtitlelocalizationkey.md)
  The key that identifies the localized string for the notification’s subtitle.
- [var subtitleLocalizationArgs: [CKRecord.FieldKey]?](./notificationinfo-swift.class/subtitlelocalizationargs.md)
  The fields for building a notification’s subtitle.
### Initializers
- [init?(coder: NSCoder)](./notificationinfo-swift.class/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the Push Notification Data
- [var notificationInfo: CKSubscription.NotificationInfo?](./notificationinfo-swift.property.md)
  The configuration for a subscription’s push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class)*