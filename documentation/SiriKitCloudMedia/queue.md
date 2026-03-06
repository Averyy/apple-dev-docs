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

- **`{activity}`**: The `persistentIdentifier` of the client’s current [`UserActivity`](useractivity.md).
- **`{queue}`**: The [`QueueIdentifier`](queueidentifier.md) for the current queue.
- **`{content}`**: The [`ContentIdentifier`](contentidentifier.md) for the current content.
- **`{offset}`**: The progress, in milliseconds, within the current content.
- **`{firstContent}`**: The [`ContentIdentifier`](contentidentifier.md) for the first item in the current queue segment.
- **`{lastContent}`**: The [`ContentIdentifier`](contentidentifier.md) for the last item in the current queue segment.
- **`{transition}`**: A [`QueueActivityReportEvent`](queueactivityreportevent.md) that indicates how the client transitions to the current content.
- **`{version}`**: The version of the `SiriKitMediaAPI` library the client uses.

## Properties

- `content` ([Content]) *(required)*: A sequence of songs, podcasts, ads, or other media content for the client to play.
- `contentItemsCount` (uint32): The number of pieces of content in the full playback queue.
- `controls` (QueueControlMapping) *(required)*: The control schemes that are relevant while playing this content.
- `identifier` (QueueIdentifier) *(required)*: The identifier for the full playback queue. If you want this `Queue` to replace the client’s current playback queue, provide a new value.
- `insertPointer` (QueueInsertPointer): The position in the client’s full playback queue to insert this queue segment.
- `nextContentUrl` (string): A URL pattern to request the next queue segment. Omit this field for the last segment in a queue, or provide a pointer to the first segment of the queue to provide a repeat mode.
- `playPointer` (QueuePlayPointer): The [`ContentIdentifier`](contentidentifier.md) for the content to play next. Omit this field if you want the client to start at the beginning of the queue segment.
- `prerollSeconds` (double): The number of seconds before the end of this queue for the client to request the next queue segment. The client may not be able to honor this hint if the user skips ahead into the last `prerollSeconds` of the current queue segment.
- `previousContentUrl` (string): A URL pattern to request the previous queue segment. Omit this field for the first segment in a queue, or provide a pointer to the last segment of the queue to provide a repeat mode.
- `skipsRemaining` (uint32): For content with the `internetRadio` value in [`PlayMediaControlScheme`](playmediacontrolscheme.md), the number of times the user can skip to another track during this queue segment.
- `version` (string) *(required)*: The version of the `SiriKitMediaAPI` library the client uses.

## See Also

- [type QueueIdentifier](queueidentifier.md)
  A stable identifier for a playback queue.
- [object QueueInsertPointer](queueinsertpointer.md)
  Instructions for editing the current playback queue.
- [object QueuePlayPointer](queueplaypointer.md)
  A position within a playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/queue)*