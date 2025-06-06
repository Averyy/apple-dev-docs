# playableContentManager(_:initializePlaybackQueueWithCompletionHandler:)

**Framework**: Mediaplayer  
**Kind**: method

Asks the delegate to prepare suggested content for playback.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func playableContentManagerInitializePlaybackQueue(_ contentManager: MPPlayableContentManager) async throws
```

#### Discussion

iOS calls this method when the user performs an action that, in context, might indicate intent to begin playing content using your app. For example, if the user frequently listens to audio content in your app with headphones while at a particular location, iOS might call this method upon plugging in headphones when the user is at that location. Your app responds by choosing appropriate content, performing any app-specific actions necessary to prepare the content for playback, and setting the [`nowPlayingInfo`](mpnowplayinginfocenter/nowplayinginfo.md) property of the shared [`MPNowPlayingInfoCenter`](mpnowplayinginfocenter.md) object to indicate to the user that this content is ready to play.

> **Note**:  Use this method only to suggest content. Don’t begin playback of content in this method—do so only upon receiving a `Play` command or when the playable content manager requests to play something else.

After preparing content for playing, call the provided `completionHandler` block with an argument of `nil`; or, if your app can’t prepare content, call the completion handler an error that indicates the reason.

## Parameters

- `contentManager`: The content manager that initiated the request.
- `completionHandler`: A block that the system calls after content is ready for playback. The block takes the following parameter:

## See Also

- [func playableContentManager(MPPlayableContentManager, initializePlaybackQueueWithContentItems: [Any]?, completionHandler: ((any Error)?) -> Void)](mpplayablecontentdelegate/playablecontentmanager(_:initializeplaybackqueuewithcontentitems:completionhandler:).md)
  Asks the delegate to prepare suggested content for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/playablecontentmanager(_:initializeplaybackqueuewithcompletionhandler:))*