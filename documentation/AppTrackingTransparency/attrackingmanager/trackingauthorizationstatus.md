# trackingAuthorizationStatus

**Framework**: App Tracking Transparency  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, nonatomic, assign, readonly) ATTrackingManagerAuthorizationStatus trackingAuthorizationStatus;
```

#### Discussion

Check this property to determine whether your app has permission to access app-related data it can use to track a person or device.

If the status is [`ATTrackingManager.AuthorizationStatus.notDetermined`](./authorizationstatus/notdetermined.md), call one of the tracking-request methods to present the tracking-authorization prompt and ask the person for permission:

- [`requestTrackingAuthorization(completionHandler:)`](./requesttrackingauthorization%28completionhandler%29.md)
- [`requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)`](./requesttrackingauthorization%28preferexpandedinterface,additionalinformationaction,completionhandler%29.md)

This property returns [`ATTrackingManager.AuthorizationStatus.restricted`](./authorizationstatus/restricted.md) when the system restricts tracking for the device, regardless of whether your app has presented the prompt.

## See Also

### Authorization status and results
- [ATTrackingManager.AuthorizationStatus](./authorizationstatus.md)
  A type that represents the tracking-authorization status of an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/trackingauthorizationstatus)*