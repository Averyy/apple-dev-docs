# areActivitiesEnabled

**Framework**: ActivityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether your app can start a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
final var areActivitiesEnabled: Bool { get }
```

## Mentions

- [Displaying live data with Live Activities](../displaying-live-data-with-live-activities.md)

## See Also

### Observing Live Activity permission changes
- [let activityEnablementUpdates: ActivityAuthorizationInfo.ActivityEnablementUpdates](./activityenablementupdates-swift.property.md)
  An asynchronous sequence you use to observe whether your app can start a Live Activity.
- [ActivityAuthorizationInfo.ActivityEnablementUpdates](./activityenablementupdates-swift.struct.md)
  A structure that offers functionality to observe whether your app can start a Live Activity.
- [init()](./init%28%29.md)
  Creates an object you use to observe user authorizations for starting Live Activities and updating them with ActivityKit push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/areactivitiesenabled)*