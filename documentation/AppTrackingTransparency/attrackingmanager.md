# ATTrackingManager

**Framework**: App Tracking Transparency  
**Kind**: class

A class that requests tracking authorization and provides the current authorization status.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ATTrackingManager
```

#### Overview

This class presents an authorization request UI that asks a person for permission to access app-related data that your app can use to track a person or device across apps and websites (see [`requestTrackingAuthorization(completionHandler:)`](attrackingmanager/requesttrackingauthorization(completionhandler:).md)). You can check the result of prior requests with the [`trackingAuthorizationStatus`](attrackingmanager/trackingauthorizationstatus.md) property.

> ❗ **Important**: In the European Union, you can use [`requestTrackingAuthorization(usingExpandedInterface:additionalInformationAction:completionHandler:)`](attrackingmanager/requesttrackingauthorization(usingexpandedinterface:additionalinformationaction:completionhandler:).md) to add an optional Additional Information button to the prompt, which provides more details to assist people in their decision-making. The authorization Ul is a full-page sheet that supports rich-text formatting.

## Topics

### Requesting authorization
- [class func requestTrackingAuthorization(completionHandler: (ATTrackingManager.AuthorizationStatus) -> Void)](attrackingmanager/requesttrackingauthorization(completionhandler:).md)
  Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.
- [class func requestTrackingAuthorization(usingExpandedInterface: Bool, additionalInformationAction: (() -> Void)?, completionHandler: (ATTrackingManager.AuthorizationStatus) -> Void)](attrackingmanager/requesttrackingauthorization(usingexpandedinterface:additionalinformationaction:completionhandler:).md)
  Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.
### Determining tracking authorization status
- [class var trackingAuthorizationStatus: ATTrackingManager.AuthorizationStatus](attrackingmanager/trackingauthorizationstatus.md)
  A value that indicates the status of the app’s tracking authorization.
- [ATTrackingManager.AuthorizationStatus](attrackingmanager/authorizationstatus.md)
  A type that represents the tracking-authorization status of an app.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [NSUserTrackingUsageDescription](../bundleresources/information-property-list/nsusertrackingusagedescription.md)
  A message that explains the purpose for accessing data that an app can use to track a person or device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager)*