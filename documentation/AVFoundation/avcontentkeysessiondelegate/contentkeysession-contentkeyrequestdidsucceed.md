# contentKeySession(_:contentKeyRequestDidSucceed:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `session`: The   instance that initiated the content key request.
- `keyRequest`: The   instance whose response was successfully processed.

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
- [func contentKeySessionContentProtectionSessionIdentifierDidChange(AVContentKeySession)](avcontentkeysessiondelegate/contentkeysessioncontentprotectionsessionidentifierdidchange(_:).md)
  Tells the receiver the content protection session identifier changed.
- [func contentKeySession(AVContentKeySession, contentKeyRequest: AVContentKeyRequest, didFailWithError: any Error)](avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequest:didfailwitherror:).md)
  Tells the receiver that the content key request failed.
- [func contentKeySessionDidGenerateExpiredSessionReport(AVContentKeySession)](avcontentkeysessiondelegate/contentkeysessiondidgenerateexpiredsessionreport(_:).md)
  Notifies the sender that an expired session report has been generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequestdidsucceed:))*