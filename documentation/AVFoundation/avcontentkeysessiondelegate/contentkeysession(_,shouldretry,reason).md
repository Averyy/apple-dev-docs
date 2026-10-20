# contentKeySession(_:shouldRetry:reason:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Provides the receiver with a content key request object to retry.

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
optional func contentKeySession(_ session: AVContentKeySession, shouldRetry keyRequest: AVContentKeyRequest, reason retryReason: AVContentKeyRequest.RetryReason) -> Bool
```

```objc
- (BOOL) contentKeySession:(AVContentKeySession *) session shouldRetryContentKeyRequest:(AVContentKeyRequest *) keyRequest reason:(AVContentKeyRequestRetryReason) retryReason;
```

## Parameters

- `session`: The content key session that is providing the content key request.
- `keyRequest`: The key request to be retried.
- `retryReason`: The reason for the retry request.

## See Also

### Updating and retrying content key requests
- [func contentKeySession(AVContentKeySession, didProvide: [AVContentKeyRequest], forInitializationData: Data?)](./contentkeysession%28_,didprovide,forinitializationdata%29.md)
- [func contentKeySession(AVContentKeySession, externalProtectionStatusDidChangeFor: AVContentKey)](./contentkeysession%28_,externalprotectionstatusdidchangefor%29.md)
  Tells the delegate when external protection state has changed.
- [func contentKeySession(AVContentKeySession, didUpdatePersistableContentKey: Data, forContentKeyIdentifier: Any)](./contentkeysession%28_,didupdatepersistablecontentkey,forcontentkeyidentifier%29.md)
  Provides the receiver with an updated persistable content key for a specific key request.
- [AVContentKeyRequest.RetryReason](../avcontentkeyrequest/retryreason.md)
  The reason for asking the client to retry a content key request.
- [func contentKeySessionContentProtectionSessionIdentifierDidChange(AVContentKeySession)](./contentkeysessioncontentprotectionsessionidentifierdidchange%28_%29.md)
  Tells the receiver the content protection session identifier changed.
- [func contentKeySession(AVContentKeySession, contentKeyRequest: AVContentKeyRequest, didFailWithError: any Error)](./contentkeysession%28_,contentkeyrequest,didfailwitherror%29.md)
  Tells the receiver that the content key request failed.
- [func contentKeySession(AVContentKeySession, contentKeyRequestDidSucceed: AVContentKeyRequest)](./contentkeysession%28_,contentkeyrequestdidsucceed%29.md)
  Tells the content key session that the response to a content key requeset was successfully processed.
- [func contentKeySessionDidGenerateExpiredSessionReport(AVContentKeySession)](./contentkeysessiondidgenerateexpiredsessionreport%28_%29.md)
  Notifies the sender that an expired session report has been generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:shouldretry:reason:))*