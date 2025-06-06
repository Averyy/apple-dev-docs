# requestTrackingAuthorization(completionHandler:)

**Framework**: App Tracking Transparency  
**Kind**: method

The request for user authorization to access app-related data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func requestTrackingAuthorization() async -> ATTrackingManager.AuthorizationStatus
```

#### Discussion

The [`requestTrackingAuthorization(completionHandler:)`](attrackingmanager/requesttrackingauthorization(completionhandler:).md) is a one-time request to authorize or deny access to app-related data that can be used for tracking the user or the device. The system remembers the user’s choice and doesn’t prompt again unless a user uninstalls and then reinstalls the app on the device.

Calls to the API only prompt when the application state is `UIApplicationStateActive`. The authorization prompt doesn’t display if another permission request is pending user confirmation. Concurrent requests aren’t preserved by iOS, and calls to the API through an app extension don’t prompt. Check the [`trackingAuthorizationStatus`](attrackingmanager/trackingauthorizationstatus.md) for a status of [`ATTrackingManager.AuthorizationStatus.notDetermined`](attrackingmanager/authorizationstatus/notdetermined.md) to determine if you need to make an additional call.

The completion handler will be called with the result of the user’s decision for granting or denying permission to use application tracking. The completion handler will be called immediately if access to request authorization is restricted.

> ❗ **Important**: To use [`requestTrackingAuthorization(completionHandler:)`](attrackingmanager/requesttrackingauthorization(completionhandler:).md), the [`NSUserTrackingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription) key must be in the [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List).

To use [`requestTrackingAuthorization(completionHandler:)`](attrackingmanager/requesttrackingauthorization(completionhandler:).md), the [`NSUserTrackingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription) key must be in the [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:))*