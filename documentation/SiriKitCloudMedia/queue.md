# Queue

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A sequence of media content for playback, with links to the previous and next segments of a full playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object Queue
```

#### Discussion

A `Queue` object is a segment of the full playback queue. You may instruct the client to insert a `Queue` object into its current playback queue, or replace it entirely.

The strings you provide in `nextContentUrl` and `previousContentUrl` may include tokens for the client to replace at runtime. Escape the brackets delimiting the tokens as `%7B` and `%7D`. The client URL encodes its replacement values. If the client doesn’t have a current value for a token, the client replaces the token with an empty string.

The client supports the following tokens:

## See Also

- [type QueueIdentifier](queueidentifier.md)
  A stable identifier for a playback queue.
- [object QueueInsertPointer](queueinsertpointer.md)
  Instructions for editing the current playback queue.
- [object QueuePlayPointer](queueplaypointer.md)
  A position within a playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/queue)*