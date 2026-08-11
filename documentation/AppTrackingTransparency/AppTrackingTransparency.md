# App Tracking Transparency

**Framework**: App Tracking Transparency  
**Kind**: module

Request user authorization to access app-related data for tracking the user or the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

#### Overview

You must use the AppTrackingTransparency framework if your app collects data about end users and shares it with other companies for purposes of tracking across apps and web sites. The AppTrackingTransparency framework presents an app-tracking authorization request to the user and provides the tracking authorization status.

To use the AppTrackingTransparency framework:

1. Set up a [`NSUserTrackingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription) to display a system-permission alert request for your app installed on end-user devices.
2. Call [`requestTrackingAuthorization(completionHandler:)`](attrackingmanager/requesttrackingauthorization(completionhandler:).md) to present the app-tracking authorization request to the end user.
3. Use [`trackingAuthorizationStatus`](attrackingmanager/trackingauthorizationstatus.md) to determine the app-tracking permission status. See [`ATTrackingManager.AuthorizationStatus`](attrackingmanager/authorizationstatus.md) for status enums.

For more information about app tracking and privacy, see [`User Privacy and Data Use`](https://developer.apple.comhttps://developer.apple.com/app-store/user-privacy-and-data-use/) and [`App Privacy Details`](https://developer.apple.comhttps://developer.apple.com/app-store/app-privacy-details/).

## Topics

### Essentials
- [NSUserTrackingUsageDescription](../BundleResources/Information-Property-List/NSUserTrackingUsageDescription.md)
  A message that informs the user why an app is requesting permission to use data for tracking the user or the device.
### Class and Components
- [class ATTrackingManager](attrackingmanager.md)
  A class that provides a tracking authorization request and the tracking authorization status of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppTrackingTransparency)*