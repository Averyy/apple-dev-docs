# authorizationStatus(for:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Returns the app’s authorization to access the user’s photo library for the specified access level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func authorizationStatus(for accessLevel: PHAccessLevel) -> PHAuthorizationStatus
```

```objc
+ (PHAuthorizationStatus) authorizationStatusForAccessLevel:(PHAccessLevel) accessLevel;
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)

## Return Value

The app’s authorization status.

## Discussion

For more information about accessing the user’s Photos library, see [Delivering an Enhanced Privacy Experience in Your Photos App](../../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md).

## Parameters

- `accessLevel`: The access level for which to determine the app’s authorization status.

## See Also

### Verifying Authorization
- [class func requestAuthorization(for: PHAccessLevel, handler: (PHAuthorizationStatus) -> Void)](./requestauthorization%28for,handler%29.md)
  Prompts the user to grant the app permission to access the photo library.
- [enum PHAccessLevel](../phaccesslevel.md)
  The app’s level of access to the user’s photo library.
- [enum PHAuthorizationStatus](../phauthorizationstatus.md)
  Information about your app’s authorization to access the user’s photo library.
- [class func authorizationStatus() -> PHAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns information about your app’s authorization to access the user’s photo library.
- [class func requestAuthorization((PHAuthorizationStatus) -> Void)](./requestauthorization%28_%29.md)
  Requests the user’s permission, if needed, to access the photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/authorizationstatus(for:))*