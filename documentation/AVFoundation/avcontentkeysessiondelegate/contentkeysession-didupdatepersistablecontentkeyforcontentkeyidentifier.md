# contentKeySession(_:didUpdatePersistableContentKey:forContentKeyIdentifier:)

**Framework**: AVFoundation  
**Kind**: method

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

#### Discussion

If the content key session provides updated persistable content key data, previous key data is no longer valid and cannot be used to answer future loading requests.

## Parameters

- `session`: The content key session that is providing the updated persistable content key.
- `persistableContentKey`: The updated persistent content key data. This data can be stored offline and used to answer future content key requests with the matching key identifier.
- `keyIdentifier`: A container- and protocol-specific identifier for the updated persistent content key.

## See Also

- [func contentKeySession(AVContentKeySession, didProvide: [AVContentKeyRequest], forInitializationData: Data?)](avcontentkeysessiondelegate/contentkeysession(_:didprovide:forinitializationdata:).md)
- [func contentKeySession(AVContentKeySession, externalProtectionStatusDidChangeFor: AVContentKey)](avcontentkeysessiondelegate/contentkeysession(_:externalprotectionstatusdidchangefor:).md)
  Tells the delegate when external protection state has changed.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didupdatepersistablecontentkey:forcontentkeyidentifier:))*