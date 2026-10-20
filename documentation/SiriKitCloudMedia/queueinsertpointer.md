# QueueInsertPointer

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

Instructions for editing the current playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object QueueInsertPointer
```

## Properties

- `afterIdentifier` (ContentIdentifier): The client inserts the new queue segment after the content with this identifier.

  **Minimum Length**: `1`; **Maximum Length**: `1000`
- `replace` (boolean): If this value is `true`, the client discards all of the current queue’s content after the item that `afterIdentifier` specifies.

  **Default**: `false`

## See Also

### Creating or Updating a Playback Queue
- [object Queue](./queue.md)
  A sequence of media content for playback, with links to the previous and next segments of a full playback queue.
- [type QueueIdentifier](./queueidentifier.md)
  A stable identifier for a playback queue.
- [object QueuePlayPointer](./queueplaypointer.md)
  A position within a playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/queueinsertpointer)*