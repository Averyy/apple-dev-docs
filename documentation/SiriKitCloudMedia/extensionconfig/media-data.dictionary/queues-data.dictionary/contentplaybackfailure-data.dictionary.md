# ExtensionConfig.Media.Queues.ContentPlaybackFailure

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

Configuration details for your service’s content playback failure endpoint.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object ExtensionConfig.Media.Queues.ContentPlaybackFailure
```

## Properties

- `url` (string) *(required)*: The relative path for the client to access the `contentPlaybackFailure` endpoint. For more information, see `contentPlaybackFailure`.

  **Default**: `/queues/contentPlaybackFailure`; **Minimum Length**: `1`; **Maximum Length**: `4000`

## See Also

### Requiring Headers and Specifying Paths for Specific Queue Endpoints
- [object ExtensionConfig.Media.Queues.PlayMedia](./playmedia-data.dictionary.md)
  Configuration details for your service’s media playback queue.
- [object ExtensionConfig.Media.Queues.UpdateActivity](./updateactivity-data.dictionary.md)
  Configuration details for your service’s update activity endpoint.
- [object ExtensionConfig.Media.Queues.ContentProtectionKey](./contentprotectionkey-data.dictionary.md)
  Configuration details for your service’s content protection key endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig/media-data.dictionary/queues-data.dictionary/contentplaybackfailure-data.dictionary)*