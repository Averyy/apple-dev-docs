# authorizationStatus()

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Returns information about your app’s authorization to access the user’s photo library.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.13+ - Deprecated in 11.0
- tvOS 10.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`authorizationStatus(for:)`](./authorizationstatus%28for%29.md) instead.

## Declaration

```swift
class func authorizationStatus() -> PHAuthorizationStatus
```

```objc
+ (PHAuthorizationStatus) authorizationStatus;
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)

## Return Value

The current authorization status.

## See Also

### Verifying Authorization
- [class func authorizationStatus(for: PHAccessLevel) -> PHAuthorizationStatus](./authorizationstatus%28for%29.md)
  Returns the app’s authorization to access the user’s photo library for the specified access level.
- [class func requestAuthorization(for: PHAccessLevel, handler: (PHAuthorizationStatus) -> Void)](./requestauthorization%28for,handler%29.md)
  Prompts the user to grant the app permission to access the photo library.
- [enum PHAccessLevel](../phaccesslevel.md)
  The app’s level of access to the user’s photo library.
- [enum PHAuthorizationStatus](../phauthorizationstatus.md)
  Information about your app’s authorization to access the user’s photo library.
- [class func requestAuthorization((PHAuthorizationStatus) -> Void)](./requestauthorization%28_%29.md)
  Requests the user’s permission, if needed, to access the photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/authorizationstatus())*