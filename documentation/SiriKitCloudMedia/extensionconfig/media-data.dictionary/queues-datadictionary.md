# ExtensionConfig.Media.Queues

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Configuration details for your service’s media queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ExtensionConfig.Media.Queues
```

## Topics

### Requiring Headers for all Queue Requests
- [object ExtensionConfig.Media.Queues.Hdr](extensionconfig/media-data.dictionary/queues-data.dictionary/hdr-data.dictionary.md)
  Headers to include with requests to media endpoints.
### Requiring Headers and Specifying Paths for Specific Queue Endpoints
- [object ExtensionConfig.Media.Queues.PlayMedia](extensionconfig/media-data.dictionary/queues-data.dictionary/playmedia-data.dictionary.md)
  Configuration details for your service’s media playback queue.
- [object ExtensionConfig.Media.Queues.UpdateActivity](extensionconfig/media-data.dictionary/queues-data.dictionary/updateactivity-data.dictionary.md)
  Configuration details for your service’s update activity endpoint.
- [object ExtensionConfig.Media.Queues.ContentPlaybackFailure](extensionconfig/media-data.dictionary/queues-data.dictionary/contentplaybackfailure-data.dictionary.md)
  Configuration details for your service’s content playback failure endpoint.
- [object ExtensionConfig.Media.Queues.ContentProtectionKey](extensionconfig/media-data.dictionary/queues-data.dictionary/contentprotectionkey-data.dictionary.md)
  Configuration details for your service’s content protection key endpoint.

## Properties

- `hdr` (ExtensionConfig.Media.Queues.Hdr): Headers to include with requests to queue endpoints.
- `playMedia` (ExtensionConfig.Media.Queues.PlayMedia): Details specific to your media playback queue.
- `updateActivity` (ExtensionConfig.Media.Queues.UpdateActivity): Details specific to your update activity endpoint.
- `contentPlaybackFailure` (ExtensionConfig.Media.Queues.ContentPlaybackFailure): Details specific to your content playback failure endpoint.
- `contentProtectionKey` (ExtensionConfig.Media.Queues.ContentProtectionKey): Details specific to your content protection key endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig/media-data.dictionary/queues-data.dictionary)*