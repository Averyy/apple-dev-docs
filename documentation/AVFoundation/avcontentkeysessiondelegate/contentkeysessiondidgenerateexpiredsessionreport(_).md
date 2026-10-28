# contentKeySessionDidGenerateExpiredSessionReport(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Notifies the sender that an expired session report has been generated.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
optional func contentKeySessionDidGenerateExpiredSessionReport(_ session: AVContentKeySession)
```

```objc
- (void) contentKeySessionDidGenerateExpiredSessionReport:(AVContentKeySession *) session;
```

## Discussion

This method is invoked when an expired session report is added to the [`storageURL`](../avcontentkeysession/storageurl.md) property.

## Parameters

- `session`: The [`AVContentKeySession`](../avcontentkeysession.md) object that recorded the generation of an expired session report.

## See Also

### Updating and retrying content key requests
- [func contentKeySession(AVContentKeySession, didProvide: [AVContentKeyRequest], forInitializationData: Data?)](./contentkeysession%28_,didprovide,forinitializationdata%29.md)
- [func contentKeySession(AVContentKeySession, externalProtectionStatusDidChangeFor: AVContentKey)](./contentkeysession%28_,externalprotectionstatusdidchangefor%29.md)
  Tells the delegate when external protection state has changed.
- [func contentKeySession(AVContentKeySession, didUpdatePersistableContentKey: Data, forContentKeyIdentifier: Any)](./contentkeysession%28_,didupdatepersistablecontentkey,forcontentkeyidentifier%29.md)
  Provides the receiver with an updated persistable content key for a specific key request.
- [func contentKeySession(AVContentKeySession, shouldRetry: AVContentKeyRequest, reason: AVContentKeyRequest.RetryReason) -> Bool](./contentkeysession%28_,shouldretry,reason%29.md)
  Provides the receiver with a content key request object to retry.
- [AVContentKeyRequest.RetryReason](../avcontentkeyrequest/retryreason.md)
  The reason for asking the client to retry a content key request.
- [func contentKeySessionContentProtectionSessionIdentifierDidChange(AVContentKeySession)](./contentkeysessioncontentprotectionsessionidentifierdidchange%28_%29.md)
  Tells the receiver the content protection session identifier changed.
- [func contentKeySession(AVContentKeySession, contentKeyRequest: AVContentKeyRequest, didFailWithError: any Error)](./contentkeysession%28_,contentkeyrequest,didfailwitherror%29.md)
  Tells the receiver that the content key request failed.
- [func contentKeySession(AVContentKeySession, contentKeyRequestDidSucceed: AVContentKeyRequest)](./contentkeysession%28_,contentkeyrequestdidsucceed%29.md)
  Tells the content key session that the response to a content key requeset was successfully processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysessiondidgenerateexpiredsessionreport(_:))*