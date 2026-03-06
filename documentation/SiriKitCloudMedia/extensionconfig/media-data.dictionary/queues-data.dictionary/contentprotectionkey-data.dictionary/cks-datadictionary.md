# ExtensionConfig.Media.Queues.ContentProtectionKey.Cks

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Configuration details for your service’s content protection system.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ExtensionConfig.Media.Queues.ContentProtectionKey.Cks
```

## Properties

- `certUrl` (string): The URL of the certicate the client must use to sign requests to the `contentProtectionKey` endpoint. For more information, see [`contentProtectionKey`](extensionconfig/media-data.dictionary/queues-data.dictionary/contentprotectionkey-data.dictionarykey.md).
- `keySystem` (ContentProtectionKeySystem) *(required)*: The content’s encryption type. The only supported value is `ContentKeySystemFairPlayStreaming`.

## See Also

- [object ExtensionConfig.Media.Queues.ContentProtectionKey.Hdr](extensionconfig/media-data.dictionary/queues-data.dictionary/contentprotectionkey-data.dictionary/hdr-data.dictionary.md)
  Headers to include with requests to the content protection key endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig/media-data.dictionary/queues-data.dictionary/contentprotectionkey-data.dictionary/cks-data.dictionary)*