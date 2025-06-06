# authorizationStatus(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns an authorization status that indicates whether the user grants the app permission to capture media of a particular type.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func authorizationStatus(for mediaType: AVMediaType) -> AVAuthorizationStatus
```

## Mentions

- [Requesting authorization to capture and save media](requesting-authorization-to-capture-and-save-media.md)

#### Return Value

An authorization status value.

#### Discussion

A user must explicitly grant your app access to record audio or video. Call this method to determine your app’s current authorization status. If it returns a value of [`AVAuthorizationStatus.notDetermined`](avauthorizationstatus/notdetermined.md), call [`requestAccess(for:completionHandler:)`](avcapturedevice/requestaccess(for:completionhandler:).md) to prompt the user for capture permission.

After the user grants permission, the system remembers their choice and doesn’t prompt them again. However, a user can change their choice at any time in the Settings app.

> **Note**:  If a user has denied your app recording permission, or hasn’t yet responded to the permission prompt, audio recordings contain only silence and video recordings contain only black frames.

 If a user has denied your app recording permission, or hasn’t yet responded to the permission prompt, audio recordings contain only silence and video recordings contain only black frames.

## Parameters

- `mediaType`: A media type for which to check the authorization status. The supported media types are   and  .

## See Also

- [class func requestAccess(for: AVMediaType, completionHandler: (Bool) -> Void)](avcapturedevice/requestaccess(for:completionhandler:).md)
  Requests the user’s permission to allow the app to capture media of a particular type.
- [enum AVAuthorizationStatus](avauthorizationstatus.md)
  Constants that indicate the status of an app’s authorization to capture media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/authorizationstatus(for:))*