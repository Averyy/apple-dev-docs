# authorizationStatus()

**Framework**: Media Player  
**Kind**: method  
**Role**: Type Method

Returns whether the app can access the user’s media library.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus
```

```objc
+ (MPMediaLibraryAuthorizationStatus) authorizationStatus;
```

#### Return Value

The status representing whether the app has access to the user’s media library.

## See Also

### Getting the default media library
- [class func requestAuthorization((MPMediaLibraryAuthorizationStatus) -> Void)](./requestauthorization%28_%29.md)
  Displays a user interface so that the user can authorize whether your app may view the media library’s contents.
- [enum MPMediaLibraryAuthorizationStatus](../mpmedialibraryauthorizationstatus.md)
  The list of possible states for authorization to access to the user’s media library.
- [class func `default`() -> MPMediaLibrary](./default%28%29.md)
  Returns an instance of the default media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/authorizationstatus())*