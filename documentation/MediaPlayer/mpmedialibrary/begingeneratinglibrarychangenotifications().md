# beginGeneratingLibraryChangeNotifications()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Asks the media library to turn on notifications for whenever the library changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func beginGeneratingLibraryChangeNotifications()
```

```objc
- (void) beginGeneratingLibraryChangeNotifications;
```

#### Discussion

This method is nestable, that is, you can call it multiple times. To turn off notifications, call [`endGeneratingLibraryChangeNotifications()`](./endgeneratinglibrarychangenotifications%28%29.md) the same number of times that you called [`beginGeneratingLibraryChangeNotifications()`](./begingeneratinglibrarychangenotifications%28%29.md).

## See Also

### Receiving notifications when the user’s library changes
- [func endGeneratingLibraryChangeNotifications()](./endgeneratinglibrarychangenotifications%28%29.md)
  Asks the media library to turn off notifications for whenever the library changes.
- [var lastModifiedDate: Date](./lastmodifieddate.md)
  The calendar date on which the media library was last modified.
- [MPMediaLibraryDidChangeNotification](../mpmedialibrarydidchangenotification.md)
  Indicates the media library has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/begingeneratinglibrarychangenotifications())*