# endGeneratingLibraryChangeNotifications()

**Framework**: Media Player  
**Kind**: method

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

#### Discussion

To completely turn off notifications, you must call this method the same number of times that you called [`beginGeneratingLibraryChangeNotifications()`](mpmedialibrary/begingeneratinglibrarychangenotifications().md).

## See Also

- [func beginGeneratingLibraryChangeNotifications()](mpmedialibrary/begingeneratinglibrarychangenotifications.md)
  Asks the media library to turn on notifications for whenever the library changes.
- [var lastModifiedDate: Date](mpmedialibrary/lastmodifieddate.md)
  The calendar date on which the media library was last modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/endgeneratinglibrarychangenotifications())*