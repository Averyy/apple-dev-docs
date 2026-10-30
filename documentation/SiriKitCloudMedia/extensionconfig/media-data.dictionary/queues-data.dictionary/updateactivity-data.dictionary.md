# ExtensionConfig.Media.Queues.UpdateActivity

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

Configuration details for your service’s update activity endpoint.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object ExtensionConfig.Media.Queues.UpdateActivity
```

## Topics

### Requiring Headers
- [object ExtensionConfig.Media.Queues.UpdateActivity.Hdr](./updateactivity-data.dictionary/hdr-data.dictionary.md)
  Headers to include with requests to the update activity endpoint.

## Properties

- `url` (string): The relative path for the client to access `updateActivity`.

  **Default**: `/queues/updateActivity`; **Minimum Length**: `1`; **Maximum Length**: `4000`
- `hdr` (ExtensionConfig.Media.Queues.UpdateActivity.Hdr): Headers to include with requests to this endpoint.

## See Also

### Requiring Headers and Specifying Paths for Specific Queue Endpoints
- [object ExtensionConfig.Media.Queues.PlayMedia](./playmedia-data.dictionary.md)
  Configuration details for your service’s media playback queue.
- [object ExtensionConfig.Media.Queues.ContentPlaybackFailure](./contentplaybackfailure-data.dictionary.md)
  Configuration details for your service’s content playback failure endpoint.
- [object ExtensionConfig.Media.Queues.ContentProtectionKey](./contentprotectionkey-data.dictionary.md)
  Configuration details for your service’s content protection key endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig/media-data.dictionary/queues-data.dictionary/updateactivity-data.dictionary)*