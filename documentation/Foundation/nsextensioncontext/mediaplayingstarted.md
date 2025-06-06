# mediaPlayingStarted()

**Framework**: Foundation  
**Kind**: method

Tells the system that the Notification Content app extension began playing a media file.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func mediaPlayingStarted()
```

#### Discussion

In your Notification Content app extension code, call this method when you programmatically begin playing a media file. When called, the system updates the appearance of the media playback button displayed in the notification content extension’s interface. For more information about implementing a notification content extension, see [`UNNotificationContentExtension`](https://developer.apple.com/documentation/UserNotificationsUI/UNNotificationContentExtension).

## See Also

- [func mediaPlayingPaused()](nsextensioncontext/mediaplayingpaused.md)
  Tells the system that the Notification Content app extension stopped playing a media file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/mediaplayingstarted())*