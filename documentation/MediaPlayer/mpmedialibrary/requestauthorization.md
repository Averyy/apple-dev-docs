# requestAuthorization(_:)

**Framework**: Media Player  
**Kind**: method

Displays a user interface so that the user can authorize whether your app may view the media library’s contents.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func requestAuthorization() async -> MPMediaLibraryAuthorizationStatus
```

## Parameters

- `completionHandler`: A block that the system calls after the user chooses whether to authorize the app.

## See Also

- [class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus](mpmedialibrary/authorizationstatus.md)
  Returns whether the app can access the user’s media library.
- [enum MPMediaLibraryAuthorizationStatus](mpmedialibraryauthorizationstatus.md)
  The list of possible states for authorization to access to the user’s media library.
- [class func `default`() -> MPMediaLibrary](mpmedialibrary/default.md)
  Returns an instance of the default media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/requestauthorization(_:))*