# MPMediaLibrary

**Framework**: Media Player  
**Kind**: class

An object that represents the state of synced media items on a device.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMediaLibrary
```

#### Overview

A user may sync their device, changing the contents on the device, while your app is running. You can use the notification provided by this class to ensure that your app’s cache of the user’s library is up-to-date.

To retrieve media items from the media library, build a custom query as described in [`MPMediaPropertyPredicate`](mpmediapropertypredicate.md) and [`MPMediaQuery`](mpmediaquery.md).

## Topics

### Getting the default media library
- [class func requestAuthorization((MPMediaLibraryAuthorizationStatus) -> Void)](mpmedialibrary/requestauthorization(_:).md)
  Displays a user interface so that the user can authorize whether your app may view the media library’s contents.
- [class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus](mpmedialibrary/authorizationstatus.md)
  Returns whether the app can access the user’s media library.
- [enum MPMediaLibraryAuthorizationStatus](mpmedialibraryauthorizationstatus.md)
  The list of possible states for authorization to access to the user’s media library.
- [class func `default`() -> MPMediaLibrary](mpmedialibrary/default.md)
  Returns an instance of the default media library.
### Receiving notifications when the user’s library changes
- [func beginGeneratingLibraryChangeNotifications()](mpmedialibrary/begingeneratinglibrarychangenotifications.md)
  Asks the media library to turn on notifications for whenever the library changes.
- [func endGeneratingLibraryChangeNotifications()](mpmedialibrary/endgeneratinglibrarychangenotifications.md)
  Asks the media library to turn off notifications for whenever the library changes.
- [var lastModifiedDate: Date](mpmedialibrary/lastmodifieddate.md)
  The calendar date on which the media library was last modified.
### Retrieving a playlist from the media library
- [func getPlaylist(with: UUID, creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler: (MPMediaPlaylist?, (any Error)?) -> Void)](mpmedialibrary/getplaylist(with:creationmetadata:completionhandler:).md)
  Retrieves an app maintained existing playlist or creates a new playlist when no playlist exists.
### Adding an item to the media library
- [func addItem(withProductID: String, completionHandler: (([MPMediaEntity], (any Error)?) -> Void)?)](mpmedialibrary/additem(withproductid:completionhandler:).md)
  Adds the designated item to the user’s music library.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary)*