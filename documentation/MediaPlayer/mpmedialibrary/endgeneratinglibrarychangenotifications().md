# endGeneratingLibraryChangeNotifications()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Asks the media library to turn off notifications for whenever the library changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func endGeneratingLibraryChangeNotifications()
```

```objc
- (void) endGeneratingLibraryChangeNotifications;
```

## Discussion

To completely turn off notifications, you must call this method the same number of times that you called [`beginGeneratingLibraryChangeNotifications()`](./begingeneratinglibrarychangenotifications%28%29.md).

## See Also

### Receiving notifications when the user’s library changes
- [func beginGeneratingLibraryChangeNotifications()](./begingeneratinglibrarychangenotifications%28%29.md)
  Asks the media library to turn on notifications for whenever the library changes.
- [var lastModifiedDate: Date](./lastmodifieddate.md)
  The calendar date on which the media library was last modified.
- [MPMediaLibraryDidChangeNotification](../mpmedialibrarydidchangenotification.md)
  Indicates the media library has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/endgeneratinglibrarychangenotifications())*