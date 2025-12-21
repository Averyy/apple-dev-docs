# AVContentKeySessionDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that handles content key requests.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
protocol AVContentKeySessionDelegate : NSObjectProtocol, Sendable
```

## Topics

### Providing new content key requests
- [func contentKeySession(AVContentKeySession, didProvide: AVContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-3coq5.md)
  Provides the receiver with a new content key request object.
- [func contentKeySession(AVContentKeySession, didProvideRenewingContentKeyRequest: AVContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:didproviderenewingcontentkeyrequest:).md)
  Provides the receiver with a new content key request object for the renewal of an existing content key.
- [func contentKeySession(AVContentKeySession, didProvide: AVPersistableContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-2wdgz.md)
  Provides the receiver with a new content key request object to process a persistable content key.
### Updating and retrying content key requests
- [func contentKeySession(AVContentKeySession, didProvide: [AVContentKeyRequest], forInitializationData: Data?)](avcontentkeysessiondelegate/contentkeysession(_:didprovide:forinitializationdata:).md)
- [func contentKeySession(AVContentKeySession, externalProtectionStatusDidChangeFor: AVContentKey)](avcontentkeysessiondelegate/contentkeysession(_:externalprotectionstatusdidchangefor:).md)
  Tells the delegate when external protection state has changed.
- [func contentKeySession(AVContentKeySession, didUpdatePersistableContentKey: Data, forContentKeyIdentifier: Any)](avcontentkeysessiondelegate/contentkeysession(_:didupdatepersistablecontentkey:forcontentkeyidentifier:).md)
  Provides the receiver with an updated persistable content key for a specific key request.
- [func contentKeySession(AVContentKeySession, shouldRetry: AVContentKeyRequest, reason: AVContentKeyRequest.RetryReason) -> Bool](avcontentkeysessiondelegate/contentkeysession(_:shouldretry:reason:).md)
  Provides the receiver with a content key request object to retry.
- [AVContentKeyRequest.RetryReason](avcontentkeyrequest/retryreason.md)
  The reason for asking the client to retry a content key request.
- [func contentKeySessionContentProtectionSessionIdentifierDidChange(AVContentKeySession)](avcontentkeysessiondelegate/contentkeysessioncontentprotectionsessionidentifierdidchange(_:).md)
  Tells the receiver the content protection session identifier changed.
- [func contentKeySession(AVContentKeySession, contentKeyRequest: AVContentKeyRequest, didFailWithError: any Error)](avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequest:didfailwitherror:).md)
  Tells the receiver that the content key request failed.
- [func contentKeySession(AVContentKeySession, contentKeyRequestDidSucceed: AVContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequestdidsucceed:).md)
  Tells the content key session that the response to a content key requeset was successfully processed.
- [func contentKeySessionDidGenerateExpiredSessionReport(AVContentKeySession)](avcontentkeysessiondelegate/contentkeysessiondidgenerateexpiredsessionreport(_:).md)
  Notifies the sender that an expired session report has been generated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVContentKeySession](avcontentkeysession.md)
  An object that creates and tracks decryption keys for media data.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate)*