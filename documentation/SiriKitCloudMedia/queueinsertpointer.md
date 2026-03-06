# QueueInsertPointer

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Instructions for editing the current playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object QueueInsertPointer
```

## Properties

- `afterIdentifier` (ContentIdentifier): The client inserts the new queue segment after the content with this identifier.
- `replace` (boolean): If this value is `true`, the client discards all of the current queue’s content after the item that `afterIdentifier` specifies.

## See Also

- [object Queue](queue.md)
  A sequence of media content for playback, with links to the previous and next segments of a full playback queue.
- [type QueueIdentifier](queueidentifier.md)
  A stable identifier for a playback queue.
- [object QueuePlayPointer](queueplaypointer.md)
  A position within a playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/queueinsertpointer)*