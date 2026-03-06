# QueuePlayPointer

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A position within a playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object QueuePlayPointer
```

## Properties

- `contentIdentifier` (ContentIdentifier): The current content.
- `offsetInMillis` (int64): The number of milliseconds into the playback progress of the current content. It’s the point where playback resumes after pausing.

## See Also

- [object Queue](queue.md)
  A sequence of media content for playback, with links to the previous and next segments of a full playback queue.
- [type QueueIdentifier](queueidentifier.md)
  A stable identifier for a playback queue.
- [object QueueInsertPointer](queueinsertpointer.md)
  Instructions for editing the current playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/queueplaypointer)*