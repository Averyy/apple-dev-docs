# BuildBetaNotificationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for the endpoint that sends a beta test notification for a build.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BuildBetaNotificationResponse
```

## Properties

- `data` (BuildBetaNotification) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [Send notification of an available build](post-v1-buildbetanotifications.md)
  Send a notification to all assigned beta testers that a build is available for testing.
- [object BuildBetaNotification](buildbetanotification.md)
  A push notification sent to eligible TestFlight testers when a new build is available to install.
- [object BuildBetaNotificationCreateRequest](buildbetanotificationcreaterequest.md)
  The request body you use to create a Build Beta Notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbetanotificationresponse)*