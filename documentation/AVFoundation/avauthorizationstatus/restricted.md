# AVAuthorizationStatus.restricted

**Framework**: AVFoundation  
**Kind**: case

A status that indicates the app isn’t permitted to use media capture devices.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.14+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case restricted
```

#### Discussion

This status occurs when a user can’t change the authorization status, possibly due to the system imposing restrictions like parental controls.

## See Also

- [AVAuthorizationStatus.notDetermined](avauthorizationstatus/notdetermined.md)
  A status that indicates the user hasn’t yet granted or denied authorization.
- [AVAuthorizationStatus.denied](avauthorizationstatus/denied.md)
  A status that indicates the user has explicitly denied an app permission to capture media.
- [AVAuthorizationStatus.authorized](avauthorizationstatus/authorized.md)
  A status that indicates the user has explicitly granted an app permission to capture media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avauthorizationstatus/restricted)*