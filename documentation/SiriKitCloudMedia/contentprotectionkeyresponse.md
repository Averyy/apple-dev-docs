# ContentProtectionKeyResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A response to a request for an item’s content protection key.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ContentProtectionKeyResponse
```

## Properties

- `keyResponse` (byte): An encrypted key response that contains the item’s content key. For FairPlay Streaming, this is the content key context (CKC); for more information, see [`FairPlay Streaming Overview`](https://developer.apple.comhttps://developer.apple.com/streaming/fps/FairPlayStreamingOverview.pdf).
- `keySystem` (ContentProtectionKeySystem): The content’s encryption type, which matches the configuration in  [`ExtensionConfig.Media.Queues.ContentProtectionKey.Cks`](extensionconfig/media-data.dictionary/queues-data.dictionary/contentprotectionkey-data.dictionary/cks-data.dictionary.md).
- `leaseRenewalDeadline` (double): The length of time, in seconds, before the content key expires. If your service doesn’t impose time limits, return `0`.
- `version` (string): The version of the client’s `SiriKitMediaAPI` library.

## See Also

- [Retrieve an Asset’s Content Protection Key](contentprotectionkey.md)
  Provide the content key for a specific protected asset.
- [object ContentProtectionKeyRequest](contentprotectionkeyrequest.md)
  A request for an item’s content protection key.
- [type ContentProtectionKeySystem](contentprotectionkeysystem.md)
  The content protection key systems that SiriKit Cloud Media supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/contentprotectionkeyresponse)*