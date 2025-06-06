# playableContentManager(_:didUpdate:)

**Framework**: Media Player  
**Kind**: method

Notifies the delegate that the playable content manager’s context information has changed.

**Availability**:
- iOS 8.4+
- iPadOS 8.4+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func playableContentManager(_ contentManager: MPPlayableContentManager, didUpdate context: MPPlayableContentManagerContext)
```

#### Discussion

A playable content manager’s context provides information about the current playback environment of an external media player, such as whether that media player limits the amount of content to display. Use the content manager’s `context` property to examine attributes of the new context after the change.

## Parameters

- `contentManager`: The content manager whose current context has changed.
- `context`: The new context of the content manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/playablecontentmanager(_:didupdate:))*