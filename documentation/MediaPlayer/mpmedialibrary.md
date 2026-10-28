# MPMediaLibrary

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPMediaLibrary : NSObject
```

## Overview

A user may sync their device, changing the contents on the device, while your app is running. You can use the notification provided by this class to ensure that your app’s cache of the user’s library is up-to-date.

To retrieve media items from the media library, build a custom query as described in [`MPMediaPropertyPredicate`](./mpmediapropertypredicate.md) and [`MPMediaQuery`](./mpmediaquery.md).

## Topics

### Getting the default media library
- [class func requestAuthorization((MPMediaLibraryAuthorizationStatus) -> Void)](./mpmedialibrary/requestauthorization%28_%29.md)
  Displays a user interface so that the user can authorize whether your app may view the media library’s contents.
- [class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus](./mpmedialibrary/authorizationstatus%28%29.md)
  Returns whether the app can access the user’s media library.
- [enum MPMediaLibraryAuthorizationStatus](./mpmedialibraryauthorizationstatus.md)
  The list of possible states for authorization to access to the user’s media library.
- [class func `default`() -> MPMediaLibrary](./mpmedialibrary/default%28%29.md)
  Returns an instance of the default media library.
### Receiving notifications when the user’s library changes
- [func beginGeneratingLibraryChangeNotifications()](./mpmedialibrary/begingeneratinglibrarychangenotifications%28%29.md)
  Asks the media library to turn on notifications for whenever the library changes.
- [func endGeneratingLibraryChangeNotifications()](./mpmedialibrary/endgeneratinglibrarychangenotifications%28%29.md)
  Asks the media library to turn off notifications for whenever the library changes.
- [var lastModifiedDate: Date](./mpmedialibrary/lastmodifieddate.md)
  The calendar date on which the media library was last modified.
- [MPMediaLibraryDidChangeNotification](./mpmedialibrarydidchangenotification.md)
  Indicates the media library has changed.
### Retrieving a playlist from the media library
- [func getPlaylist(with: UUID, creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler: (MPMediaPlaylist?, (any Error)?) -> Void)](./mpmedialibrary/getplaylist%28with,creationmetadata,completionhandler%29.md)
  Retrieves an app maintained existing playlist or creates a new playlist when no playlist exists.
### Adding an item to the media library
- [func addItem(withProductID: String, completionHandler: (([MPMediaEntity], (any Error)?) -> Void)?)](./mpmedialibrary/additem%28withproductid,completionhandler%29.md)
  Adds the designated item to the user’s music library.
### Initializers
- [init?(coder: NSCoder)](./mpmedialibrary/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary)*