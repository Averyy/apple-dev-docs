# MPMediaLibraryDidChangeNotification

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

Indicates the media library has changed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```c
extern NSString * const MPMediaLibraryDidChangeNotification;
```

## Discussion

When the system posts this notification, your app should reevaluate items or playlists that you previously cached.

## See Also

### Receiving notifications when the user’s library changes
- [func beginGeneratingLibraryChangeNotifications()](./mpmedialibrary/begingeneratinglibrarychangenotifications%28%29.md)
  Asks the media library to turn on notifications for whenever the library changes.
- [func endGeneratingLibraryChangeNotifications()](./mpmedialibrary/endgeneratinglibrarychangenotifications%28%29.md)
  Asks the media library to turn off notifications for whenever the library changes.
- [var lastModifiedDate: Date](./mpmedialibrary/lastmodifieddate.md)
  The calendar date on which the media library was last modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrarydidchangenotification)*