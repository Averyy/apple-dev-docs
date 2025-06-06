# beginGeneratingLibraryChangeNotifications()

**Framework**: Media Player  
**Kind**: method

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

#### Discussion

This method is nestable, that is, you can call it multiple times. To turn off notifications, call [`endGeneratingLibraryChangeNotifications()`](mpmedialibrary/endgeneratinglibrarychangenotifications().md) the same number of times that you called [`beginGeneratingLibraryChangeNotifications()`](mpmedialibrary/begingeneratinglibrarychangenotifications().md).

## See Also

- [func endGeneratingLibraryChangeNotifications()](mpmedialibrary/endgeneratinglibrarychangenotifications.md)
  Asks the media library to turn off notifications for whenever the library changes.
- [var lastModifiedDate: Date](mpmedialibrary/lastmodifieddate.md)
  The calendar date on which the media library was last modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/begingeneratinglibrarychangenotifications())*