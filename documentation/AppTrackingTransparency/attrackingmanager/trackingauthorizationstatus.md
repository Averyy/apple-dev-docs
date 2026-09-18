# trackingAuthorizationStatus

**Framework**: App Tracking Transparency  
**Kind**: property

A value that indicates the status of the app’s tracking authorization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var trackingAuthorizationStatus: ATTrackingManager.AuthorizationStatus { get }
```

#### Discussion

Check this property to determine whether your app has permission to access app-related data it can use to track a person or device.

If the status is [`ATTrackingManager.AuthorizationStatus.notDetermined`](attrackingmanager/authorizationstatus/notdetermined.md), call one of the tracking-request methods to present the tracking-authorization prompt and ask the person for permission:

- [`requestTrackingAuthorization(completionHandler:)`](attrackingmanager/requesttrackingauthorization(completionhandler:).md)
- [`requestTrackingAuthorization(usingExpandedInterface:additionalInformationAction:completionHandler:)`](attrackingmanager/requesttrackingauthorization(usingexpandedinterface:additionalinformationaction:completionhandler:).md)

This property returns [`ATTrackingManager.AuthorizationStatus.restricted`](attrackingmanager/authorizationstatus/restricted.md) when the system restricts tracking for the device, regardless of whether your app has presented the prompt.

## See Also

- [ATTrackingManager.AuthorizationStatus](attrackingmanager/authorizationstatus.md)
  A type that represents the tracking-authorization status of an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/trackingauthorizationstatus)*