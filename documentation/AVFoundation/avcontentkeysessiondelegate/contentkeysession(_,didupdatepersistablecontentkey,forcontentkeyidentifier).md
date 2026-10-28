# contentKeySession(_:didUpdatePersistableContentKey:forContentKeyIdentifier:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Provides the receiver with an updated persistable content key for a specific key request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
optional func contentKeySession(_ session: AVContentKeySession, didUpdatePersistableContentKey persistableContentKey: Data, forContentKeyIdentifier keyIdentifier: Any)
```

```objc
- (void) contentKeySession:(AVContentKeySession *) session didUpdatePersistableContentKey:(NSData *) persistableContentKey forContentKeyIdentifier:(id) keyIdentifier;
```

## Discussion

If the content key session provides updated persistable content key data, previous key data is no longer valid and cannot be used to answer future loading requests.

## Parameters

- `session`: The content key session that is providing the updated persistable content key.
- `persistableContentKey`: The updated persistent content key data. This data can be stored offline and used to answer future content key requests with the matching key identifier.
- `keyIdentifier`: A container- and protocol-specific identifier for the updated persistent content key.

## See Also

### Updating and retrying content key requests
- [func contentKeySession(AVContentKeySession, didProvide: [AVContentKeyRequest], forInitializationData: Data?)](./contentkeysession%28_,didprovide,forinitializationdata%29.md)
- [func contentKeySession(AVContentKeySession, externalProtectionStatusDidChangeFor: AVContentKey)](./contentkeysession%28_,externalprotectionstatusdidchangefor%29.md)
  Tells the delegate when external protection state has changed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didupdatepersistablecontentkey:forcontentkeyidentifier:))*