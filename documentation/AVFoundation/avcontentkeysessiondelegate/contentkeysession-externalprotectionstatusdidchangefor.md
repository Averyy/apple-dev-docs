# contentKeySession(_:externalProtectionStatusDidChangeFor:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate when external protection state has changed.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func contentKeySession(_ session: AVContentKeySession, externalProtectionStatusDidChangeFor contentKey: AVContentKey)
```

## See Also

- [func contentKeySession(AVContentKeySession, didProvide: [AVContentKeyRequest], forInitializationData: Data?)](avcontentkeysessiondelegate/contentkeysession(_:didprovide:forinitializationdata:).md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:externalprotectionstatusdidchangefor:))*