# PHAuthorizationStatus.restricted

**Framework**: Photos  
**Kind**: case  
**Role**: Case

The app isn’t authorized to access the photo library, and the user can’t grant such permission.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case restricted
```

```c
PHAuthorizationStatusRestricted
```

## Discussion

Parental controls or institutional configuration profiles can restrict the user’s ability to grant photo library access to an app.

## See Also

### Status Types
- [PHAuthorizationStatus.notDetermined](./notdetermined.md)
  The user hasn’t set the app’s authorization status.
- [PHAuthorizationStatus.denied](./denied.md)
  The user explicitly denied this app access to the photo library.
- [PHAuthorizationStatus.authorized](./authorized.md)
  The user explicitly granted this app access to the photo library.
- [PHAuthorizationStatus.limited](./limited.md)
  The user authorized this app for limited photo library access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phauthorizationstatus/restricted)*