# QueuePlayPointer

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A position within a playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object QueuePlayPointer
```

## Properties

- `contentIdentifier` (ContentIdentifier): The current content.

  **Minimum Length**: `1`; **Maximum Length**: `1000`
- `offsetInMillis` (int64): The number of milliseconds into the playback progress of the current content. It’s the point where playback resumes after pausing.

## See Also

### Creating or Updating a Playback Queue
- [object Queue](./queue.md)
  A sequence of media content for playback, with links to the previous and next segments of a full playback queue.
- [type QueueIdentifier](./queueidentifier.md)
  A stable identifier for a playback queue.
- [object QueueInsertPointer](./queueinsertpointer.md)
  Instructions for editing the current playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/queueplaypointer)*