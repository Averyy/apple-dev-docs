# AVAuthorizationStatus.notDetermined

**Framework**: AVFoundation  
**Kind**: case

A status that indicates the user hasn’t yet granted or denied authorization.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case notDetermined
```

## Mentions

- [Requesting authorization to capture and save media](requesting-authorization-to-capture-and-save-media.md)

#### Discussion

This is the default status prior to user to granting or denying recording priviledge to the app. Call [`requestAccess(for:completionHandler:)`](avcapturedevice/requestaccess(for:completionhandler:).md) to prompt the user for permission.

## See Also

- [AVAuthorizationStatus.restricted](avauthorizationstatus/restricted.md)
  A status that indicates the app isn’t permitted to use media capture devices.
- [AVAuthorizationStatus.denied](avauthorizationstatus/denied.md)
  A status that indicates the user has explicitly denied an app permission to capture media.
- [AVAuthorizationStatus.authorized](avauthorizationstatus/authorized.md)
  A status that indicates the user has explicitly granted an app permission to capture media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus/notdetermined)*