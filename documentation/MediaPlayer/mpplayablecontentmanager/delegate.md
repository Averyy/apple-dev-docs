# delegate

**Framework**: Media Player  
**Kind**: property

A delegate that lets the media player manage the app’s playback queue.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any MPPlayableContentDelegate)? { get set }
```

#### Discussion

The delegate responds to external events that trigger a change in the media item that’s playing. An example of such an event would be choosing to play a song from a different album, or requesting suggested content to play next. The app must be able to respond to these events at any time.

To instead respond to events that affect the playback state of the currently playing item, use the [`MPRemoteCommandEvent`](mpremotecommandevent.md) class.

## See Also

- [protocol MPPlayableContentDelegate](mpplayablecontentdelegate.md)
  The protocol used to let external media players send playback commands to an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/delegate)*