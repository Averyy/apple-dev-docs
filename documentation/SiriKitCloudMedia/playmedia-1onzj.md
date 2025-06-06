# Get a Media Queue

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest

Provide a playback queue from a successfully processed play media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

#### Discussion

There isn’t a default path for this endpoint. Specify the URL for this endpoint in your [`ExtensionConfig.Media.Queues.PlayMedia`](extensionconfig/media-data.dictionary/queues-data.dictionary/playmedia-data.dictionary.md) object.

## Topics

### Receiving a Queue Request
- [object PlayMediaRequest](playmediarequest.md)
  A request for a media playback queue.
### Creating or Updating a Playback Queue
- [object Queue](queue.md)
  A sequence of media content for playback, with links to the previous and next segments of a full playback queue.
- [type QueueIdentifier](queueidentifier.md)
  A stable identifier for a playback queue.
- [object QueueInsertPointer](queueinsertpointer.md)
  Instructions for editing the current playback queue.
- [object QueuePlayPointer](queueplaypointer.md)
  A position within a playback queue.
### Providing Queue Items
- [object Content](content.md)
  A description of a piece of playback content, such as a song, podcast, or advertisement.
- [type ContentIdentifier](contentidentifier.md)
  An identifier for a song, podcast, ad, or other media content. The identifier must be stable and unique within a queue.
- [object ContentAttributes](contentattributes.md)
  Metadata for some media content.
### Customizing Playback Controls
- [object QueueControlMapping](queuecontrolmapping.md)
  A dictionary of configuration names and the media controls they permit.
- [object PlayMediaControl](playmediacontrol.md)
  A configuration for permitted user interactions and other player behaviors during playback.
- [type PlayMediaControlScheme](playmediacontrolscheme.md)
  Default playback controls and settings for common content types.
- [object PlayMediaControlCommandSet](playmediacontrolcommandset.md)
  A set of modifications to apply to the default set of available playback controls.

## Request Body

A [`UserActivity`](useractivity.md) and constraints for the queue your service provides.

## See Also

- [Process a Play Media Intent](playmedia-1g2o9.md)
  Interpret the user’s request to play a media item, and provide instructions to access a corresponding playback queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmedia-1onzj)*