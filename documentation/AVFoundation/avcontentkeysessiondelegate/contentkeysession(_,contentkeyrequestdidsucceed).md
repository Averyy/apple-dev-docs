# contentKeySession(_:contentKeyRequestDidSucceed:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the content key session that the response to a content key requeset was successfully processed.

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
optional func contentKeySession(_ session: AVContentKeySession, contentKeyRequestDidSucceed keyRequest: AVContentKeyRequest)
```

```objc
- (void) contentKeySession:(AVContentKeySession *) session contentKeyRequestDidSucceed:(AVContentKeyRequest *) keyRequest;
```

## Parameters

- `session`: The [`AVContentKeySession`](../avcontentkeysession.md) instance that initiated the content key request.
- `keyRequest`: The [`AVContentKeyRequest`](../avcontentkeyrequest.md) instance whose response was successfully processed.

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
- [func contentKeySessionDidGenerateExpiredSessionReport(AVContentKeySession)](./contentkeysessiondidgenerateexpiredsessionreport%28_%29.md)
  Notifies the sender that an expired session report has been generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequestdidsucceed:))*