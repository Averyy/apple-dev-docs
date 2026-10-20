# default()

**Framework**: Media Player  
**Kind**: method  
**Role**: Type Method

Returns an instance of the default media library.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> MPMediaLibrary
```

```objc
+ (MPMediaLibrary *) defaultMediaLibrary;
```

#### Return Value

The user’s default media library.

## See Also

### Getting the default media library
- [class func requestAuthorization((MPMediaLibraryAuthorizationStatus) -> Void)](./requestauthorization%28_%29.md)
  Displays a user interface so that the user can authorize whether your app may view the media library’s contents.
- [class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns whether the app can access the user’s media library.
- [enum MPMediaLibraryAuthorizationStatus](../mpmedialibraryauthorizationstatus.md)
  The list of possible states for authorization to access to the user’s media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/default())*