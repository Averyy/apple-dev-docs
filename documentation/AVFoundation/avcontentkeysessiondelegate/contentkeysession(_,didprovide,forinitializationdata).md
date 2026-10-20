# contentKeySession(_:didProvide:forInitializationData:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
optional func contentKeySession(_ session: AVContentKeySession, didProvide keyRequests: [AVContentKeyRequest], forInitializationData initializationData: Data?)
```

```objc
- (void) contentKeySession:(AVContentKeySession *) session didProvideContentKeyRequests:(NSArray<AVContentKeyRequest *> *) keyRequests forInitializationData:(NSData *) initializationData;
```

## See Also

### Updating and retrying content key requests
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
- [func contentKeySessionDidGenerateExpiredSessionReport(AVContentKeySession)](./contentkeysessiondidgenerateexpiredsessionreport%28_%29.md)
  Notifies the sender that an expired session report has been generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didprovide:forinitializationdata:))*