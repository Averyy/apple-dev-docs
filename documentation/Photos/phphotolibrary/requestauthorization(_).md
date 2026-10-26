# requestAuthorization(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Requests the user’s permission, if needed, to access the photo library.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.13+ - Deprecated in 27.2
- tvOS 10.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`requestAuthorization(for:handler:)`](./requestauthorization%28for,handler%29.md) instead.

## Declaration

```swift
class func requestAuthorization(_ handler: @escaping (PHAuthorizationStatus) -> Void)
```

```objc
+ (void) requestAuthorization:(void (^)(PHAuthorizationStatus status)) handler;
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)
- [Fetching Assets](../../PhotoKit/fetching-assets.md)

## Parameters

- `handler`: A block Photos calls upon determining your app’s authorization to access the photo library.

  The block takes a single parameter:

  - **status**: The current authorization status.

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
- [class func authorizationStatus() -> PHAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns information about your app’s authorization to access the user’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/requestauthorization(_:))*