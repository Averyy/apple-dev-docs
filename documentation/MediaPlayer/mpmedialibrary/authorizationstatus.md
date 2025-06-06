# authorizationStatus()

**Framework**: Media Player  
**Kind**: method

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

#### Return Value

The status representing whether the app has access to the user’s media library.

## See Also

- [class func requestAuthorization((MPMediaLibraryAuthorizationStatus) -> Void)](mpmedialibrary/requestauthorization(_:).md)
  Displays a user interface so that the user can authorize whether your app may view the media library’s contents.
- [enum MPMediaLibraryAuthorizationStatus](mpmedialibraryauthorizationstatus.md)
  The list of possible states for authorization to access to the user’s media library.
- [class func `default`() -> MPMediaLibrary](mpmedialibrary/default.md)
  Returns an instance of the default media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/authorizationstatus())*