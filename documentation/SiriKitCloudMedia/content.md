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

If you provide a `playIndex` for any content, you must provide a `playIndex` for each `Content` object in the [`Queue`](queue.md). These indices must have a strong ordering. If your `Queue` also provides a `contentItemsCount`, the client may use these values to display or announce playback progress to the user. For example, if a queue’s `contentItemsCount` is 7 and the `playIndex` for the current content is 3, the client might present the playback progress as .

## See Also

- [type ContentIdentifier](contentidentifier.md)
  An identifier for a song, podcast, ad, or other media content. The identifier must be stable and unique within a queue.
- [object ContentAttributes](contentattributes.md)
  Metadata for some media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/content)*