# PHAuthorizationStatus.authorized

**Framework**: Photos  
**Kind**: case  
**Role**: Case

The user explicitly granted this app access to the photo library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case authorized
```

```c
PHAuthorizationStatusAuthorized
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)

## See Also

### Status Types
- [PHAuthorizationStatus.notDetermined](./notdetermined.md)
  The user hasn’t set the app’s authorization status.
- [PHAuthorizationStatus.restricted](./restricted.md)
  The app isn’t authorized to access the photo library, and the user can’t grant such permission.
- [PHAuthorizationStatus.denied](./denied.md)
  The user explicitly denied this app access to the photo library.
- [PHAuthorizationStatus.limited](./limited.md)
  The user authorized this app for limited photo library access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phauthorizationstatus/authorized)*