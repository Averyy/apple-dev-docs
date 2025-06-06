# Build Beta Notifications

**Framework**: App Store Connect API

Requests to send notifications to all assigned testers that builds are ready for testing.

#### Overview

You use a `buildBetaNotifications` resource to manually notify all assigned beta testers that a build is available for testing.

## Topics

### Sending Notifications
- [Send Notification of an Available Build](post-v1-buildbetanotifications.md)
  Send a notification to all assigned beta testers that a build is available for testing.
### Objects
- [object BuildBetaNotification](buildbetanotification.md)
  The data structure that represents a Build Beta Notifications resource.
- [object BuildBetaNotificationCreateRequest](buildbetanotificationcreaterequest.md)
  The request body you use to create a Build Beta Notification.
- [object BuildBetaNotificationResponse](buildbetanotificationresponse.md)
  A response that contains a single Build Beta Notifications resource.

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [Build Beta Details](build-beta-details.md)
  TestFlight-specific information about beta builds.
- [Beta Build Localizations](beta-build-localizations.md)
  Beta test information about builds, specific to a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build-beta-notifications)*