# ActivityAuthorizationInfo

**Framework**: ActivityKit  
**Kind**: class

An object with information about whether a person allowed your app to start Live Activities and permitted content updates with frequent ActivityKit push notifications.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
final class ActivityAuthorizationInfo
```

#### Overview

By default, your app can start, update, and end a Live Activity if you use ActivityKit to offer Live Activities. However, a person can deactivate Live Activities for an app in Settings. To check if your app can start, update, or end a Live Activity, use the synchronous [`areActivitiesEnabled`](activityauthorizationinfo/areactivitiesenabled.md) property or the asynchronous [`activityEnablementUpdates`](activityauthorizationinfo/activityenablementupdates-swift.property.md) sequence.

Similarly, `ActivityAuthorizationInfo` provides functionality to check whether a person has permitted your app to update Live Activities with frequent ActivityKit push notifications. To check whether you can send frequent ActivityKit push notifications to update Live Activity content, use the synchronous [`frequentPushesEnabled`](activityauthorizationinfo/frequentpushesenabled.md) property or the asynchronous [`frequentPushEnablementUpdates`](activityauthorizationinfo/frequentpushenablementupdates-swift.property.md) sequence.

> **Note**: To update a Live Activity with frequent ActivityKit push notifications, add the `NSSupportsFrequentLiveActivityUpdates` key with a Boolean value of `YES` to your app’s `Info.plist` file. For additional information, see [`Starting and updating Live Activities with ActivityKit push notifications`](starting-and-updating-live-activities-with-activitykit-push-notifications.md).

To update a Live Activity with frequent ActivityKit push notifications, add the `NSSupportsFrequentLiveActivityUpdates` key with a Boolean value of `YES` to your app’s `Info.plist` file. For additional information, see [`Starting and updating Live Activities with ActivityKit push notifications`](starting-and-updating-live-activities-with-activitykit-push-notifications.md).

## Topics

### Observing Live Activity permission changes
- [var areActivitiesEnabled: Bool](activityauthorizationinfo/areactivitiesenabled.md)
  A Boolean value that indicates whether your app can start a Live Activity.
- [let activityEnablementUpdates: ActivityAuthorizationInfo.ActivityEnablementUpdates](activityauthorizationinfo/activityenablementupdates-swift.property.md)
  An asynchronous sequence you use to observe whether your app can start a Live Activity.
- [ActivityAuthorizationInfo.ActivityEnablementUpdates](activityauthorizationinfo/activityenablementupdates-swift.struct.md)
  A structure that offers functionality to observe whether your app can start a Live Activity.
- [init()](activityauthorizationinfo/init.md)
  Creates an object you use to observe user authorizations for starting Live Activities and updating them with ActivityKit push notifications.
### Observing availability of frequent ActivityKit push notifications
- [var frequentPushesEnabled: Bool](activityauthorizationinfo/frequentpushesenabled.md)
  A Boolean value that indicates whether a person permitted you to update Live Activities with frequent ActivityKit push notifications.
- [let frequentPushEnablementUpdates: ActivityAuthorizationInfo.FrequentPushEnablementUpdates](activityauthorizationinfo/frequentpushenablementupdates-swift.property.md)
  An asynchronous sequence you use to observe whether a person permitted you to update Live Activities with frequent ActivityKit push notifications.
- [ActivityAuthorizationInfo.FrequentPushEnablementUpdates](activityauthorizationinfo/frequentpushenablementupdates-swift.struct.md)
  A structure that can observe whether you can update Live Activities with frequent ActivityKit push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationinfo)*