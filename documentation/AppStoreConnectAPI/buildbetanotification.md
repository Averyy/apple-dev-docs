# BuildBetaNotification

**Framework**: App Store Connect API  
**Kind**: dictionary

A push notification sent to eligible TestFlight testers when a new build is available to install.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BuildBetaNotification
```

## Properties

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object BuildBetaNotificationCreateRequest](buildbetanotificationcreaterequest.md)
  The request body you use to create a Build Beta Notification.
- [object BuildBetaNotificationResponse](buildbetanotificationresponse.md)
  The response body for the endpoint that sends a beta test notification for a build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbetanotification)*