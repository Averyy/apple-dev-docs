# playableContentManager(_:initiatePlaybackOfContentItemAt:completionHandler:)

**Framework**: Media Player  
**Kind**: method

Asks the delegate to begin playback of the specified content item.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func playableContentManager(_ contentManager: MPPlayableContentManager, initiatePlaybackOfContentItemAt indexPath: IndexPath) async throws
```

#### Discussion

The system calls this method when a media player interface needs to play a media item. Your app responds by beginning playback of the requested media item. After beginning playback, call the provided `completionHandler` block with an argument of `nil`; or, if your app can’t begin playback, call the completion handler with an error that indicates the reason.

> ❗ **Important**:  Don’t automatically restart playback when the media item is already playing. In most cases, it’s better for your app to do nothing and continue to play the current media item.

 Don’t automatically restart playback when the media item is already playing. In most cases, it’s better for your app to do nothing and continue to play the current media item.

## Parameters

- `contentManager`: The content manager that initiated the request.
- `indexPath`: The index for the indicated item.
- `completionHandler`: A block that the system calls after initiating a playback request. The block takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/playablecontentmanager(_:initiateplaybackofcontentitemat:completionhandler:))*