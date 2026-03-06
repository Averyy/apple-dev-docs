# Content

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A description of a piece of playback content, such as a song, podcast, or advertisement.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object Content
```

#### Discussion

If you provide a `playIndex` for any content, you must provide a `playIndex` for each `Content` object in the [`Queue`](queue.md). These indices must have a strong ordering. If your `Queue` also provides a `contentItemsCount`, the client may use these values to display or announce playback progress to the user. For example, if a queue’s `contentItemsCount` is 7 and the `playIndex` for the current content is 3, the client might present the playback progress as *3 of 7*.

## Properties

- `attributes` (ContentAttributes): The content’s metadata.
- `control` (string): The set of controls the user may access while the client is playing this content. Define controls in the [`QueueControlMapping`](queuecontrolmapping.md) object.
- `identifier` (ContentIdentifier) *(required)*: A stable identifier for this content. Content identifiers must be unique within a [`Queue`](queue.md). Minimum length: `1`. Maximum Length: `1000`.
- `isLive` (boolean): `true` for a live stream, `false` for prerecorded content.
- `playIndex` (uint64): This content’s position within the playback queue.
- `url` (string): A URL to request the audio or video data.

## See Also

- [type ContentIdentifier](contentidentifier.md)
  An identifier for a song, podcast, ad, or other media content. The identifier must be stable and unique within a queue.
- [object ContentAttributes](contentattributes.md)
  Metadata for some media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/content)*