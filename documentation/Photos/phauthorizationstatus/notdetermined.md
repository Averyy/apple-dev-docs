# PHAuthorizationStatus.notDetermined

**Framework**: Photos  
**Kind**: case  
**Role**: Case

The user hasn’t set the app’s authorization status.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case notDetermined
```

```c
PHAuthorizationStatusNotDetermined
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)

#### Discussion

The framework automatically prompts for user authorization when you attempt to fetch assets, asset collections, or collection lists. Alternatively, you may call the [`requestAuthorization(for:handler:)`](../phphotolibrary/requestauthorization%28for,handler%29.md) method to prompt the user for authorization at a time of your choosing.

## See Also

### Status Types
- [PHAuthorizationStatus.restricted](./restricted.md)
  The app isn’t authorized to access the photo library, and the user can’t grant such permission.
- [PHAuthorizationStatus.denied](./denied.md)
  The user explicitly denied this app access to the photo library.
- [PHAuthorizationStatus.authorized](./authorized.md)
  The user explicitly granted this app access to the photo library.
- [PHAuthorizationStatus.limited](./limited.md)
  The user authorized this app for limited photo library access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phauthorizationstatus/notdetermined)*