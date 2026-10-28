# MPMediaPlaybackIsPreparedToPlayDidChangeNotification

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

Indicates that the prepared to play status of the media player has changed.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS
- tvOS - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```c
extern NSString * const MPMediaPlaybackIsPreparedToPlayDidChangeNotification;
```

## Discussion

Posted upon change in the prepared-to-play state of an object conforming to the [`MPMediaPlayback`](./mpmediaplayback.md) protocol. The object whose state has changed is available as the object associated with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaybackispreparedtoplaydidchangenotification)*