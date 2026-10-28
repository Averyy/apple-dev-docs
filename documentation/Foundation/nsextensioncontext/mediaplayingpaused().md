# mediaPlayingPaused()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the system that the Notification Content app extension stopped playing a media file.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func mediaPlayingPaused()
```

```objc
- (void) mediaPlayingPaused;
```

## Discussion

In your Notification Content app extension code, call this method when you programmatically stop playing a media file. When called, the system updates the appearance of the media playback button displayed in the notification content extension’s interface. For more information about implementing a notification content extension, see [`UNNotificationContentExtension`](../../UserNotificationsUI/unnotificationcontentextension.md).

## See Also

### Controlling media playback in notification content extensions
- [func mediaPlayingStarted()](./mediaplayingstarted%28%29.md)
  Tells the system that the Notification Content app extension began playing a media file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/mediaplayingpaused())*