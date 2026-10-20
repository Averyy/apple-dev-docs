# App Tracking Transparency

**Framework**: App Tracking Transparency  
**Kind**: module  
**Role**: Framework

Request authorization to access app-related data that your app can use to track the person or the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

#### Overview

Your app needs to use the App Tracking Transparency framework if it collects data about people and shares it with other companies to track them across apps and websites. The framework presents a tracking-authorization UI and reports the current authorization status.

#### Request authorization to access app-related data

To use the App Tracking Transparency framework:

1. Add the [`NSUserTrackingUsageDescription`](../BundleResources/information-property-list/nsusertrackingusagedescription.md) key to your app’s target properties in Xcode.
2. Call [`requestTrackingAuthorization(completionHandler:)`](./attrackingmanager/requesttrackingauthorization%28completionhandler%29.md) to present the tracking-authorization request.
3. Check [`trackingAuthorizationStatus`](./attrackingmanager/trackingauthorizationstatus.md) to determine the current authorization status; see [`ATTrackingManager.AuthorizationStatus`](./attrackingmanager/authorizationstatus.md) for the possible values.

For more information about app tracking and privacy, see [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/) and [App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/).

## Topics

### Essentials
- [class ATTrackingManager](./attrackingmanager.md)
  A class that requests tracking authorization and provides the current authorization status.
- [NSUserTrackingUsageDescription](../BundleResources/information-property-list/nsusertrackingusagedescription.md)
  A message that explains the purpose for accessing data that an app can use to track a person or device.
### Authorization requests
- [class func requestTrackingAuthorization(completionHandler: (ATTrackingManager.AuthorizationStatus) -> Void)](./attrackingmanager/requesttrackingauthorization%28completionhandler%29.md)
  Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.
- [class func requestTrackingAuthorization(preferExpandedInterface: Bool, additionalInformationAction: (() -> Void)?, completionHandler: (ATTrackingManager.AuthorizationStatus) -> Void)](./attrackingmanager/requesttrackingauthorization%28preferexpandedinterface,additionalinformationaction,completionhandler%29.md)
  Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.
- [NSUserTrackingMarkdownUsageDescription](../BundleResources/information-property-list/nsusertrackingmarkdownusagedescription.md)
  A message that explains the purpose for accessing data that an application can use to track a person or device.
### Authorization status and results
- [class var trackingAuthorizationStatus: ATTrackingManager.AuthorizationStatus](./attrackingmanager/trackingauthorizationstatus.md)
  A value that indicates the status of the app’s tracking authorization.
- [ATTrackingManager.AuthorizationStatus](./attrackingmanager/authorizationstatus.md)
  A type that represents the tracking-authorization status of an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppTrackingTransparency)*