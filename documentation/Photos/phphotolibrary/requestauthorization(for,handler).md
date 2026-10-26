# requestAuthorization(for:handler:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Prompts the user to grant the app permission to access the photo library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func requestAuthorization(for accessLevel: PHAccessLevel, handler: @escaping @Sendable (PHAuthorizationStatus) -> Void)
```

```swift
class func requestAuthorization(for accessLevel: PHAccessLevel) async -> PHAuthorizationStatus
```

```objc
+ (void) requestAuthorizationForAccessLevel:(PHAccessLevel) accessLevel handler:(void (^)(PHAuthorizationStatus status)) handler;
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)
- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

#### Discussion

For more information about accessing the user’s Photos library, see [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md).

## Parameters

- `accessLevel`: The access level to request.
- `handler`: The callback the system invokes when it’s made a determination of the app’s status.

## See Also

### Verifying Authorization
- [class func authorizationStatus(for: PHAccessLevel) -> PHAuthorizationStatus](./authorizationstatus%28for%29.md)
  Returns the app’s authorization to access the user’s photo library for the specified access level.
- [enum PHAccessLevel](../phaccesslevel.md)
  The app’s level of access to the user’s photo library.
- [enum PHAuthorizationStatus](../phauthorizationstatus.md)
  Information about your app’s authorization to access the user’s photo library.
- [class func authorizationStatus() -> PHAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns information about your app’s authorization to access the user’s photo library.
- [class func requestAuthorization((PHAuthorizationStatus) -> Void)](./requestauthorization%28_%29.md)
  Requests the user’s permission, if needed, to access the photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/requestauthorization(for:handler:))*