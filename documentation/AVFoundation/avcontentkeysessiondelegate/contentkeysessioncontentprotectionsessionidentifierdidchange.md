# contentKeySessionContentProtectionSessionIdentifierDidChange(_:)

**Framework**: AVFoundation  
**Kind**: method

Tells the receiver the content protection session identifier changed.

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
optional func contentKeySessionContentProtectionSessionIdentifierDidChange(_ session: AVContentKeySession)
```

## Parameters

- `session`: The content key session to be notified.

## See Also

- [func contentKeySession(AVContentKeySession, didProvide: [AVContentKeyRequest], forInitializationData: Data?)](avcontentkeysessiondelegate/contentkeysession(_:didprovide:forinitializationdata:).md)
- [func contentKeySession(AVContentKeySession, externalProtectionStatusDidChangeFor: AVContentKey)](avcontentkeysessiondelegate/contentkeysession(_:externalprotectionstatusdidchangefor:).md)
  Tells the delegate when external protection state has changed.
- [func contentKeySession(AVContentKeySession, didUpdatePersistableContentKey: Data, forContentKeyIdentifier: Any)](avcontentkeysessiondelegate/contentkeysession(_:didupdatepersistablecontentkey:forcontentkeyidentifier:).md)
  Provides the receiver with an updated persistable content key for a specific key request.
- [func contentKeySession(AVContentKeySession, shouldRetry: AVContentKeyRequest, reason: AVContentKeyRequest.RetryReason) -> Bool](avcontentkeysessiondelegate/contentkeysession(_:shouldretry:reason:).md)
  Provides the receiver with a content key request object to retry.
- [AVContentKeyRequest.RetryReason](avcontentkeyrequest/retryreason.md)
  The reason for asking the client to retry a content key request.
- [func contentKeySession(AVContentKeySession, contentKeyRequest: AVContentKeyRequest, didFailWithError: any Error)](avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequest:didfailwitherror:).md)
  Tells the receiver that the content key request failed.
- [func contentKeySession(AVContentKeySession, contentKeyRequestDidSucceed: AVContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequestdidsucceed:).md)
  Tells the content key session that the response to a content key requeset was successfully processed.
- [func contentKeySessionDidGenerateExpiredSessionReport(AVContentKeySession)](avcontentkeysessiondelegate/contentkeysessiondidgenerateexpiredsessionreport(_:).md)
  Notifies the sender that an expired session report has been generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysessioncontentprotectionsessionidentifierdidchange(_:))*