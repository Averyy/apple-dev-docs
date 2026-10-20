# requestAuthorization(_:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Type Method

Displays a user interface so that the user can authorize whether your app may view the media library’s contents.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func requestAuthorization(_ completionHandler: @escaping @Sendable (MPMediaLibraryAuthorizationStatus) -> Void)
```

```swift
class func requestAuthorization() async -> MPMediaLibraryAuthorizationStatus
```

```objc
+ (void) requestAuthorization:(void (^)(MPMediaLibraryAuthorizationStatus status)) completionHandler;
```

## Parameters

- `completionHandler`: A block that the system calls after the user chooses whether to authorize the app.

  - **status**: The status chosen by the user.

## See Also

### Getting the default media library
- [class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns whether the app can access the user’s media library.
- [enum MPMediaLibraryAuthorizationStatus](../mpmedialibraryauthorizationstatus.md)
  The list of possible states for authorization to access to the user’s media library.
- [class func `default`() -> MPMediaLibrary](./default%28%29.md)
  Returns an instance of the default media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/requestauthorization(_:))*