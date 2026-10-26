# PHAuthorizationStatus

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Information about your app’s authorization to access the user’s photo library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHAuthorizationStatus
```

```c
enum PHAuthorizationStatus : NSInteger;
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)

## Topics

### Status Types
- [PHAuthorizationStatus.notDetermined](./phauthorizationstatus/notdetermined.md)
  The user hasn’t set the app’s authorization status.
- [PHAuthorizationStatus.restricted](./phauthorizationstatus/restricted.md)
  The app isn’t authorized to access the photo library, and the user can’t grant such permission.
- [PHAuthorizationStatus.denied](./phauthorizationstatus/denied.md)
  The user explicitly denied this app access to the photo library.
- [PHAuthorizationStatus.authorized](./phauthorizationstatus/authorized.md)
  The user explicitly granted this app access to the photo library.
- [PHAuthorizationStatus.limited](./phauthorizationstatus/limited.md)
  The user authorized this app for limited photo library access.
### Initializers
- [init?(rawValue: Int)](./phauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Verifying Authorization
- [class func authorizationStatus(for: PHAccessLevel) -> PHAuthorizationStatus](./phphotolibrary/authorizationstatus%28for%29.md)
  Returns the app’s authorization to access the user’s photo library for the specified access level.
- [class func requestAuthorization(for: PHAccessLevel, handler: (PHAuthorizationStatus) -> Void)](./phphotolibrary/requestauthorization%28for,handler%29.md)
  Prompts the user to grant the app permission to access the photo library.
- [enum PHAccessLevel](./phaccesslevel.md)
  The app’s level of access to the user’s photo library.
- [class func authorizationStatus() -> PHAuthorizationStatus](./phphotolibrary/authorizationstatus%28%29.md)
  Returns information about your app’s authorization to access the user’s photo library.
- [class func requestAuthorization((PHAuthorizationStatus) -> Void)](./phphotolibrary/requestauthorization%28_%29.md)
  Requests the user’s permission, if needed, to access the photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phauthorizationstatus)*