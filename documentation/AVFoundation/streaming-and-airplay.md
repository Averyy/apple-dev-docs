# Streaming and AirPlay

**Framework**: AVFoundation

Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.

## Topics

### Essentials
- [Supporting AirPlay in your app](supporting-airplay-in-your-app.md)
  Set up your app to use AirPlay to send content wirelessly.
### Route selection
- [class AVRouteDetector](avroutedetector.md)
  An object that detects available media playback routes.
### Buffered playback
- [Implementing simple enhanced buffering for your content](implementing-simple-enhanced-buffering-for-your-content.md)
  Configure your app for simple enhanced buffering to stream content faster to AirPlay-enabled devices and supported CarPlay vehicles.
- [Implementing flexible enhanced buffering for your content](implementing-flexible-enhanced-buffering-for-your-content.md)
  Configure your app for flexible enhanced buffering to stream content faster to AirPlay-enabled devices and supported CarPlay vehicles.
- [Integrating AirPlay for Long-Form Video Apps](integrating-airplay-for-long-form-video-apps.md)
  Integrate AirPlay features and implement a dedicated external playback experience by preparing the routing system for long-form video playback.
### Resource loading
- [class AVAssetResourceLoader](avassetresourceloader.md)
  An object that mediates resource requests from a URL asset.
- [protocol AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md)
  Methods you can implement to handle resource-loading requests coming from a URL asset.
- [class AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md)
  An object that encapsulates information about a resource request from a resource loader object.
- [class AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md)
  An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [class AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md)
  An object that contains information about the originator of a resource-loading request.
- [class AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md)
  An object for requesting data from a resource that an asset resource-loading request references.
- [class AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md)
  A query for retrieving essential information about a resource that an asset resource-loading request references.
### FairPlay Streaming
- [class AVContentKeySession](avcontentkeysession.md)
  An object that creates and tracks decryption keys for media data.
- [protocol AVContentKeySessionDelegate](avcontentkeysessiondelegate.md)
  A protocol that handles content key requests.
- [class AVContentKey](avcontentkey.md)
  An object that represents the content key decryptor.
- [class AVContentKeySpecifier](avcontentkeyspecifier.md)
  An object that uniquely identifies a content key.
- [class AVContentKeyRequest](avcontentkeyrequest.md)
  An object that encapsulates information about a content decryption key request issued from a content key session object.
- [class AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md)
  An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [class AVContentKeyResponse](avcontentkeyresponse.md)
  An object that encapsulates information about a response to a content decryption key request.
- [enum AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md)
  Constants that specify whether sufficient protection exists to display the content.
- [func AVSampleBufferAttachContentKey(CMSampleBuffer, AVContentKey, NSErrorPointer) -> Bool](avsamplebufferattachcontentkey(_:_:_:).md)
  Attaches a content key to a sample buffer for the purpose of content decryption.

## See Also

- [Media playback](media-playback.md)
  Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.
- [Offline playback and storage](offline-playback-and-storage.md)
  Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.
- [Sample buffer playback](sample-buffer-playback.md)
  Create custom controllers to play and synchronize the timing of sample buffer streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/streaming-and-airplay)*