# ExtensionConfig

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Instructions for accessing your media service’s endpoints.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ExtensionConfig
```

## Topics

### Specifying Request Headers
- [object ExtensionConfig.Hdr](extensionconfig/hdr-data.dictionary.md)
  Headers to include with all requests to the media service.
- [object ExtensionEndpointConfig.Hdr](extensionendpointconfig/hdr-data.dictionary.md)
  Headers to include with requests to intent endpoints.
- [object ExtensionConfig.Intent.Hdr](extensionconfig/intent-data.dictionary/hdr-data.dictionary.md)
  Headers to include with requests to intent endpoints.
- [object ExtensionConfig.Media.Queues.Hdr](extensionconfig/media-data.dictionary/queues-data.dictionary/hdr-data.dictionary.md)
  Headers to include with requests to media endpoints.
- [object ExtensionConfig.Media.Queues.PlayMedia.Hdr](extensionconfig/media-data.dictionary/queues-data.dictionary/playmedia-data.dictionary/hdr-data.dictionary.md)
  Headers to include with requests to media endpoints.
- [object ExtensionConfig.Media.Queues.UpdateActivity.Hdr](extensionconfig/media-data.dictionary/queues-data.dictionary/updateactivity-data.dictionary/hdr-data.dictionary.md)
  Headers to include with requests to the update activity endpoint.
### Describing Supported Intent Endpoints
- [object ExtensionEndpointConfig](extensionendpointconfig.md)
  Instructions for accessing an intent endpoint.
- [object ExtensionConfig.Intent](extensionconfig/intent-data.dictionary.md)
  Instructions for accessing your media service’s intent endpoints.
### Describing Supported Media Endpoints
- [object ExtensionConfig.Media](extensionconfig/media-data.dictionary.md)
  Instructions for accessing your service’s media endpoints.

## See Also

- [Configure Your Service Endpoints](configuration-resource.md)
  Provide configuration details for your media server’s endpoints to a HomePod speaker or an Apple TV.
- [type ExtensionConfigTag](extensionconfigtag.md)
  A unique identifier for a specific media service configuration.
- [object PlayMediaControlActivity](playmediacontrolactivity.md)
  Options for reporting playback progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig)*