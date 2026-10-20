# lastModifiedDate

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The calendar date on which the media library was last modified.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var lastModifiedDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * lastModifiedDate;
```

## See Also

### Receiving notifications when the user’s library changes
- [func beginGeneratingLibraryChangeNotifications()](./begingeneratinglibrarychangenotifications%28%29.md)
  Asks the media library to turn on notifications for whenever the library changes.
- [func endGeneratingLibraryChangeNotifications()](./endgeneratinglibrarychangenotifications%28%29.md)
  Asks the media library to turn off notifications for whenever the library changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/lastmodifieddate)*