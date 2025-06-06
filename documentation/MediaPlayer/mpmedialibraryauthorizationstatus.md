# MPMediaLibraryAuthorizationStatus

**Framework**: Media Player  
**Kind**: enum

The list of possible states for authorization to access to the user’s media library.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum MPMediaLibraryAuthorizationStatus
```

## Topics

### Authorization statuses
- [MPMediaLibraryAuthorizationStatus.notDetermined](mpmedialibraryauthorizationstatus/notdetermined.md)
  The user hasn’t determined whether to authorize the use of their media library.
- [MPMediaLibraryAuthorizationStatus.denied](mpmedialibraryauthorizationstatus/denied.md)
  The app may not access the items in the user’s media library.
- [MPMediaLibraryAuthorizationStatus.restricted](mpmedialibraryauthorizationstatus/restricted.md)
  The app may access some of the content in the user’s media library.
- [MPMediaLibraryAuthorizationStatus.authorized](mpmedialibraryauthorizationstatus/authorized.md)
  Your app may access items in the user’s media library.
### Initializers
- [init?(rawValue: Int)](mpmedialibraryauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func requestAuthorization((MPMediaLibraryAuthorizationStatus) -> Void)](mpmedialibrary/requestauthorization(_:).md)
  Displays a user interface so that the user can authorize whether your app may view the media library’s contents.
- [class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus](mpmedialibrary/authorizationstatus.md)
  Returns whether the app can access the user’s media library.
- [class func `default`() -> MPMediaLibrary](mpmedialibrary/default.md)
  Returns an instance of the default media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus)*