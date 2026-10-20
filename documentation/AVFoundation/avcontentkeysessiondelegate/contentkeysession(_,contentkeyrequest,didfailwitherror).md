# contentKeySession(_:contentKeyRequest:didFailWithError:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the receiver that the content key request failed.

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
optional func contentKeySession(_ session: AVContentKeySession, contentKeyRequest keyRequest: AVContentKeyRequest, didFailWithError err: any Error)
```

```objc
- (void) contentKeySession:(AVContentKeySession *) session contentKeyRequest:(AVContentKeyRequest *) keyRequest didFailWithError:(NSError *) err;
```

## Parameters

- `session`: The content key session that initiated the content key request.
- `keyRequest`: The content key request that failed.
- `err`: An instance of [`NSError`](../../Foundation/nserror.md) that describes the failure that occurred.

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
- [func contentKeySession(AVContentKeySession, contentKeyRequestDidSucceed: AVContentKeyRequest)](./contentkeysession%28_,contentkeyrequestdidsucceed%29.md)
  Tells the content key session that the response to a content key requeset was successfully processed.
- [func contentKeySessionDidGenerateExpiredSessionReport(AVContentKeySession)](./contentkeysessiondidgenerateexpiredsessionreport%28_%29.md)
  Notifies the sender that an expired session report has been generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequest:didfailwitherror:))*